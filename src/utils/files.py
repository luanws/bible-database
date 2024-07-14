import os


def create_directory_if_not_exists(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)


def walk_directory(directory: str) -> list[str]:
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files
