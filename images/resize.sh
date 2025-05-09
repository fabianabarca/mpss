#!/bin/bash

# Loop through all SVG files in the current directory
for file in *.svg; do
    if [[ -f "$file" ]]; then
        echo "Processing $file..."
        # Use Inkscape CLI to resize and overwrite the SVG file
        inkscape --export-area-drawing --export-plain-svg --export-filename="$file" "$file"
        if [[ $? -eq 0 ]]; then
            echo "Successfully processed $file"
        else
            echo "Error processing $file"
        fi
    fi
done

echo "All SVG files have been processed."