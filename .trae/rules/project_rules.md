1. Frameworks:
    - Frontend Framework: Streamlit >=1.35.0
    - Backend Framework: FastAPI >=0.110.0
    - LLM Integration: OpenAI GPT-4o via Trae’s MCP agents
    - DB Layer: in-memory SQLite DB
2. Details on the testing framework.
API & Backend Testing: pytest >=8.0 with httpx for async endpoint testing
3. No login required for demo
4. Backend endpoints protected using a mock header-based role check:
5. Files Management:
    - Allowed formats: .pdf, .csv, .txt
    - Max file size: 5MB (Streamlit limit override optional)
    - Files stored with hashed filenames and linked to query ID
    - Files are ephemeral — purged every 30 minutes in demo
6. Each MCP agent has a single responsibility:
    - Query Enhancement Agent
    - Safety Scoring Agent
    - Triage Agent
    - Doctor Approval Agent
    - Agent context includes patient message + file summary + AI history
    - Agents use shared rules and prompt templates stored in rules.md
7. Documentation:
    - README includes: setup, role guide, agent strategy, safety rationale
    - Swagger docs generated via FastAPI for all endpoints
    - Diagram of data + AI flow for judges
    - Bonus: Test scripts & demo data for fast judge replay


