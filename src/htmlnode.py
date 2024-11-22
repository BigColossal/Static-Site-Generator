class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            return " ".join(f'{key}="{value}"' for key, value in self.props.items())
        else:
            return ""
        
    def __repr__(self):
        return f'HTMLNode(tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props})'

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (self.tag == other.tag and
                    self.value == other.value and
                    self.children == other.children and
                    self.props == other.props)
        return False
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("no value found")
        if not self.tag:
            return self.value
        html_props = self.props_to_html()
        if self.props:
            prop_space = " "
        else:
            prop_space = ""

        return f"<{self.tag}{prop_space}{html_props}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f'LeafNode(tag = {self.tag}, value = {self.value}, props = {self.props})'
    
    def __eq__(self, other):
        if isinstance(other, LeafNode):
            return (self.tag == other.tag and
                    self.value == other.value and
                    self.props == other.props)
        return False
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError('no tags detected')
        if not self.children:
            raise ValueError('no children detected')
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
