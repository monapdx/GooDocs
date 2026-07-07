from pathlib import Path

# 1. Automatically get the directory where this script file is located
folder = Path(__file__).parent.resolve()

print(f"Searching for .gif files in: {folder}\n")

# 2. Find all .gif files (case-insensitive search for both .gif and .GIF)
# rglob stands for "recursive glob", which searches all sub-folders automatically.
gif_files = list(folder.rglob("*.[gG][iI][fF]"))

# 3. Display the results
if gif_files:
    print(f"Found {len(gif_files)} .gif image(s):")
    for file in gif_files:
        print(file)
else:
    print("No .gif files found.")