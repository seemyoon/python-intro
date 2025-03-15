# 1. Create a files folder in the current folder
# 2. Add two files first.txt and second.txt to this folder and write 2-3 strings of text to them
# 3. Read all text lines of the first file
# 4. Read the text lines of the second file one by one
# 5. Delete both files
# 6. Delete the files folder
from pathlib import Path

test_folder_path = Path("test-folder")

first_file_path = test_folder_path / "first.txt"
second_file_path = test_folder_path / "second.txt"

try:
    if not first_file_path.exists() and second_file_path.exists():
        raise TypeError(f"{test_folder_path} is not existed")

    with open(first_file_path, "w") as file:
        file.write("banana \n")
        file.write("grape \n")
        file.write("strawberry \n")

    with open(second_file_path, "w") as file:
        file.write("coca-cola \n")
        file.write("sprite \n")
        file.write("fanta \n")

    with open(first_file_path) as file:
        all_lines = file.readlines()
        print(all_lines)

    with open(second_file_path) as file:
        for line in file:
            print(line.strip())


except TypeError as e:
    print("error: ", e)

if first_file_path.exists():
    first_file_path.unlink()

if second_file_path.exists():
    second_file_path.unlink()

if test_folder_path.exists():
    test_folder_path.rmdir()

print("All files and folder deleted successfully!")
