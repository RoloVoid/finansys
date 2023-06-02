# A tool used to search keyword in a given list of str

from flashtext import KeywordProcessor

class File_Searcher():
    def __init__(self,file,case_sensitive=False):
        self.file = file
        self.searcher = KeywordProcessor(case_sensitive=case_sensitive)
    
    def add_key_word(self,keywords:list):
        self.searcher.add_keywords_from_list(keywords)

    # assume file is a str list, like task1
    def search_given_file(self) -> list :
        if not isinstance(self.file,list): return ["wrong"]
        result = []
        for page in self.file:
            if self.searcher.extract_keywords(page): 
                result.append(page)
        
        return result
                