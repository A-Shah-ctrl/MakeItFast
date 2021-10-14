import pdfplumber

class Extractor:
    def __init__(self, path:str):
        self.text = self._get_text(path)

    def _get_text(self, path:str):
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += str(page.extract_text())

        return text

    def get_text(self):
        return self.text

