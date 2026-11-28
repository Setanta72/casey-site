"""
render_v6p2_orbit_video.py
Renders a seamless 360-degree Cycles Metal GPU turntable orbit video of the exact V6.2
KUMIKO-TRUSS Baltic birch + workshop-orange 3D-printed hardware lamp directly from the
FreeCAD V6.2 B-Rep meshes.

Run via Blender 5.2 CLI:
  /Applications/Blender.app/Contents/MacOS/Blender --background --python \
      /Users/setanta/Documents/Projects/OpenVis/KumikoTruss/01_standalone_showcase/render_v6p2_orbit_video.py
"""

import os
import math
import bpy
from mathutils import Vector

MESH_DIR   = "/tmp/v6p2_blender_meshes"
FRAMES_DIR = "/tmp/v6p2_orbit_frames"
os.makedirs(FRAMES_DIR, exist_ok=True)

N_FRAMES = 120
RES_X, RES_Y = 1280, 720

# Clear default scene
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.engine = "CYCLES"
scene.cycles.device = "GPU"
scene.cycles.samples = 28
scene.cycles.use_denoising = True
scene.cycles.denoiser = "OPENIMAGEDENOISE"
scene.cycles.max_bounces = 6
scene.cycles.diffuse_bounces = 3
scene.cycles.glossy_bounces = 3
scene.cycles.transmission_bounces = 2
scene.cycles.transparent_max_bounces = 4

# Enable Apple Metal GPU cleanly
prefs = bpy.context.preferences.addons["cycles"].preferences
try:
    prefs.compute_device_type = "METAL"
    prefs.get_devices()
    for d in prefs.devices:
        d.use = (d.type == "METAL")
except Exception as e:
    print("Metal setup note:", e)

scene.render.resolution_x = RES_X
scene.render.resolution_y = RES_Y
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.render.fps = 24
scene.view_settings.view_transform = "AgX"
try:
    scene.view_settings.look = "AgX - Punchy"
except Exception:
    pass
scene.view_settings.exposure = -0.55


def make_birch_mat():
    mat = bpy.data.materials.new("Baltic_Birch_Ply")
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    texc = nt.nodes.new("ShaderNodeTexCoord")
    mp = nt.nodes.new("ShaderNodeMapping")
    mp.inputs["Scale"].default_value = (8.0, 28.0, 95.0)
    noise = nt.nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value = 3.6
    noise.inputs["Detail"].default_value = 7.0
    noise.inputs["Distortion"].default_value = 1.6
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.22
    ramp.color_ramp.elements[0].color = (0.42, 0.27, 0.14, 1.0)
    ramp.color_ramp.elements[1].position = 0.78
    ramp.color_ramp.elements[1].color = (0.72, 0.54, 0.34, 1.0)

    ao = nt.nodes.new("ShaderNodeAmbientOcclusion")
    ao.inputs["Distance"].default_value = 0.025
    mix_ao = nt.nodes.new("ShaderNodeMix")
    mix_ao.data_type = "RGBA"
    mix_ao.blend_type = "MULTIPLY"
    mix_ao.inputs["Factor"].default_value = 0.48

    bsdf.inputs["Roughness"].default_value = 0.42
    if "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = 0.15
        bsdf.inputs["Coat Roughness"].default_value = 0.28

    nt.links.new(texc.outputs["Object"], mp.inputs["Vector"])
    nt.links.new(mp.outputs["Vector"], noise.inputs["Vector"])
    nt.links.new(noise.outputs["Fac"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], mix_ao.inputs[6])
    nt.links.new(ao.outputs["Color"], mix_ao.inputs[7])
    nt.links.new(mix_ao.outputs[2], bsdf.inputs["Base Color"])
    nt.links.new(bsdf.outputs["BSDF"], out.inputs["Surface"])
    return mat


def make_pbr_mat(name, rgba, rough=0.35, metal=0.0, coat=0.0, emit=None, emit_strength=0.0):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = rgba
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Metallic"].default_value = metal
    if coat > 0.0 and "Coat Weight" in bsdf.inputs:
        bsdf.inputs["Coat Weight"].default_value = coat
        bsdf.inputs["Coat Roughness"].default_value = 0.22
    if emit is not None and emit_strength > 0.0:
        bsdf.inputs["Emission Color"].default_value = emit
        bsdf.inputs["Emission Strength"].default_value = emit_strength
    return mat


mats = {
    "birch_ply":       make_birch_mat(),
    "fdm_orange":      make_pbr_mat("Workshop_Orange_PETG", (0.78, 0.11, 0.015, 1.0), rough=0.26, coat=0.30),
    "tpu_dark":        make_pbr_mat("TPU_Charcoal",         (0.04, 0.042, 0.045, 1.0), rough=0.68),
    "steel_hw":        make_pbr_mat("BlackOxide_Steel",     (0.11, 0.125, 0.145, 1.0), rough=0.26, metal=0.90),
    "nylon_bulb_body": make_pbr_mat("Nylon_And_IKEA_White", (0.85, 0.83, 0.79, 1.0),   rough=0.36),
    "bulb_lens_glow":  make_pbr_mat("IKEA_2700K_Glow",      (1.0, 0.82, 0.52, 1.0),    rough=0.2,
                                    emit=(1.0, 0.68, 0.30, 1.0), emit_strength=32.0),
}

# Import all 6 V6.2 CAD meshes (mm -> m via scale 0.001) with clean outward normals + EdgeSplit!
imported = []
for stem, mat in mats.items():
    fp = os.path.join(MESH_DIR, f"{stem}.stl")
    bpy.ops.wm.stl_import(filepath=fp, global_scale=0.001)
    obj = bpy.context.active_object
    obj.name = stem
    obj.data.materials.clear()
    obj.data.materials.append(mat)
    # Weld STL vertices & recalculate consistent outward normals to eliminate dark shading artefacts!
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.mesh.remove_doubles(threshold=1e-6)
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode="OBJECT")
    # Smooth curved corners while keeping every >=28° planar/wall edge mathematically crisp!
    bpy.ops.object.shade_smooth()
    es = obj.modifiers.new(name="CrispEdges", type="EDGE_SPLIT")
    es.use_edge_angle = True
    es.split_angle = math.radians(28.0)
    imported.append(obj)

# Compute bounding box center so lamp orbits around its true visual centroid!
all_pts = [o.matrix_world @ Vector(b) for o in imported for b in o.bound_box]
min_z = min(p.z for p in all_pts)
max_z = max(p.z for p in all_pts)
cx = 0.5 * (min(p.x for p in all_pts) + max(p.x for p in all_pts))
cy = 0.5 * (min(p.y for p in all_pts) + max(p.y for p in all_pts))
# Shift lamp so its horizontal visual center sits at X=0, Y=0 and feet rest at Z=0!
for o in imported:
    o.location.x -= cx
    o.location.y -= cy
    o.location.z -= min_z

# Find bulb lens center in shifted world coordinates for real 2700K spot beam!
lens_obj = bpy.data.objects["bulb_lens_glow"]
lens_pts = [lens_obj.matrix_world @ Vector(b) for b in lens_obj.bound_box]
lens_ctr = sum(lens_pts, Vector((0, 0, 0))) / len(lens_pts)

# Architectural Studio Tabletop & Seamless Backdrop
bpy.ops.mesh.primitive_cylinder_add(vertices=96, radius=2.6, depth=0.02, location=(0, 0, -0.01))
floor = bpy.context.active_object
floor.name = "Studio_Floor"
floor.data.materials.append(make_pbr_mat("Studio_Paper", (0.58, 0.56, 0.52, 1.0), rough=0.72))

# Subtle raised architectural plinth disc directly under the lamp
bpy.ops.mesh.primitive_cylinder_add(vertices=96, radius=0.22, depth=0.014, location=(0, 0, -0.007))
plinth = bpy.context.active_object
plinth.name = "Studio_Plinth"
plinth.data.materials.append(make_pbr_mat("Plinth_Stone", (0.72, 0.70, 0.65, 1.0), rough=0.52))

# Clean warm architectural studio World environment
world = bpy.data.worlds.new("Studio_World")
scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes["Background"]
bg.inputs["Color"].default_value = (0.36, 0.35, 0.33, 1.0)
bg.inputs["Strength"].default_value = 0.42

def add_area(name, loc, rot_deg, energy, size_x, size_y, color):
    ld = bpy.data.lights.new(name, type="AREA")
    ld.energy = energy
    ld.shape = "RECTANGLE"
    ld.size = size_x
    ld.size_y = size_y
    ld.color = color
    lo = bpy.data.objects.new(name, ld)
    bpy.context.collection.objects.link(lo)
    lo.location = loc
    lo.rotation_euler = tuple(math.radians(a) for a in rot_deg)
    return lo

# 3-Point Warm Editorial Lighting (dramatic warm contrast showing the 2700K Kumiko light pool!)
add_area("Key_Light",  (0.90, -0.95, 0.95), (52, 0, 42),  34.0, 0.70, 0.55, (1.0, 0.96, 0.90))
add_area("Fill_Light", (-0.95, -0.60, 0.60), (65, 0, -56), 12.0, 0.90, 0.65, (0.85, 0.91, 1.0))
add_area("Rim_Light",  (-0.35, 1.05, 0.78), (62, 0, 160), 22.0, 0.85, 0.35, (1.0, 0.92, 0.82))

# Real 2700K IKEA LED Spot Light inside the Kumiko Shade (tilted 24 deg forward to match shade axis!)
spot_d = bpy.data.lights.new("IKEA_2700K_Beam", type="SPOT")
spot_d.energy = 26.0
spot_d.color = (1.0, 0.68, 0.30)
spot_d.spot_size = math.radians(74.0)
spot_d.spot_blend = 0.42
spot_d.shadow_soft_size = 0.012
spot_o = bpy.data.objects.new("IKEA_2700K_Beam", spot_d)
bpy.context.collection.objects.link(spot_o)
spot_o.location = lens_ctr + Vector((0.0, 0.0, -0.008))
spot_o.rotation_euler = (0.0, math.radians(-24.0), 0.0)

# Camera Orbit Rig — Full Lamp Framing (TPU feet to top wrist arch w/ studio margin!)
target = bpy.data.objects.new("Orbit_Target", None)
bpy.context.collection.objects.link(target)
target.location = (0.0, 0.0, 0.215)

rig = bpy.data.objects.new("Orbit_Rig", None)
bpy.context.collection.objects.link(rig)
rig.location = (0.0, 0.0, 0.0)

cam_d = bpy.data.cameras.new("Studio_Cam")
cam_d.lens = 48.0
cam_d.dof.use_dof = True
cam_d.dof.focus_object = target
cam_d.dof.aperture_fstop = 8.0
cam_o = bpy.data.objects.new("Studio_Cam", cam_d)
bpy.context.collection.objects.link(cam_o)
cam_o.parent = rig
cam_o.location = (0.88, -0.82, 0.42)  # Pull back cleanly so full 435mm lamp has generous margin on all 360 deg!
trk = cam_o.constraints.new(type="TRACK_TO")
trk.target = target
trk.track_axis = "TRACK_NEGATIVE_Z"
trk.up_axis = "UP_Y"
scene.camera = cam_o

# Render 120 exact linear 360-deg orbit frames (or just Frame 1 when ONLY_FRAME_1=1 for fast check!)
frames_to_render = [1] if os.environ.get("ONLY_FRAME_1") == "1" else list(range(1, N_FRAMES + 1))
for f in frames_to_render:
    ang = 2.0 * math.pi * (f - 1) / float(N_FRAMES)
    rig.rotation_euler = (0.0, 0.0, ang)
    scene.frame_set(f)
    scene.render.filepath = os.path.join(FRAMES_DIR, f"frame_{f:04d}.png")
    bpy.ops.render.render(write_still=True)
    if f in (1, 30, 60, 90, 120):
        print(f"Rendered orbit frame {f}/{N_FRAMES}")
print("BLENDER_ORBIT_FRAMES_OK")
