def extract_title(markdown):
    if markdown[0] == "#":
        new_markdown = markdown.lstrip("#")
        new_markdown = new_markdown.strip()
        return new_markdown
    else:
        raise Exception("no title found")