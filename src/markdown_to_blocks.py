def markdown_to_blocks(markdown):
    blocks = []
    sections = markdown.split("\n\n")
    for s in sections:
        s = s.strip()
        if s != "":
            blocks.append(s)
    return blocks