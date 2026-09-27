from pydb.storage.page import Page
def test_page_write_read():
    page = Page()
    data = b"Hello PyDB"
    page.write(0, data)
    result = page.read(0, len(data))
    assert result == data
