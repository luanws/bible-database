import json
import os
from typing import TypedDict

from termcolor import colored

language = input('Language: ')  # Example: en

book_chapters = {
    'GEN': 50, 'EXO': 40, 'LEV': 27, 'NUM': 36, 'DEU': 34, 'JOS': 24,
    'JDG': 21, 'RUT': 4, '1SA': 31, '2SA': 24, '1KI': 22, '2KI': 25,
    '1CH': 29, '2CH': 36, 'EZR': 10, 'NEH': 13, 'EST': 10, 'JOB': 42,
    'PSA': 150, 'PRO': 31, 'ECC': 12, 'SNG': 8, 'ISA': 66, 'JER': 52,
    'LAM': 5, 'EZK': 48, 'DAN': 12, 'HOS': 14, 'JOL': 3, 'AMO': 9,
    'OBA': 1, 'JON': 4, 'MIC': 7, 'NAM': 3, 'HAB': 3, 'ZEP': 3,
    'HAG': 2, 'ZEC': 14, 'MAL': 4, 'MAT': 28, 'MRK': 16, 'LUK': 24,
    'JHN': 21, 'ACT': 28, 'ROM': 16, '1CO': 16, '2CO': 13, 'GAL': 6,
    'EPH': 6, 'PHP': 4, 'COL': 4, '1TH': 5, '2TH': 3, '1TI': 6,
    '2TI': 4, 'TIT': 3, 'PHM': 1, 'HEB': 13, 'JAS': 5, '1PE': 5,
    '2PE': 3, '1JN': 5, '2JN': 1, '3JN': 1, 'JUD': 1, 'REV': 22
}

number_of_verses_from_version = {
    'A21': 31104,
    'ARA': 31104,  # ok
    'ARC': 31105,  # ok
    'BLT': 7959,
    'NAA': 31105,
    'NBV-P': 31105,
    'NTLH': 31103,  # ok
    'NVI': 31103,
    'NVT': 31104,
    'TB': 31102,
    'VFL': 31102,
}


class Verse(TypedDict):
    book: str
    chapter: int
    verse: int
    text: str


def get_all_versions_from_language(language: str) -> list[str]:
    versions = []
    for file in os.listdir(f'data/json/{language}'):
        if file.endswith('.json'):
            versions.append(file[:-5])
    return versions


def get_verses_from_json(file_path: str) -> list[Verse]:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def check_number_of_verses(verses: list[Verse], version_name: str):
    verse_count = len(verses)
    correct_verse_count = number_of_verses_from_version[version_name]
    if verse_count == number_of_verses_from_version[version_name]:
        version_name_colored = colored(version_name, "cyan")
        verse_count_colored = colored(str(verse_count), "green")
        print(f'{version_name_colored} has {verse_count_colored} verses')
    else:
        version_name_colored = colored(version_name, "cyan")
        verse_count_colored = colored(str(verse_count), "red")
        correct_verse_count_colored = colored(str(correct_verse_count), "red")
        print(f'{version_name_colored} has {verse_count_colored} verses, but should be {correct_verse_count_colored}')


for version_name in get_all_versions_from_language(language):
    source_file_path = f'data/json/{language}/{version_name}.json'
    verses: list[Verse] = get_verses_from_json(source_file_path)
    check_number_of_verses(verses, version_name)
