---
title: "Playing Tag! Extending Obsidians capability to analyse tags with python"
date: 2023-05-21
image: /images/placeholder.svg
---

> Icon or eyesore? 
> 
> 
> Yashica Electro 35 on Arcos debed in XTOL 1:1

I had a slight frustration with my latest efforts to use Obsidian as a tool for qualitative analysis. This arises mainly from how I'm trying to use tags as codes on notes or passages of dialog. The beauty of Obsidian is however that the files are stored as straight forward markdown and in normal folder structures. Here I get ChatGPT to help me write a  custom Python script designed to search a specified folder and find all tags in each note and output to a csv for later analysis.

In Obsidian, tags are used by simply adding a # symbol in front of a keyword. While Obsidian has built-in features for working with tags, it doesn't provide a direct functionality to examine the co-occurrence of tags across different notes or ot export a list of your notes with all the tags this note contains as a table or a csv. This is where our Python script comes into play.

The specific application I'm working on is a card sorting activity and here I want to be able to highlight a passage of text and create a memo from it but also attach a tag for which card and tags that code for the participants response to that card. So I have a card called "Salary" we're interested in finding all tags that co-occur in notes with that specific target tag #salary. This kind of analysis can give us insights into related topics and how different topics are interconnected. So whats here is a Python script to find all notes in an Obsidian vault (its just a folder on your hard drive folks) where a specific target tag appears, and then count all *other tags* that appear in those notes. This script Python's built-in modules like os for file and directory operations, re for regular expressions (regex), and collections for efficient counting.

The script works as follows:

It iterates over all markdown files (notes) in the specified Obsidian vault.

For each note, it finds all tags (using a regex pattern).

If the target tag is found in the note, it increments a count for every other tag in the note.

Finally, it prints the co-occurring tags along with their counts and writes the results to a CSV file.

The ability to see and count tag co-occurrences can significantly enhance an Obsidian user's understanding of their notes. It allows us to identify themes and relationships among different topics. Furthermore, exporting this data to a CSV file opens up opportunities for further analysis using other tools like Excel or Python's data analysis libraries.

Here's the script (modify to taste):

import os
import re
import csv
from collections import defaultdict

# Path to your Obsidian vault
vault_path = '/path/to/your/vault'

# Target tag
target_tag = '#salary'

# Regex to find tags
tag_re = re.compile(r'#\w+')

# Dict to count co-occurring tags
tag_counts = defaultdict(int)

# Iterate over all notes in vault
for filename in os.listdir(vault_path):
    if filename.endswith('.md'):
        with open(os.path.join(vault_path, filename), 'r') as f:
            content = f.read()
            tags = tag_re.findall(content)
            if target_tag in tags:
                for tag in tags:
                    if tag != target_tag:
                        tag_counts[tag] += 1

# Write the results to a CSV file
with open('tag_counts.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Tag', 'Count'])
    for tag, count in tag_counts.items():
        writer.writerow([tag, count])

# Print co-occurring tags and their counts
for tag, count in tag_counts.items():
    print(f'{tag}: {count}')

Qualitative analysis typically involves a considerable amount of text-based data which requires sorting, labelling, and categorising - this is where coding comes into play. The Python script is effectively performing a co-occurrence analysis, which can be particularly useful in understanding which codes often occur together which can help to identify themes or relationships in the data that might not be immediately obvious. This could also be useful in code refinement as the ability to easily analyse these co-occurrences can support the iterative process of refining a codebook. Ultimately this will be useful in data driven theory building. 

The second code example is in some ways a simpler affair which just trawls through the specified folder in your vault and finds all the notes with tags attached and reports out these tags as a neatly formatted csv file. This could be transformed into a pivot table in something like excel to do crosstab analysis. 

import os
import re
import csv

# Directory where your Obsidian vault is stored
dir_path = '/path/to/your/vault'
# Regular expression to match tags
tag_re = re.compile(r"#\w+")

# A dictionary to store notes and their associated tags
notes = {}

# Walk through all files in the directory
for root, dirs, files in os.walk(dir_path):
    for file in files:
        # Only look at markdown files
        if file.endswith(".md"):
            with open(os.path.join(root, file), 'r') as f:
                contents = f.read()
                tags = tag_re.findall(contents)
                notes[file] = tags

# Write the note names and associated tags to a CSV file
with open('obsidian_tags.csv', 'w', newline='') as csvfile:
    fieldnames = ['note', 'tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for note, tags in notes.items():
        writer.writerow({'note': note, 'tags': ', '.join(tags)})