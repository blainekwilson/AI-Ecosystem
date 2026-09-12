# AI Ecosystem

An open visual reference for understanding the components, interactions, threats, and security controls that make up modern AI systems.

## Project goals

This repository is intended to make the modern AI ecosystem easier to understand visually. It starts with a canonical component and flow taxonomy, then builds multiple views of the ecosystem rather than attempting to force everything into one diagram.

The project is designed to mature through four levels:

1. **Understand** — What are the components?
2. **Visualize** — How do the components interact?
3. **Threat Model** — What can go wrong with each component and interaction?
4. **Secure** — What controls should prevent, detect, or mitigate those threats?

## Design principles

- **One canonical vocabulary.** Component IDs and flow IDs remain stable across every view.
- **Multiple diagrams, one model.** Each diagram focuses on a different architectural concern.
- **Structured data first.** Components and flows live in YAML and can be used to generate diagrams.
- **Mermaid for logical views.** Mermaid diagrams are easy to review and maintain in Git.
- **Draw.IO for detailed visual views.** Presentation-grade and dense security diagrams can be added later.
- **Threats attach to both components and flows.** Security problems often exist at boundaries, not just inside boxes.
- **Controls map to threats.** Later versions should make the threat → control relationship explicit.

## Planned views

| View | Diagram | Purpose |
|---|---|---|
| 01 | AI Ecosystem Overview | 10,000-foot map of the ecosystem |
| 02 | AI Application Architecture | How chat, Copilot-style apps, models, context, tools, and agents fit together |
| 03 | Agentic AI Architecture | Observe → reason → act → observe loops and multi-agent coordination |
| 04 | AI Integration & MCP | APIs, function calling, MCP clients, MCP servers, tools, and external services |
| 05 | AI Data & Knowledge | Enterprise data, cloud data, RAG, embeddings, vector stores, memory, and context construction |
| 06 | AI Model Architecture | Foundation models, LLMs, multimodal models, embedding models, gateways, and providers |
| 07 | AI Identity & Access | Human identity, workload identity, delegated access, secrets, tokens, and tool permissions |
| 08 | AI Development & Supply Chain | Training data, fine-tuning, evaluation, registries, deployment, and dependency provenance |
| 09 | AI Security Controls | Security control overlay across the ecosystem |
| 10 | AI Threat Model | Threat overlay across components, flows, and trust boundaries |

## First logical view

```mermaid
flowchart LR
    U01[U01 User / Initiator]
    APP01[APP01 AI Application / Copilot]
    A01[A01 Agent]
    A02[A02 Agent Runtime / Orchestrator]
    M01[M01 Foundation / LLM Model]
    K01[K01 Context Construction]
    K02[K02 RAG / Retrieval]
    K03[K03 Memory]
    P01[P01 Function / Tool Calling]
    P02[P02 MCP Client]
    P03[P03 MCP Server]
    T01[T01 Tool / Connector]
    D01[D01 Internal Data]
    D02[D02 Cloud Data]
    X01[X01 External AI Provider]
    X02[X02 External Service]

    U01 -->|F001 Request| APP01
    APP01 -->|F002 Delegate| A02
    A02 -->|F003 Invoke agent| A01
    A01 -->|F004 Inference request| M01
    A01 -->|F005 Build context| K01
    K01 -->|F006 Retrieve knowledge| K02
    K01 -->|F007 Read/write memory| K03
    K02 -->|F008 Query internal data| D01
    K02 -->|F009 Query cloud data| D02
    A01 -->|F010 Tool request| P01
    P01 -->|F011 Native tool call| T01
    A01 -->|F012 MCP request| P02
    P02 -->|F013 MCP protocol| P03
    P03 -->|F014 Invoke tool| T01
    T01 -->|F015 External service call| X02
    M01 -->|F016 Provider inference| X01
```

## Repository layout

```text
ai-ecosystem/
├── data/
│   ├── components.yaml
│   ├── flows.yaml
│   ├── views.yaml
│   ├── threats.yaml
│   └── controls.yaml
├── diagrams/
├── docs/
├── schemas/
├── scripts/
└── README.md
```

## Generating Mermaid diagrams

Install PyYAML:

```bash
python3 -m pip install -r requirements.txt
```

Generate all logical Mermaid views:

```bash
python3 scripts/generate_mermaid.py
```

Validate IDs and references:

```bash
python3 scripts/validate_model.py
```

## Status

This is an initial draft. The component taxonomy is intentionally small enough to review before expanding into detailed threat and control mappings.

## License

No license has been selected yet. See `LICENSE-NOT-SELECTED.md`.
