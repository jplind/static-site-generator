from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links
import string

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_strings = node.text.split(delimiter)
        if len(split_strings) == 1:
            new_nodes.append(node)
            continue
        if len(split_strings) < 3 or len(split_strings) % 2 == 0:
            raise Exception("invalid markdown syntax")
        for i, s in enumerate(split_strings):
            if i % 2 == 0:
                new_nodes.append(TextNode(s, TextType.TEXT))
            else:
                new_nodes.append(TextNode(s, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for (image, url) in images:
            sections = text.split(f"![{image}]({url})", 1)
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image, TextType.IMAGE, url))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for (link, url) in links:
            sections = text.split(f"[{link}]({url})", 1)
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link, TextType.LINK, url))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes
        