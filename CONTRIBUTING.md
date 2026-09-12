# Contributing

Contributions are welcome once the taxonomy stabilizes.

## Principles

1. Reuse an existing component before creating a new one.
2. Do not change an existing component ID to mean something different.
3. Give every new flow a unique `F###` identifier.
4. Keep vendor names in `examples` rather than component names whenever possible.
5. Threats may map to both components and flows.
6. Controls should be technology-neutral where practical.
7. Logical Mermaid views should remain readable without security overlays.
8. Detailed Draw.IO diagrams may add trust boundaries, controls, and annotations without redefining the canonical taxonomy.

## Validation

Run:

```bash
python3 scripts/validate_model.py
python3 scripts/generate_mermaid.py
```
