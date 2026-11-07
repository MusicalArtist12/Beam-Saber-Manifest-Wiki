import re
def on_page_markdown(markdown: str, page, **kwargs):
    lst = re.findall(r"(?: )#([A-Za-z1-9_\-]+)", markdown)
    page.meta["tags"] = lst
    return markdown