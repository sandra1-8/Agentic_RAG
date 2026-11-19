"""
Agent 1: Section Decomposition
Input : Markdown produced by Docling (one tender/legal document)
Output: one .md file per section + hierarchy.json + sections_metadata.json

Usage:
    python section_agent.py input.md --out output_dir
"""
import re, json, argparse
from pathlib import Path

HASH_HEAD = re.compile(r'^(#{1,6})\s+(.*\S)\s*$')
NUM_HEAD  = re.compile(r'^(\d+(?:\.\d+)*)\.?\s+(.+?)\s*$')
PLAIN_NUM = re.compile(r'^(\d+(?:\.\d+)+)\.?\s+([A-Z].{0,100}[^.\s])\s*$')  # e.g. "4.2.1 Authentication"


def parse_heading(line):
    """Return (level, number_or_None, title) or None if line is not a heading."""
    m = HASH_HEAD.match(line)
    if m:
        text = m.group(2)
        n = NUM_HEAD.match(text)
        if n:  # numbered heading: depth comes from the number, NOT from '#'
            num = n.group(1)
            return num.count('.') + 1, num, n.group(2)
        return -len(m.group(1)), None, text   # negative = unnumbered, value = -(# count)
    p = PLAIN_NUM.match(line)  # numbered line without '#'
    if p:
        return p.group(1).count('.') + 1, p.group(1), p.group(2)
    return None


def base_hash_depth(md_text):
    """Which '#' count do top-level numbered headings (e.g. '1 Intro') use in this file?"""
    from collections import Counter
    c = Counter()
    for line in md_text.splitlines():
        m = HASH_HEAD.match(line)
        if m:
            n = NUM_HEAD.match(m.group(2))
            if n and "." not in n.group(1):
                c[len(m.group(1))] += 1
    return c.most_common(1)[0][0] if c else 2


def decompose(md_text):
    base = base_hash_depth(md_text)
    sections, stack = [], []          # stack of (level, section_id)
    cur = {"id": "0", "title": "Preamble", "level": 0, "number": None,
           "parent": None, "lines": []}
    unnumbered = 0
    in_code = False
    last_real = 0          # level of the last non-label heading

    def close():
        text = "\n".join(cur["lines"]).strip()
        if text or cur["id"] != "0":
            sections.append({**{k: cur[k] for k in ("id", "title", "level", "number", "parent")},
                             "content": text})

    for line in md_text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
        h = None if in_code else parse_heading(line)
        if not h:
            cur["lines"].append(line)
            continue
        close()
        level, num, title = h
        if level < 0:                      # unnumbered heading
            hashes = -level
            if title.rstrip().endswith("."):     # label-like ("Specific objectives.") -> child of last real heading
                level = last_real + 1
            elif hashes > base:            # deeper than top-level sections -> sub-heading
                level = last_real + 1
            else:                          # same depth as numbered sections -> top-level sibling
                level = 1
            is_label = title.rstrip().endswith(".")
        else:
            is_label = False
        if not is_label:
            last_real = level
        if num:
            sid = num
        else:
            unnumbered += 1
            sid = f"u{unnumbered}"
        while stack and stack[-1][0] >= level:
            stack.pop()
        parent = stack[-1][1] if stack else None
        stack.append((level, sid))
        cur = {"id": sid, "title": title, "level": level, "number": num,
               "parent": parent, "lines": []}
    close()
    return sections


def add_paths(sections):
    by_id = {s["id"]: s for s in sections}
    for s in sections:
        path, node = [], s
        while node:
            path.append(f'{node["id"]} {node["title"]}' if node["number"] else node["title"])
            node = by_id.get(node["parent"])
        s["path"] = " > ".join(reversed(path))
    return sections


def write_outputs(sections, out_dir, source):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    meta = []
    for i, s in enumerate(sections):
        fname = f"section_{s['id']}.md"
        body = f"# {s['title']}\n\n{s['content']}\n" if s["id"] != "0" else s["content"] + "\n"
        (out / fname).write_text(body, encoding="utf-8")
        meta.append({"file": fname, "section": s["id"], "title": s["title"],
                     "parent": s["parent"], "level": s["level"], "path": s["path"],
                     "order": i, "source": source, "char_count": len(s["content"]),
                     "contains_table": "|" in s["content"] and "---" in s["content"],
                     "contains_image": "![" in s["content"] or "<!-- image -->" in s["content"]})
    (out / "sections_metadata.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "hierarchy.json").write_text(
        json.dumps({s["id"]: s["title"] for s in sections if s["id"] != "0"}, indent=2, ensure_ascii=False),
        encoding="utf-8")
    return meta


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("input_md"); ap.add_argument("--out", default="sections_out")
    a = ap.parse_args()
    secs = add_paths(decompose(Path(a.input_md).read_text(encoding="utf-8")))
    meta = write_outputs(secs, a.out, Path(a.input_md).name)
    print(f"{len(meta)} sections written to {a.out}/")
    for m in meta:
        print(f'  {m["section"]:<8} parent={str(m["parent"]):<6} {m["title"]}')