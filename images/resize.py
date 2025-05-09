import os
import subprocess

# Get all SVG files in the current directory
svg_files = [f for f in os.listdir('.') if f.endswith('.svg')]

# Resize each SVG file to fit the content only
for svg_file in svg_files:
    try:
        subprocess.run(
            [
                "inkscape",
                "--export-area-drawing",
                "--export-plain-svg",
                f"--export-filename={svg_file}",
                svg_file,
            ],
            check=True,
        )
        print(f"Resized and overwritten: {svg_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {svg_file}: {e}")