class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        html = "<" + self.tag + ">"
        if self.children:
            for child in self.children:
                html += child.to_html()
        html += "</" + self.tag + ">"
        return html

    
    def props_to_html(self):
        if self.props == None or len(self.props) == 0:
            return ""
        result = ""
        for key, value in self.props.items():
            result += " " + key + "=\"" + value +"\""
        return result
    
    def __repr__(self):
        result = "HTMLNode("
        result += str(self.tag) + ", "
        result += str(self.value) + ", "
        result += str(self.children) + ", "
        result += str(self.props) + ")"
        return result