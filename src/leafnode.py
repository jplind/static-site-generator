from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def __repr__(self):
        result = "LeafNode("
        result += str(self.tag) + ", "
        result += str(self.value) + ", "
        result += str(self.props) + ")"
        return result
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        html = "<" + self.tag
        html += self.props_to_html() + ">" + self.value + "</" + self.tag + ">"
        return html
                
        