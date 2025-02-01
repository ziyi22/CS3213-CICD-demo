import os

filename = "Documentation.md"

if os.path.exists(filename):
    if os.path.getsize(filename) == 0:
        print(f"{filename} exists but is empty.")
        exit(1)
    else:
        print(f"{filename} exists and is not empty.")
        exit(0)
else:
    print(f"{filename} does not exist.")
    exit(1)