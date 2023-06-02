from reader.pdf_reader import Pdf_Reader
from utils.searcher import File_Searcher


p = Pdf_Reader()
p.read('./data/sample/容百科技招股书.pdf')
file = p.extract_text([i for i in range(p.get_pages())])

fs = File_Searcher(file,True)
fs.add_key_word(["增资","转让"])
pages = fs.search_given_file()

print(len(pages))