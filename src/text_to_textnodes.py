from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_images_links import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):

    nodes = [TextNode(text, TextType.TEXT)]

    bold_nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)

    italic_nodes = split_nodes_delimiter(bold_nodes, '*', TextType.ITALIC)

    code_nodes = split_nodes_delimiter(italic_nodes, '`', TextType.CODE)

    image_nodes = split_nodes_image(code_nodes)

    final_nodes = split_nodes_link(image_nodes)
    return final_nodes

final_nodes = text_to_textnodes('This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)')