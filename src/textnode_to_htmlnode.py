from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case (TextType.TEXT):
            return LeafNode(None, text_node.text)
        case (TextType.BOLD):
            return LeafNode("b", text_node.text)
        case (TextType.ITALIC):
            return LeafNode("i", text_node.text)
        case (TextType.CODE):
            return LeafNode('code', text_node.text)
        case (TextType.LINKS):
            return LeafNode('a', text_node.text, {'href': text_node.url})
        case (TextType.IMAGES):
            return LeafNode('img', text_node.text, {'src': text_node.url})
        case _:
            raise Exception('no valid TextType found')

