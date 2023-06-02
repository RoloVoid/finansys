import os

from reader.reader import Reader
from PyPDF2 import PdfReader

class Pdf_Reader(Reader):
    def __init__(self,type='pdf'):
        super(Pdf_Reader,self).__init__(type)
        assert(self.type=='pdf')

    def read(self,file):
        if not os.path.exists(file):
            print("not exist")
            return 
        self.file = PdfReader(file)

    def get_pages(self) -> int:
        return len(self.file.pages)
    
    def extract_text(self,indexs: list,visitor=None) -> list:
        l = self.get_pages()
        results = []
        for i in indexs:
            if i < 0 or i >= l: 
                # print("\nThe page %d is out of border: [0,%d)\n" % (i,l))
                print(f"\nthe page {i} is out of border: [0,{l}) \n")
                continue
            if visitor:
                results.append(self.file.pages[i].extract_text(0,90,visitor_text=visitor))
            else: 
                results.append(self.file.pages[i].extract_text(0,90))

        return results
    
    
    # A visitor is used to restrict the area we need to extract texts
    # see https://pypdf2.readthedocs.io/en/3.0.0/user/extract-text.html#using-a-visitor

    # 非常慢，不要轻易使用，以使用分页为主
    def full_text_extract(self,visitor=None) -> str:
        l = self.get_pages()
        result = self.extract_text([ i for i in range(l)],visitor=visitor)
        return ' '.join(result)
    