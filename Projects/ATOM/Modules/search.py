from ddgs import DDGS

def web_search(cmd):
    with DDGS() as d:
        res = [r["body"] for r in d.text(cmd, max_results=3)]
    return "\n".join(res)
