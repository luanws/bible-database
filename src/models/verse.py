from src.models.chapter import Chapter


class Verse:
    def __init__(self, chapter: Chapter, verse_number: int, verse_text: str):
        self.chapter = chapter
        self.verse_number = verse_number
        self.verse_text = verse_text

    def __dict__(self):
        return {
            "book": self.chapter.book_id,
            "chapter": self.chapter.chapter_number,
            "verse": self.verse_number,
            "text": self.verse_text,
        }