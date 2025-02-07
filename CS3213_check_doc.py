import os

filename = "Documentation.md"

if os.path.exists(filename):
    if os.path.getsize(filename) == 0:
        print(f"{filename} is empty.")
        exit(1)
    else:
        print(f"Nice, you have a doc at {filename}.")
        exit(0)
else:
    print(f"{filename} does not exist.")
    exit(1)
