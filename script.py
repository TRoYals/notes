import os
import re

def process_ad_blocks(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    ad_pattern = re.compile(r"```ad-(\w+)\n([\s\S]*?)\n```")
    content = ad_pattern.sub(lambda m: f"::: {m.group(1)}\n{m.group(2)}\n:::", content)
    with open(file_path, "w") as f:
        f.write(content)

def process_links(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    link_pattern = re.compile(r"\[\[(([^\]#]+)(#(.+?))?)(\|(.+?))?\]\]")

    def replace_link(match):
        full_link = match.group(2)
        anchor = match.group(4)
        title = match.group(6)

        if anchor:
            return f"[{title or anchor}]({full_link.replace(' ', '%20')}.md#{anchor})"
        else:
            return f"[{title or full_link}]({full_link.replace(' ', '%20')}.md)"

    content = link_pattern.sub(replace_link, content)

    with open(file_path, "w") as f:
        f.write(content)

def remove_tags(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    card_pattern = re.compile(r"#card")
    content = card_pattern.sub("", content)
    caret_pattern = re.compile(r"\^[\w]+")
    content = caret_pattern.sub("", content)
    with open(file_path, "w") as f:
        f.write(content)

for root, dirs, files in os.walk("static_resources"):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            process_ad_blocks(file_path)
            process_links(file_path)
            remove_tags(file_path)
