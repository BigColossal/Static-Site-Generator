from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node
from htmlnode import ParentNode, LeafNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    div = ParentNode('div', [])
    for block in blocks:
        extracted_parent_node, block_type = create_corresponding_parent_node(block)
        if block_type == "code":
            lines = block
        else:
            lines = block.split("\n")
        leaf_nodes = create_corresponding_leaf_nodes(lines, block_type)
        organize_leaf_nodes_into_parent(leaf_nodes, extracted_parent_node, block_type)
        div.children.append(extracted_parent_node)
    return div
        
def create_corresponding_parent_node(block):
    block_type = block_to_block_type(block)
    if block_type.value == "heading":
        corresponding_tag = produce_heading_tag(block)
        return ParentNode(corresponding_tag, []), block_type.value
    elif block_type.value == "code":
        return ParentNode("pre", [ParentNode("code", [])]), block_type.value
    elif block_type.value == "normal":
        return ParentNode("p", []), block_type.value
    elif block_type.value == "quote":
        return ParentNode("blockquote", []), block_type.value
    elif block_type.value == "unordered":
        return ParentNode("ul", produce_list_parent_nodes(block)), block_type.value
    elif block_type.value == "ordered":
        return ParentNode("ol", produce_list_parent_nodes(block)), block_type.value
    
def produce_heading_tag(block):
    i = 0
    while True:
        if block[i] == "#":
            i += 1
        else:
            return f"h{i}"
        
def produce_list_parent_nodes(block):
    lines = block.split("\n")
    final_nodes = [ParentNode("li", []) for line in lines]
    return final_nodes

def create_corresponding_leaf_nodes(lines, block_type):
    if block_type == "code":
        lines = clean_line(lines, block_type)
        return LeafNode(None, lines)
    leaf_nodes = []
    if block_type == "normal":
        lines = [" ".join(lines),]
    already_cleaned = False
    for line in lines:
        line, already_cleaned = clean_line(line, block_type, already_cleaned)
        text_nodes_created = text_to_textnodes(line)
        leaf_nodes_in_line = []
        for text_node in text_nodes_created:
            leaf_node = text_node_to_html_node(text_node)
            leaf_nodes_in_line.append(leaf_node)
        leaf_nodes.append(leaf_nodes_in_line)
    return leaf_nodes


def clean_line(line, block_type, already_cleaned):
    if block_type == "normal":
        return line, already_cleaned
    elif block_type == "heading":
        line = line.lstrip("#")
        return line.lstrip(), already_cleaned
    elif block_type == "quote":
        line = line[1:]
        if already_cleaned:
            return line, already_cleaned
        else:
            already_cleaned = True
            return line.lstrip(), already_cleaned
    elif block_type == "unordered":
        return line [2:], already_cleaned
    elif block_type == "ordered":
        return line[3:], already_cleaned
    elif block_type == "code":
        return line[3:-3], already_cleaned

def organize_leaf_nodes_into_parent(leaf_nodes, parent_node, block_type):
    if block_type == "code":
        parent_node.children[0].children.append(leaf_nodes)
        return
    i = 0
    for line in leaf_nodes:
        for leaf_node in line:
            if block_type == "unordered" or block_type == "ordered":
                parent_node.children[i].children.append(leaf_node)
                continue
            parent_node.children.append(leaf_node)

        i += 1