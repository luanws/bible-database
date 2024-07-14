import json
import os
from typing import Any

from src.utils.files import walk_directory


def get_data_file_paths() -> list[list[str]]:
    files = walk_directory("data")
    files = [file.split(os.sep)[1:] for file in files]
    files = [file for file in files if file[0] != "custom" and len(file) > 1]
    return files


def add_available_version(
    file_name: str,
    directories: list[str],
    available_versions: dict,
):
    directory = directories[0]
    if len(directories) == 1:
        file_name_without_extension = os.path.splitext(file_name)[0]
        available_versions_list = available_versions.get(directory) or []
        available_versions_list.append(file_name_without_extension)
        available_versions[directory] = available_versions_list
    else:
        if available_versions.get(directory) is None:
            available_versions[directory] = {}
        add_available_version(file_name, directories[1:], available_versions[directory])


def get_available_versions(file_paths: list[list[str]]) -> dict:
    available_versions = {}
    for file in file_paths:
        file_name = file[-1]
        directories = file[:-1]
        add_available_version(file_name, directories, available_versions)
    return available_versions


def save_json(data: dict[str, Any]):
    with open("data/available_versions.json", "w") as f:
        content = json.dumps(data, indent=4)
        f.write(content)


if __name__ == "__main__":
    file_paths = get_data_file_paths()
    available_versions = get_available_versions(file_paths)
    save_json(available_versions)
