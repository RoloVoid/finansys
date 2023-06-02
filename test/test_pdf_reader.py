import os, sys
sys.path.append(os.getcwd()) # pytest需要增加当前工作目录以提取自定义模块

from reader.reader import Reader
from reader.pdf_reader import Pdf_Reader

data_path = './data/sample'
filename = '容百科技招股书.pdf'
test_path = os.path.join(data_path,filename)

class Test_pdf_reader():
    def test_init(self):
        p = Pdf_Reader()
        assert(isinstance(p,Reader))
        assert(isinstance(p,Pdf_Reader))

    def test_read(self):
        p = Pdf_Reader()
        p.read(test_path)

    def test_get_pages(self):
        p = Pdf_Reader()
        p.read(test_path)
        print('\n',p.get_pages())

    def test_read_texts(self):
        p = Pdf_Reader()
        p.read(test_path)
        texts = p.extract_text([78,5,62,542])
        print('\n',texts[0])

    # def test_full_text(self):
    #     p = Pdf_Reader()
    #     p.read(test_path)
    #     f_text = p.full_text_extract()
    #     print('\n',f_text)
