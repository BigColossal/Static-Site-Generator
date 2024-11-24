from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os
import shutil
from pathlib import Path

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

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        full_path = os.path.join(dir_path_content, file)
        if file.endswith('.md'):
            # remove the .md and add .html
            file_without_ext = file[:-3]  # removes last 3 characters ('.md')
            new_file = file_without_ext + '.html'
            complete_dest_path = os.path.join(dest_dir_path, new_file)
        else:
            complete_dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(full_path) or os.path.islink(full_path):
            if file.endswith('.md'):
                generate_page(full_path, template_path, complete_dest_path)
        elif os.path.isdir(full_path):
            os.makedirs(complete_dest_path, exist_ok=True)
            generate_page_recursive(full_path, template_path, complete_dest_path)


generate_page_recursive("content/", "template.html", "public/")