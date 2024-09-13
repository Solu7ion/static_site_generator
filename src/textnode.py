class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text 
        self.text_type = text_type
        self.url = url 

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (self.text == other.text and 
                    self.text_type == other.text_type and 
                    self.url == other.url)
        return False

    def __repr__(self):
        TEXT = self.text 
        TEXT_TYPE = self.text_type
        URL = self.url 
        return TextNode(TEXT, TEXT_TYPE, URL)
