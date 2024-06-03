#!/bin/bash

# Iterate over each directory in the current directory
for dir in */; do
	# Trim the trailing slash from the directory name
	dir=${dir%/}

	# Check if it's a directory
	if [ -d "$dir" ]; then
		# Create solution.py in the directory
		touch "$dir/solution.py"
    touch "$dir/README.md"
		echo "Created solution.py in $dir"
	fi
done
