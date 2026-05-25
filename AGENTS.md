# AI Agent Instructions for Graph Pipeline Analyzer

## 1. Project Context
This project is a stateless web application designed to transform tabular datasets (CSV) into structured network graphs. It uses mathematical similarity (Cosine) and topological inference to generate homogeneous and heterogeneous connections between nodes.

## 2. Tech Stack
- **Environment & Package Manager:** `uv`
- **Backend Framework:** FastAPI (Python 3.10+)
- **Data Processing:** Pandas, Scikit-learn (StandardScaler, cosine_similarity)
- **Graph Mathematics:** NetworkX
- **Visualization (Backend-rendered):** Matplotlib (Agg backend)
- **Data Validation:** Pydantic
- **Frontend Template Engine:** Jinja2
- **Frontend Reactivity:** Alpine.js (via CDN)
- **Frontend Styling:** Vanilla CSS (No heavy frameworks)

## 3. Architecture & Directory Structure
The application follows a modular, MVC-like structure. 
**Agent Rule:** ALWAYS respect this exact structure. Do not create new directories unless explicitly requested.

```text
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI initialization and static/router mounting ONLY
│   ├── routes.py        # API Endpoints and HTTP logic
│   ├── schemas.py       # Pydantic models and Enums for strict validation
│   ├── static/          # Static assets (CSS, JS)
│   ├── templates/       # Jinja2 HTML templates
│   └── utils/           # Helper functions (e.g., pandas type mapping)
├── tests/               # Pytest files
└── pyproject.toml       # uv dependency management

```

## 4. Core Business Logic (The Graph Pipeline)

When modifying the graph generation logic (`generate_graph`), adhere to the established 4-step pipeline:

1. **Graph Building (Features):** Calculate cosine similarity on standardized numeric data. Create edges if weight $\ge \epsilon$. Tag edge `type='feature'`.
2. **Emergent Relationships:** Infer edges topologically. If two unconnected nodes share $\ge 2$ neighbors, connect them. Tag edge `type='emergent'`.
3. **Pruning:** Remove ANY edge where weight is below the pruning threshold.
4. **Communities:** Use NetworkX's Louvain community detection (`nx.community.louvain_communities`) as a proxy for Leiden to assign node colors.

**Important Graph Constraints:**

* The graph is an undirected, weighted multi-edge conceptual graph.
* We deliberately use **two types of edges** (Features vs. Emergent) for visual interpretability. Keep this logic intact.

## 5. Coding Standards & Agent Rules

### Python / Backend Rules:

* **Strict Typing:** Use Python type hints and Pydantic models for ALL incoming/outgoing data payloads.
* **Statelessness:** DO NOT introduce databases (SQL, NoSQL, Neo4j, etc.) unless explicitly instructed. The application operates in-memory per request.
* **Error Handling:** Use `HTTPException` from FastAPI to return clear, user-facing error messages to the frontend.
* **Matplotlib Threading:** Matplotlib is run in a server environment. ALWAYS use `matplotlib.use('Agg')` and ensure figures are explicitly closed (`plt.close()`) to prevent memory leaks.

### Frontend Rules:

* **Reactivity:** Use Alpine.js (`x-data`, `x-model`, `x-show`, etc.) for DOM manipulation. DO NOT use jQuery or vanilla JS DOM selectors (`document.getElementById`) unless absolutely necessary.
* **Styling:** Keep CSS simple, semantic, and contained within `app/static/css/style.css`.
* **Separation of Concerns:** HTML handles structure and Alpine directives. JS functions go in `app/static/js/app.js`. CSS goes in its own file.

## 6. Developer Commands

* Setup: `uv venv` and `uv pip install -e .`
* Run Server: `uvicorn app.main:app --reload`
* Run Tests: `pytest tests/`
