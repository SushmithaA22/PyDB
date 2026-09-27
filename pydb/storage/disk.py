from pathlib import Path 
from pydb.storage.page import Page,PAGE_SIZE

class DiskManager:
    def __init__(self,filename="pydb.data"):
        self.filename=Path(filename)
        if not self.filename.exists():
            self.filename.touch()

    def write_page(self,page_id,page):
        if page_id<0:
            raise ValueError("page ID can't be -ve")
        if not isinstance(page,Page):
            raise TypeError("page must be a page object")
        with open(self.filename,"r+b") as file:
            offset=page_id*PAGE_SIZE
            file.seek(offset)
            file.write(page.data)

    def read_page(self,page_id):
        if page_id<0:
            raise ValueError("Page ID can't be -ve")
        with open(self.filename,"rb") as file:
            offset=page_id*PAGE_SIZE
            file.seek(offset)
            data=file.read(PAGE_SIZE)
        page=Page()
        if data:
            page.data[:len(data)]=data
        return page

    def page_count(self):
        file_size=self.filename.stat().st_size
        return file_size