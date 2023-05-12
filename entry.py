class Entry:
    def __init__(self):
        self.quotes = ""
        self.author = ""
        self.location = ""
    
    def get_quotes(self):
        return self.quotes
    def set_quotes(self, quotes):
        self.quotes = quotes
    
    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author
    
    def get_location(self):
        return self.location
    def set_location(self, location):
        self.location = location
    
    def __str__(self):
        return self.quotes + self.author + self.location