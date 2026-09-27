PAGE_SIZE = 4096

class Page:
    def __init__(self):
        self.data = bytearray(PAGE_SIZE)

    def write(self, offset, data):
        if offset<0:
            raise ValueError("offset can't be negative")
        end = offset + len(data)
        if end>PAGE_SIZE:
            raise ValueError("Data exceeds page size")
        self.data[offset:end]=data

        if end > PAGE_SIZE:
            raise ValueError("Data exceeds page size")

        self.data[offset:end] = data

    def read(self, offset, size):
        if offset<0 or size<0:
            raise ValueError("offset can't be -ve")
        if offset+size>PAGE_SIZE:
            raise ValueError("read exceeds page size")
        return bytes(self.data[offset:offset + size])
