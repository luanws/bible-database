class Chapter:
    def __init__(
        self,
        version_id: str,
        version_name: str,
        book_index: int,
        chapter_index: int,
        book_id: str,
    ):
        self.version_id = version_id
        self.version_name = version_name
        self.book_index = book_index
        self.chapter_index = chapter_index
        self.book_id = book_id

    @property
    def chapter_number(self) -> int:
        return self.chapter_index + 1
