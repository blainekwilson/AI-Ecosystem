#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]

CATEGORY_CLASS = {
    "user": "user",
    "application": "app",
    "agent": "agent",
    "model": "model",
    "knowledge": "knowledge",
    "protocol": "protocol",
    "tool": "tool",
    "data": "data",
    "identity": "identity",
    "control": "control",
    "external": "external",
    "lifecycle": "lifecycle",
}

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def safe_label(text):
    return text.replace('"', "'").replace("\n", " ")

def render_view(view, components_by_id, flows_by_id):
    lines = [
        "flowchart LR",
        "    %% Generated from data/components.yaml + data/flows.yaml + data/views.yaml",
    ]

    for cid in view["components"]:
        c = components_by_id[cid]
        label = f'{c["id"]} {c["name"]}'
        lines.append(f'    {cid}["{safe_label(label)}"]')

    lines.append("")

    for fid in view["flows"]:
        f = flows_by_id[fid]
        if f["source"] not in view["components"] or f["destination"] not in view["components"]:
            continue
        label = f'{f["id"]} {f["name"]}'
        lines.append(f'    {f["source"]} -->|"{safe_label(label)}"| {f["destination"]}')

    lines.append("")
    lines.extend([
        "    classDef user fill:#eef6ff,stroke:#5b8def,color:#111;",
        "    classDef app fill:#e9f7ef,stroke:#4f9d69,color:#111;",
        "    classDef agent fill:#fff0f0,stroke:#d85c5c,color:#111;",
        "    classDef model fill:#f4efff,stroke:#7a63b8,color:#111;",
        "    classDef knowledge fill:#eef8e8,stroke:#6f9e57,color:#111;",
        "    classDef protocol fill:#fff7e8,stroke:#c58a2a,color:#111;",
        "    classDef tool fill:#edf7ed,stroke:#4e8a4b,color:#111;",
        "    classDef data fill:#edf5ff,stroke:#5a84b8,color:#111;",
        "    classDef identity fill:#f5efff,stroke:#8b62b2,color:#111;",
        "    classDef control fill:#f7f1ff,stroke:#765aa6,color:#111;",
        "    classDef external fill:#eef4ff,stroke:#5577aa,color:#111;",
        "    classDef lifecycle fill:#f8f5ed,stroke:#8a7953,color:#111;",
    ])

    category_groups = {}
    for cid in view["components"]:
        c = components_by_id[cid]
        category_groups.setdefault(c["category"], []).append(cid)

    for cat, ids in category_groups.items():
        cls = CATEGORY_CLASS.get(cat)
        if cls:
            lines.append(f'    class {",".join(ids)} {cls};')

    return "\n".join(lines) + "\n"

def main():
    components = load_yaml(ROOT / "data/components.yaml")["components"]
    flows = load_yaml(ROOT / "data/flows.yaml")["flows"]
    views = load_yaml(ROOT / "data/views.yaml")["views"]

    components_by_id = {c["id"]: c for c in components}
    flows_by_id = {f["id"]: f for f in flows}

    for view in views:
        output = ROOT / view["output"]
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render_view(view, components_by_id, flows_by_id), encoding="utf-8")
        print(f"generated {output.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
