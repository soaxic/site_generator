import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_node = node.text.split(delimiter)
            if len(split_node) % 2 == 0:
                raise SyntaxError("Closing delimiter not found")
            count = 0
            for split in split_node:
                if split == "":
                    count += 1
                    continue
                elif count % 2 == 0:
                    new_nodes.append(TextNode(split, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split, text_type))
                count += 1
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[.*?\]\(.*?\)", text)
    tupled_images = []
    for image in images:
        tupled_images.append(
            (
                "".join(re.findall(r"\[(.*?)\]", image)),
                "".join(re.findall(r"\((.*?)\)", image)),
            )
        )
    return tupled_images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[.*?\]\(.*?\)", text)
    tupled_links = []
    for link in links:
        tupled_links.append(
            (
                "".join(re.findall(r"\[(.*?)\]", link)),
                "".join(re.findall(r"\((.*?)\)", link)),
            )
        )
    return tupled_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        working_section = old_node.text
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            images = extract_markdown_images(working_section)
            for image in images:
                alt_text = image[0]
                image_link = image[1]
                split_node = working_section.split(f"![{alt_text}]({image_link})", 1)
                if split_node[0] != "":
                    new_nodes.append(TextNode(split_node[0], TextType.TEXT))
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_link))
                working_section = split_node[1]
            if working_section != "":
                    new_nodes.append(TextNode(working_section, TextType.TEXT))
    return new_nodes