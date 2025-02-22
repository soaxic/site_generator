import os
from converter import *
from markdown import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    source_file = get_file_contents(from_path)
    template_file = get_file_contents(template_path)
    html = markdown_to_html_code(source_file).to_html()
    title = extract_title(source_file)
    template_file = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html)
    if not os.path.exists(os.path.dirname(dest_path)):
        print(f"Creating {os.path.dirname(dest_path)}")
        os.makedirs(os.path.dirname(dest_path))
    write_file(template_file, dest_path)
    
def get_file_contents(path):
    with open(path) as file:
        return file.read()
    
def write_file(content, dest):
    with open(dest, "w") as file:
        file.write(content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dirs = list(map(lambda x: os.path.join(dir_path_content, x), os.listdir(dir_path_content)))
    for dir in dirs:
        dest = dir.replace(dir_path_content, dest_dir_path)
        if os.path.isdir(dir):
            generate_pages_recursive(dir, template_path, dest)
        else:
            generate_page(dir, template_path, dest.replace(".md", ".html"))