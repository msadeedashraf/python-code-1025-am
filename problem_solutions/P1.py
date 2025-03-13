"""
import os


# A function to list directories
def list_directories(path):
    for root, dir, files in os.walk(path):
        print(f"Directories : {root}")
        for directory in dir:
            print(f"Sub-directories : {directory}")
            for file in files:
                print(f"Files: {file}")


myPath = "D:\\CBC\\SEProject\\fsd_aug_2024_am\\python\\testfolder"
list_directories(myPath)
"""

"""
import os


def list_tree(path, level=0):
    #Recursively lists all directories and files in a tree-like structure with depth levels.
    try:
        items = sorted(os.listdir(path))  # Sort for better readability
        # print(items)
        for item in items:
            item_path = os.path.join(path, item)
            prefix = (
                "│   " * (level - 1) + "├── " if level > 0 else ""
            )  # Tree structure formatting
            print(prefix + item)
            if os.path.isdir(item_path):
                list_tree(item_path, level + 1)  # Recursively call for subdirectories
    except PermissionError:
        print("│   " * level + "🚫 Permission Denied")


myPath = "D:\\CBC\\SEProject\\fsd_aug_2024_am\\python\\testfolder"

print(f"Root: {myPath}")
list_tree(myPath)


"""


import os


def print_tree(path, level=0):
    """Recursively prints directories and files in a tree structure with depth."""
    try:
        items = sorted(os.listdir(path))  # Sort items for better readability
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print("│   " * level + "├── 📂 " + item)  # Directory icon
                print_tree(item_path, level + 1)  # Recursive call for subdirectories
            else:
                print("│   " * level + "├── 📄 " + item)  # File icon
    except PermissionError:
        print("│   " * level + "└── ❌ Permission Denied")


myPath = "D:\\CBC\\SEProject\\fsd_aug_2024_am\\python\\testfolder"

print(f"Root: {myPath}")
print_tree(myPath)
