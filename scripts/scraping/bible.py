import json

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.bible.com/bible'
version_id = '1608'
version_name = 'ARA'
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
book_ids = list(book_chapters.keys())


class Chapter:
    def __init__(self, version_id: str, version_name: str, book_index: int, chapter_index: int):
        self.version_id = version_id
        self.version_name = version_name
        self.book_index = book_index
        self.chapter_index = chapter_index

    @property
    def chapter_number(self) -> int:
        return self.chapter_index + 1

    @property
    def book_id(self) -> str:
        return book_ids[self.book_index]

    def make_url(self) -> str:
        return f'{base_url}/{self.version_id}/{self.book_id}.{self.chapter_number}.{self.version_name}'


class Verse:
    def __init__(self, chapter: Chapter, verse_number: int, verse_text: str):
        self.chapter = chapter
        self.verse_number = verse_number
        self.verse_text = verse_text

    def __dict__(self):
        return {
            'book': self.chapter.book_id,
            'chapter': self.chapter.chapter_number,
            'verse': self.verse_number,
            'text': self.verse_text
        }


def make_chapter_url(version_id: str, version_name: str, book_index: int, chapter_index: int) -> str:
    book = book_ids[book_index]
    chapter = chapter_index + 1
    return f'{base_url}/{version_id}/{book}.{chapter}.{version_name}'


def get_soup_from_chapter_url(chapter_url: str) -> BeautifulSoup:
    response = requests.get(chapter_url)
    return BeautifulSoup(response.text, 'html.parser')


def save_verses_in_json(filename: str, verses: list[Verse]):
    verses_json = json.dumps([verse.__dict__() for verse in verses])
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(verses_json)


all_chapters = [Chapter(version_id, version_name, book_index, chapter_index) for book_index in range(
    len(book_ids)) for chapter_index in range(book_chapters[book_ids[book_index]])]

print(f'{len(all_chapters)} chapters generated')

verses: list[Verse] = []
for chapter in all_chapters:
    chapter_url = chapter.make_url()
    print(f'Getting {chapter_url}')
    soup = get_soup_from_chapter_url(chapter_url)

    for verse_number in range(1, 1000):
        print(f'{chapter.book_id}.{chapter.chapter_number}.{verse_number}')
        verse_span = soup.find(
            'span', attrs={'data-usfm': f'{chapter.book_id}.{chapter.chapter_number}.{verse_number}'})
        if verse_span is None:
            break
        verse_text = ''.join([v.text for v in verse_span.contents[1:]])
        verse = Verse(chapter, verse_number, verse_text)
        print(verse_text)
        verses.append(verse)

save_verses_in_json(f'data/json/{version_name}.json', verses)
