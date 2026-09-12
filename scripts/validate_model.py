#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    with open(ROOT / "data" / name, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def duplicates(items):
    seen = set()
    dup = set()
    for x in items:
        if x in seen:
            dup.add(x)
        seen.add(x)
    return sorted(dup)

def main():
    errors = []

    components = load("components.yaml")["components"]
    flows = load("flows.yaml")["flows"]
    views = load("views.yaml")["views"]
    threats = load("threats.yaml")["threats"]
    controls = load("controls.yaml")["controls"]

    component_ids = [c["id"] for c in components]
    flow_ids = [f["id"] for f in flows]
    threat_ids = [t["id"] for t in threats]
    control_ids = [c["id"] for c in controls]

    for label, ids in [
        ("component", component_ids),
        ("flow", flow_ids),
        ("threat", threat_ids),
        ("control", control_ids),
    ]:
        d = duplicates(ids)
        if d:
            errors.append(f"duplicate {label} IDs: {', '.join(d)}")

    component_set = set(component_ids)
    flow_set = set(flow_ids)

    for f in flows:
        if f["source"] not in component_set:
            errors.append(f'{f["id"]}: unknown source {f["source"]}')
        if f["destination"] not in component_set:
            errors.append(f'{f["id"]}: unknown destination {f["destination"]}')

    for v in views:
        for cid in v.get("components", []):
            if cid not in component_set:
                errors.append(f'view {v["id"]}: unknown component {cid}')
        for fid in v.get("flows", []):
            if fid not in flow_set:
                errors.append(f'view {v["id"]}: unknown flow {fid}')

    for t in threats:
        for cid in t.get("applies_to_components", []):
            if cid not in component_set:
                errors.append(f'{t["id"]}: unknown component {cid}')
        for fid in t.get("applies_to_flows", []):
            if fid not in flow_set:
                errors.append(f'{t["id"]}: unknown flow {fid}')

    if errors:
        print("Validation failed:")
        for e in errors:
            print(f" - {e}")
        return 1

    print(
        f"Validation passed: {len(component_ids)} components, "
        f"{len(flow_ids)} flows, {len(threat_ids)} threats, "
        f"{len(control_ids)} controls, {len(views)} views."
    )
    return 0

if __name__ == "__main__":
    sys.exit(main())
