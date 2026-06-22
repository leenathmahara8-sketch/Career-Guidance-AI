# CareerWise AI — Agent Guide

## Quick start
```powershell
pip install -r requirements.txt
python random_forest_model.py    # train RF model (produces models/*.joblib)
python app.py                     # dev server at http://127.0.0.1:5000
```

## Key commands
| Command | Purpose |
|---------|---------|
| `python random_forest_model.py` | Train RF from Excel, saves to `models/rf_model.joblib` |
| `python generate_dataset.py` | Generate synthetic CSV → `data/student_career_data.csv` |
| `python app.py` | Start Flask dev server (Python 3.13) |

No tests exist (`tests/` is an empty package). No lint/formatter config.
CareerEngine auto-trains on first startup from `data/student_career_data.csv` (~10s).

## Architecture

- **app.py** — Flask factory; registers blueprints, attaches services, creates DB tables
- **config.py** — reads env vars, path constants, CORS config
- **routes/** — 6 blueprints: `health`, `auth`, `predict`, `chat`, `resume`, `assess`
- **services/** — `career_engine.py`, `prediction.py`, `chatbot.py`, `auth.py`, `skill_gap.py`, `course_recommender.py`, `key_manager.py`
- **templates/** — Jinja2 (assess form, results, history)
- **Static HTML** in root: `Ai and Ml.html`, `login.html` (`/login`), `cv.html` (`/cv`)
- **New**: `POST /api/assess` JSON endpoint; `/history` pagination (10 per page)

## Two ML pipelines (different data sources)

1. **`random_forest_model.py`** — standalone script, reads `career data_ set.csv (1).xlsx`, trains RF → `models/rf_model.joblib` + encoders. Backend loads this via `PredictionEngine`.
2. **`services/career_engine.py`** — reads `data/student_career_data.csv`, trains DT + RF → `models/career_*.joblib`. Auto-trains if artefacts missing. Used by assessment form at `/assess`.

Both must exist for full functionality.

## Env & secrets

Copy `.env.example` → `.env`. Key variables:
- `LLM_PROVIDER` — `openai` (default), `gemini`, or `ollama`
- `OPENAI_API_KEY` / `GEMINI_API_KEY` — required for respective providers
- `FLASK_SECRET_KEY` — random string for session signing
- `.env` is gitignored; `.env.example` has placeholder keys (safe to commit)

## Chatbot providers
- **OpenAI** (`gpt-3.5-turbo`) — needs `OPENAI_API_KEY`
- **Gemini** (`gemini-flash-lite-latest`) — needs `LLM_PROVIDER=gemini` + `GEMINI_API_KEY`
- **Ollama** (local) — set `LLM_PROVIDER=ollama`, needs `ollama serve` running; uses `llama3.2` by default (override via `OLLAMA_MODEL`)
- **Fallback** — rule-based keyword matching works with zero config when no provider is available

## Known bug: chatbot fallback not wired

When Gemini/OpenAI quota is exhausted or the provider fails, `routes/chat.py:24` catches `RuntimeError` and returns 503 instead of falling back to `ChatbotService._chat_fallback()`. The rule-based fallback works (no API key needed) but is never reached. Fix: in `chat.py`, catch the error and retry with `chatbot_service._chat_fallback(message)`.

## Auth quirks
- SQLite `users.db` for user storage; in-memory dict for session tokens
- Tokens lost on server restart (intentional for portfolio scope)
- `users.db` is gitignored

## Resume analysis
- `.txt` files: full text extraction + LLM analysis
- `.pdf/.doc/.docx`: metadata-only (no `pdfplumber`/`python-docx` installed)
- Max file size: 5 MB

## Gotchas
- The project root is the Flask static folder — do not delete `Ai and Ml.html`, `login.html`, `cv.html`
- `models/` directory is gitignored — always regenerate after clone: `python random_forest_model.py`
- `FLASK_DEBUG=true` enables auto-reload; disable in production
- CORS allows all origins (`*`) — safe for portfolio-only deployment
- Both the Excel-based RF (`random_forest_model.py`) and CSV-based DT+RF (`CareerEngine`) train separate models; one is not a substitute for the other
- `data/courses.json` drives course recommendations on results page; add careers there if expanding the model
