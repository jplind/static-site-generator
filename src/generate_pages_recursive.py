import os
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node

def generate_pages_recursive(base_path, content_dir_path, template_path, destination_dir_path):
    for item in os.listdir(content_dir_path):
        content_path = os.path.join(content_dir_path, item)
        destination_path = os.path.join(destination_dir_path, item)
        if os.path.isfile(content_path) and content_path.endswith(".md"):
            generate_page(base_path, content_path, template_path, destination_path[:-2] + "html")
        else:
            os.mkdir(destination_path)
            generate_pages_recursive(base_path, content_path, template_path, destination_path)

def generate_page(base_path, md_path, template_path, html_path):
    with open(md_path) as f:
        md = f.read()
    
    with open(template_path) as f:
        template = f.read()
    
    title = extract_title(md)
    content = markdown_to_html_node(md).to_html()
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    page = page.replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')
    with open(html_path, "w") as f:
        f.write(page)