from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        contents_of_markdown = file.read()
    
    with open(template_path, 'r') as file:
        contents_of_template = file.read()
    
    html_node = markdown_to_html_node(contents_of_markdown)
    html = html_node.to_html()

    title_of_markdown = extract_title(contents_of_markdown)

    new_full_page = contents_of_template.replace("{{ Title }}", title_of_markdown)
    new_full_page = new_full_page.replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as file:
        file.write(new_full_page)