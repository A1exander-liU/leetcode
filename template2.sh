#!/bin/bash

pythonContents="class Solution:\n\tdef function(self) -> None:\n\t\treturn"
readmeContents="# Problem\n\n### Example 1\n\n### Solution"

# Iterate over each directory in the current directory
for dir in */; do
  # Trim the trailing slash from the directory name
  dir=${dir%/}

  # Check if it's a directory
  if [ -d "$dir" ]; then
    # Create solution.py in the directory
    echo pythonContents >"$dir/solution.py"
    echo readmeContents >"$dir/README.md"
    echo "Created solution.py in $dir"
  fi
done
