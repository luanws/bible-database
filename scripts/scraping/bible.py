import codecs
import json
import os
import re
from itertools import count

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.bible.com/bible'
versions_url = 'https://www.bible.com/versions'
language = input('Language: ')  # Example: en
version_name = input('Version name: ')  # Example: 'ARA'
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
    def __init__(self, version_id: str, version_name: str, book_index: int, chapter_index: int, book_id: str):
        self.version_id = version_id
        self.version_name = version_name
        self.book_index = book_index
        self.chapter_index = chapter_index
        self.book_id = book_id

    @property
    def chapter_number(self) -> int:
        return self.chapter_index + 1


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


def get_book_id_from_chapter(chapter: Chapter) -> str:
    return book_ids[chapter.book_index]


def make_chapter_url(chapter: Chapter) -> str:
    book_id = get_book_id_from_chapter(chapter)
    return f'{base_url}/{chapter.version_id}/{book_id}.{chapter.chapter_number}.{chapter.version_name}'


def get_soup_from_chapter_url(chapter_url: str) -> BeautifulSoup:
    response = requests.get(chapter_url)
    return BeautifulSoup(response.text, 'html.parser')


def create_directory_if_not_exists(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_verses_in_json(filename: str, verses: list[Verse]):
    create_directory_if_not_exists(os.path.dirname(filename))
    verses_json = json.dumps([verse.__dict__() for verse in verses])
    with open(filename, 'w', encoding='utf-8') as f:
        content = codecs.decode(verses_json, 'unicode_escape')
        f.write(content)


def get_all_chapters(book_ids: list[str], book_chapters: dict[str, int], version_id: str, version_name: str) -> list[Chapter]:
    return [Chapter(
        version_id=version_id,
        version_name=version_name,
        book_index=book_index,
        chapter_index=chapter_index,
        book_id=book_ids[book_index]
    ) for book_index in range(len(book_ids)) for chapter_index in range(book_chapters[book_ids[book_index]])]


def scrape_version_id(versions_url: str, version_name: str) -> str:
    response = requests.get(versions_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    version_a = soup.find('a', text=re.compile(f'\\({version_name}\\)'))
    href = version_a['href']
    search = re.search(r'/versions/(\d+)-', href)
    if not isinstance(search, re.Match):
        raise Exception('Version not found')
    version_id: str = search.group(1)
    return version_id


try:
    version_id = scrape_version_id(versions_url, version_name)
except Exception as e:
    print(f'Version {version_name} not found. Please insert the version ID manually.')
    version_id = input('Version ID: ')

print(f'Version ID: {version_id}')
all_chapters = get_all_chapters(book_ids, book_chapters, version_id, version_name)
print(f'{len(all_chapters)} chapters generated')

verses: list[Verse] = []
for chapter in all_chapters:
    chapter_url = make_chapter_url(chapter)
    print(f'Getting {chapter_url}')
    soup = get_soup_from_chapter_url(chapter_url)

    for verse_number in count(1):
        print(f'{chapter.book_id}.{chapter.chapter_number}.{verse_number}')
        verse_span = soup.find(
            'span', attrs={'data-usfm': f'{chapter.book_id}.{chapter.chapter_number}.{verse_number}'})
        if verse_span is None:
            break
        content_verse_spans = verse_span.find_all('span', attrs={'class': 'content'})
        verse_text = ''.join([v.text for v in content_verse_spans])
        verse = Verse(chapter, verse_number, verse_text)
        print(verse_text)
        verses.append(verse)

save_verses_in_json(f'data/json/{language}/{version_name}.json', verses)
