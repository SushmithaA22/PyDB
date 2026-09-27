from pydb.storage.disk import DiskManager
from pydb.storage.page import Page

def test_write_and_read_page(tmp_path):
    database_file=tmp_path/"test.db"
    disk=DiskManager(database_file)
    page=Page()
    data=b"Hello from disk"
    page.write(0,data)
    disk.write_page(0,page)
    loaded_page=disk.read_page(0)
    result=loaded_page.read(0,len(data))
    assert result==data