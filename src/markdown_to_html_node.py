from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import BlockType, block_to_block_type
from htmlnode import HTMLNode
from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node
from parentnode import ParentNode
from textnode import TextType, TextNode
import string

def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        blocktype = block_to_block_type(block)
        match blocktype:
            case BlockType.PARAGRAPH:
                paragraph = " ".join(block.split("\n"))
                children.append(ParentNode("p", text_to_children(paragraph)))
            case BlockType.HEADING:
                count = 0
                while block[count] == "#":
                    count += 1
                children.append(ParentNode(f"h{count}", text_to_children(block[count + 1:])))
            case BlockType.CODE:
                text_node = TextNode(block[4:-3], TextType.TEXT)
                code_block = ParentNode("code", [text_node_to_html_node(text_node)])
                children.append(ParentNode("pre", [code_block]))
            case BlockType.QUOTE:
                children.append(ParentNode("blockquote", text_to_children(block[1:].strip())))
            case BlockType.ULIST:
                lines = block.split("\n")
                html_nodes = []
                for line in lines:
                    html_nodes.append(ParentNode("li", text_to_children(line[2:])))
                children.append(ParentNode("ul", html_nodes))
            case BlockType.OLIST:
                lines = block.split("\n")
                html_nodes = []
                for line in lines:
                    text = line.split(". ", 1)[1]
                    html_nodes.append(ParentNode("li", text_to_children(text)))
                children.append(ParentNode("ol", html_nodes))
    htmlnode = ParentNode("div", children)
    return htmlnode

def text_to_children(text):
    children = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    return children