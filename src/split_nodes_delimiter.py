from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, delimited_text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        sections = old_node.text.split(delimiter)
        split_nodes = []
        if len(sections) % 2 == 0:
            raise ValueError('Invalid markdown, markdown section')
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], delimited_text_type))
        new_nodes.extend(split_nodes)
    return new_nodes