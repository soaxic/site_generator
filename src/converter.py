from markdown import *
from blocktype import *
from htmlnode import *
from textnode import *

def markdown_to_html_code(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        blocktype = block_to_blocktype(block)
        nodes.extend(block_to_htmlnodes(block, blocktype))
    return ParentNode("div", nodes)

def block_to_htmlnodes(block, blocktype):
    match blocktype:
        case BlockType.PARAGRAPH:
            #This should split by line break and wrap each section in p
            children = unwrap_paragraph(block)
            return children
        case BlockType.HEADING:
            heading_level = 0
            for letter in block[:6]:
                if letter == "#":
                    heading_level += 1
                else:
                    break
            children = get_children(block[heading_level+1:])
            return [ParentNode(f"h{heading_level}", children)]
        case BlockType.CODE:
            children = get_code_children(block[4:-4])
            return [ParentNode("pre", children)]
        case BlockType.QUOTE:
            lines = block.split("\n")
            children = []
            for i in range(len(lines)):
                lines[i] = lines[i][1:]
                children.extend(get_children(lines[i][1:]))
                #children.extend(block_to_htmlnodes(lines[i], BlockType.PARAGRAPH))
            return [ParentNode("blockquote", children)]
        case BlockType.UNORDERED_LIST:
            children = get_unordered_list_children(block)
            return [ParentNode("ul", children)]
        case BlockType.ORDERED_LIST:
            children = get_ordered_list_children(block)
            return [ParentNode("ol", children)]
        
def unwrap_paragraph(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        textnodes = []
        textnodes.extend(text_to_textnodes(line))
        htmlnodes = []
        for node in textnodes:
            htmlnodes.append(text_node_to_html_node(node))
        children.append(ParentNode("p", htmlnodes))
    return children

def get_children(block):
    textnodes = text_to_textnodes(block)
    children = []
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    return children

def get_unordered_list_children(lines):
    lines = lines.split("\n")
    children = []
    for li in lines:
        textnodes = []
        textnodes.extend(text_to_textnodes(li[2:]))
        htmlnodes = []
        for node in textnodes:
            htmlnodes.append(text_node_to_html_node(node))
        children.append(ParentNode("li", htmlnodes))
    return children

def get_ordered_list_children(lines):
    lines = lines.split("\n")
    children = []
    for i, li in enumerate(lines, 1):
        prefix_length = len(str(i)) + 2
        textnodes = []
        textnodes.extend(text_to_textnodes(li[prefix_length:]))
        htmlnodes = []
        for node in textnodes:
            htmlnodes.append(text_node_to_html_node(node))
        children.append(ParentNode("li", htmlnodes))
    return children

def get_code_children(lines):
    lines = lines.split("\n")
    children = []
    for li in lines:
        textnodes = []
        textnodes.extend(text_to_textnodes(li))
        htmlnodes = []
        for node in textnodes:
            htmlnodes.append(text_node_to_html_node(node))
        children.append(ParentNode("code", htmlnodes))
    return children