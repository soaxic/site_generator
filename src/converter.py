from markdown import *
from blocktype import *
from htmlnode import *
from textnode import *

def markdown_to_html_code(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        blocktype = block_to_blocktype(block)
        nodes.append(block_to_htmlnodes(block, blocktype))
    return ParentNode("div", nodes)

def block_to_htmlnodes(block, blocktype):
    match blocktype:
        case BlockType.PARAGRAPH:
            children = get_children(block)
            return ParentNode("p", children)
        case BlockType.HEADING:
            heading_check = list(block[:6])
            heading_level = 0
            for letter in heading_check:
                if letter == "#":
                    heading_level += 1
                else:
                    break
            children = get_children(block[heading_level+1:])
            return ParentNode(f"h{heading_level}", children)
        case BlockType.CODE:
            return LeafNode("code", block[4:-4])
        case BlockType.QUOTE:
            #TODO - Replace this with a recursive call that sends the lines of the block back through as blocktype.paragraph
            #lines = block.split("\n")
            #children = []
            #for i in range(len(lines)):
            #    lines[i] = lines[i][1:]
            #    children.extend(get_children(lines[i]))
            #for child in children:
            #   child.tag = "p"
            #print(children)
            #return ParentNode("blockquote", children)

def get_children(block):
    textnodes = text_to_textnodes(block)
    children = []
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    return children