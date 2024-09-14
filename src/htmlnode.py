from types import NotImplementedType


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(f' {key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children, props):
        super().__init__(tag=tag, value=value, children=children,props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return f"{self.value}"
        props_str = ' '.join([f'{key}="{value}"' for key, value in self.props.items()] if self.props else '')        
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
