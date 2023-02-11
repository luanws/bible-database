import codecs
import json
import os
from typing import TypedDict

language = input('Language: ')  # Example: en
version_name = input('Version name: ')  # Example: 'ARA'


class VerseDict(TypedDict):
    book: str
    chapter: int
    verse: int
    text: str


def create_directory_if_not_exists(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)


def read_version_json(language: str, version_name: str) -> list[VerseDict]:
    filename = f'data/json/{language}/{version_name}.json'
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_books_from_verse_dict(verse_dict_list: list[VerseDict]) -> list[str]:
    books = []
    for verse_dict in verse_dict_list:
        book = verse_dict['book']
        if book not in books:
            books.append(book)
    return books


def get_chapters_from_book(verse_dict_list: list[VerseDict], book: str) -> list[VerseDict]:
    return [verse_dict for verse_dict in verse_dict_list if verse_dict['book'] == book]


def get_verses_from_chapter(verse_dict_list_book: list[VerseDict], chapter: int) -> list[VerseDict]:
    return [verse_dict for verse_dict in verse_dict_list_book if verse_dict['chapter'] == chapter]


def get_verse_dict(verse_dict_list_chapter: list[VerseDict], verse: int) -> VerseDict:
    return [verse_dict for verse_dict in verse_dict_list_chapter if verse_dict['verse'] == verse][0]


def save_hierarchy_in_json(filename: str, hierarchy_dict: list[list[list[str]]]):
    create_directory_if_not_exists(os.path.dirname(filename))
    hierarchy_json = json.dumps(hierarchy_dict)
    with open(filename, 'w', encoding='utf-8') as f:
        content = codecs.decode(hierarchy_json, 'unicode_escape')
        f.write(content)


hierarchy: list[list[list[str]]] = []
verse_dict_list = read_version_json(language, version_name)
books = get_books_from_verse_dict(verse_dict_list)
for book_index, book in enumerate(books):
    print(book)
    verse_dict_list_book = get_chapters_from_book(verse_dict_list, book)
    chapters = list(set([verse_dict['chapter'] for verse_dict in verse_dict_list_book]))
    hierarchy.append([])
    for chapter in chapters:
        verse_dict_list_chapter = get_verses_from_chapter(verse_dict_list_book, chapter)
        verse_text_list = [verse_dict['text'] for verse_dict in verse_dict_list_chapter]
        hierarchy[book_index].append(verse_text_list)

save_hierarchy_in_json(f'data/custom/json/{language}/{version_name}.json', hierarchy)
