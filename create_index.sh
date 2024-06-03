#!/bin/bash

# Navigate to the Knowledge Acquisition directory
cd "/Users/viraatd/Documents/Personal/viraat.lol/content/Knowledge Acquisition"

# Loop through each directory
for dir in */; do
  # Remove the trailing slash from the directory name
  dirname=${dir%/}
  
  # Create an index.md file with the appropriate title
  echo "---" > "$dirname/index.md"
  echo "title: $dirname" >> "$dirname/index.md"
  echo "---" >> "$dirname/index.md"
done

