import re

def extract_text(content: str):
    pattern = r'NEW "(.*?)"'
    return re.findall(pattern, content)

def replace_text(content: str, translated: list):
    for t in translated:
        content = content.replace('NEW ""', f'NEW "{t}"', 1)
    return content