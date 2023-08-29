from src.service.file.FileParse import FileParse

import fitz


# pdf 解析类
class PDFParser(FileParse):
    def __init__(self, file_path):
        self.file_path = file_path
        self.doc = None

    def load_file(self):
        self.doc = fitz.open(self.file_path)

    def extract_text(self):
        text = ""
        for page in self.doc:
            text += page.get_text()
            text += "------ " + str(page.number+1) + " --------\n"
        return text
