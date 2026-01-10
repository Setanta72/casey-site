import { defineCollection, z } from 'astro:content';

// Posts: dated writing (blog posts, opinions, tutorials)
const posts = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    draft: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
  }),
});

// Projects: ongoing work with updates (camera repairs, ceramic series, code projects)
const projects = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    started: z.coerce.date(),
    updated: z.coerce.date().optional(),
    status: z.enum(['active', 'complete', 'paused', 'archived']).default('active'),
    category: z.enum(['photography', 'ceramics', 'art', 'code', 'making', 'research']),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
  }),
});

// Pieces: single finished works (a photo, a pot, a painting, a 3D model)
const pieces = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    date: z.coerce.date(),
    category: z.enum(['photography', 'ceramics', 'art', 'code', 'making']),
    project: z.string().optional(), // Link to parent project if any
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
    dimensions: z.string().optional(),
    medium: z.string().optional(),
  }),
});

// Notes: quick reference material (process notes, technique reminders)
const notes = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    updated: z.coerce.date(),
    category: z.enum(['photography', 'ceramics', 'art', 'code', 'making', 'research']),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = { posts, projects, pieces, notes };
