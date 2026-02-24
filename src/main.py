from generate_public import generate_public
from generate_pages_recursive import generate_pages_recursive

def main():
	generate_public()
	generate_pages_recursive("content", "template.html", "public")

main()