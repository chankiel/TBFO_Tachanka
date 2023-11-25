from bs4 import BeautifulSoup

def html_to_array(html_string):
    # Parse the HTML string
    soup = BeautifulSoup(html_string, 'html.parser')

    # Function to recursively extract tags and text content
    def extract_tags_and_text(element):
        result = []
        if hasattr(element, 'contents'):
            for content in element.contents:
                if isinstance(content, str):
                    result.append(content)
                elif hasattr(content, 'name'):
                    result.append(f"<{content.name}>")
                    result.extend(extract_tags_and_text(content))
                    result.append(f"</{content.name}>")
        return result

    # Start extracting from the root HTML element
    result_array = extract_tags_and_text(soup)

    return result_array

# Input HTML string
html_string = "<html                           ><head><title>Simple Web</title></head><body><h1 id=\"judul\">Hello, World!</h1> <p id = \"\">This is a simple webpage.</p></body></html>"
 
# Get the result array
result_array = html_to_array(html_string)

# Print the result
print(result_array)
