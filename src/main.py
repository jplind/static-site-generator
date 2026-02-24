from generate_docs import generate_docs
from generate_pages_recursive import generate_pages_recursive
import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_base_path = "/"

def main():
	generate_docs()
	base_path = default_base_path
	if len(sys.argv) > 1:
		base_path = sys.argv[1]
	generate_pages_recursive(base_path, dir_path_content, template_path, dir_path_public)

main()