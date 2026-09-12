# Architecture Notes

## What this repository means by "AI Ecosystem"

The **AI Ecosystem** is the collection of models, applications, agents, protocols, tools, data sources, identity systems, controls, external providers, and lifecycle processes that together create modern AI-enabled systems.

An LLM is therefore one component of the ecosystem, not the ecosystem itself.

## Core distinctions

### Foundation model vs. LLM

A foundation model is a broadly trained model that can be adapted to many tasks. An LLM is a foundation model focused primarily on language. Multimodal foundation models may process text, images, audio, or video.

### AI application / Copilot vs. model

A Copilot-style product is an AI application. It may combine one or more models with context construction, RAG, memory, agents, tools, identity, and policy controls.

### Agent vs. agent runtime

An agent is the goal-directed reasoning/acting component. The runtime or orchestrator manages execution state, retries, routing, approvals, workflow, and coordination.

### Tool vs. MCP server

A tool is a capability. An MCP server is a protocol endpoint that can expose tools, resources, or prompts to an MCP client. The MCP server is not necessarily the underlying business capability.

### RAG vs. vector database

RAG is a runtime retrieval pattern. A vector database or search index is one possible supporting component used by RAG.

### Memory vs. RAG

RAG retrieves knowledge relevant to the current task. Memory stores and retrieves state from prior interactions or prior agent activity.

## Threat-modeling direction

Later versions should map:

```text
Component -> Threat -> Control
Flow      -> Threat -> Control
```

Trust boundaries should be represented separately because many AI security failures occur when identity, data, control, or instructions cross boundaries.
