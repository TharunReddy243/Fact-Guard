import sys
import os
'''
# Ensure at least one file path is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <file1> <file2> ...")
    sys.exit(1)
'''

file_paths = sys.argv[1:]

for file_path in file_paths:
    try:
        with open(file_path, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("An error occurred while reading the file:", e)

    try:
        #os.remove(file_path)
        print("Deleted:", file_path)
    except Exception as e:
        print("An error occurred while deleting the file:", e)
