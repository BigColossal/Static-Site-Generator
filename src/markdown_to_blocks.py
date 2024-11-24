from enum import Enum

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    final_blocks = []
    for block in blocks:
        block = block.strip()
        if len(block) == 0:
            continue
        final_blocks.append(block)
    return final_blocks

class BlockType(Enum):
    HEADING = "heading" # Begins with 1-6 hashtags(#), then followed by a space
    CODE = "code" # Starts and ends in 3 backticks (```)
    QUOTE = "quote" # Starts with a greater than symbol (>)
    UNORDERED = "unordered" # Starts with either an asterisk or dash(* or -), then following by a space
    ORDERED = "ordered" # Must start with a number followed by a "." character and a space. Must also start at 1 and increment by 1
    NORMAL = "normal"

    def __str__(self):
        return self.value

def block_to_block_type(block):
    if block[0] == '#': # checking for heading block
        i = 1
        while True:
            if block[i] == " ":
                return BlockType.HEADING
            elif block[i] == "#":
                i += 1
            else:
                return BlockType.NORMAL # if no space is found, simply return that the block is normal
            
    elif block[:3] == "```": # checking for code block
        if block[-3:] == "```": # check if it ends with the three backticks as well
            return BlockType.CODE
        else:
            return BlockType.NORMAL # otherwise, set it to normal
        
    elif block[0] == ">": # checking for quotes block
        quote_lines = block.split("\n")
        for line in quote_lines:
            if line[0] == ">":
                continue
            else:
                return BlockType.NORMAL
        return BlockType.QUOTE
    
    elif block[0] == "-" or block[0] == "*": # checking for unordered list block
        unordered_list_lines = block.split("\n")
        for line in unordered_list_lines:
            if (line[0] == "-" or line[0] == "*") and line[1] == " ":
                continue
            else:
                return BlockType.NORMAL
        return BlockType.UNORDERED
    
    elif block[:3] == "1. ": # checking for ordered block
        ordered_list_lines = block.split("\n")
        i = 1
        for line in ordered_list_lines:
            if line[:3] == f"{i}. ":
                i += 1
                continue
            else:
                return BlockType.NORMAL
        return BlockType.ORDERED
    
    else: # if nothing else
        return BlockType.NORMAL
            
