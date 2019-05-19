import logging
import os
import re


def list_files() -> None:
    """
        List all the files in the dir directory
    """
    # Walk through the dir directory and grab the root, directories
    # and files within the directory
    for root, dirs, files in os.walk("dir"):
        for file in files:
            print(file)


def list_files_with_root() -> None:
    """
        List all files with the root directory attached
    """
    # Walk through the dir directory
    for root, dirs, files in os.walk("dir"):
        for file in files:
            # Join the paths together
            full_path = os.path.join(root, file)
            print(full_path)


def find_pdfs() -> None:
    """
        Find all pdfs within a directory
    """
    for root, dirs, files in os.walk("dir"):
        for file in files:
            if file.endswith(".pdf"):
                full_file_path = os.path.join(root, file)
                print(full_file_path)


def find_even_nums() -> None:
    """
        Find all directories that contain even numbers
    """
    for root, dirs, files in os.walk("dir"):
        for file in files:
            # Even numbers only
            if re.search(r"[13579]", file):
                full_path = os.path.join(root, file)
                print(full_path)


if __name__ == "__main__":
    list_files()
    list_files_with_root()
    find_pdfs()
