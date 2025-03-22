from markitdown import MarkItDown

md = MarkItDown() # Set to True to enable plugins
result = md.convert("651742440485_.pic.jpg")
print(result.text_content)
