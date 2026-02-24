from generate_docs import generate_docs
from generate_pages_recursive import generate_pages_recursive
import sys

def main():
	generate_docs()
	base_path = "/"
	if len(sys.argv) > 1:
		base_path = sys.argv[1]
	generate_pages_recursive(base_path, "content", "template.html", "docs")

main()