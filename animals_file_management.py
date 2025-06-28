SOURCE_PATH = "animals_template.html"
DESTINATION_PATH = "animals.html"

def read_html_template():
    with open(SOURCE_PATH, 'r') as handle:
        return handle.read()

def write_html_content(content):
    with open(DESTINATION_PATH, 'w') as handle:
        handle.write(content)