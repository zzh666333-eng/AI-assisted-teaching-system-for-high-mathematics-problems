[README.md](https://github.com/user-attachments/files/28542466/README.md)
# AI-assisted-teaching-system-for-high-mathematics-problems
Synthesize advanced mathematics problems and conduct problem review and correction
# T2P Mentor

AI-driven calculus practice and audit system for problem generation, handwritten answer review, and adaptive learning support.

![T2P Mentor Home](assets/screenshots/home.png)

## Overview

T2P Mentor is an intelligent mathematics learning assistant focused on calculus practice. It combines structured problem generation, adaptive task recommendation, and multimodal answer auditing into one workflow, helping students move from targeted practice to feedback-driven improvement.

The project currently includes:

- Configurable problem generation by topic, mode, difficulty, and question type
- Adaptive learning continuation based on user progress
- AI auditing for handwritten photo uploads and text answers
- Topic-based progress tracking and learning history persistence
- FastAPI backend for integration with a web frontend

## Demo Screens

### Main workspace

Students can choose the knowledge dimension, practice mode, difficulty level, and question type before generating a problem.

![Main workspace](assets/screenshots/home.png)

### Photo upload and audit

The system accepts handwritten work as an image, then sends it through the multimodal audit pipeline.

![Photo upload and audit](assets/screenshots/upload-audit.png)

### AI audit report

After analysis, T2P Mentor returns a structured report including correctness, logical alignment score, error analysis, tutor feedback, and next-step guidance.

![AI audit report](assets/screenshots/report.png)

## Key Features

### 1. Intelligent problem generation

- Generate questions by topic, mode, difficulty, and question type
- Support `drill` mode for focused practice
- Support `exam` mode for integrated, cross-topic synthesis
- Persist generated problems as JSON for later reuse and auditing

### 2. Handwritten solution auditing

- Accept base64 images or text submissions
- Compare student work against the selected problem and reference solution
- Return structured feedback with:
  - correctness
  - logical alignment score
  - error analysis
  - tutor feedback
  - next-step hints

### 3. Adaptive learning loop

- Maintain user progress by topic
- Recommend the next topic, mode, and difficulty automatically
- Record results after each task to update mastery and progression level

### 4. API-first backend

- Built on FastAPI
- Easy to connect with a web client or other learning interfaces
- Clear endpoint separation for generation, auditing, and user progress

## How It Works

The core request flow is:

1. The frontend sends a request to the FastAPI backend.
2. `api_server.py` routes the request to the matching handler.
3. Request parameters are parsed into models such as `GenerateRequest` or `AuditRequest`.
4. Business logic is delegated to `UserSession`, `BatchGenerator`, `ProblemGenerator`, and `GoldenDataLoader`.
5. Prompts are assembled and sent to Gemini through `GeminiClient`.
6. Model output is post-processed, validated, and scored.
7. Results are stored as JSON or written into user progress records.
8. The backend returns a structured JSON response to the client.

## Project Structure

```text
T2P/
├─ api_server.py           # FastAPI backend entry
├─ main.py                 # CLI entry for generation and review
├─ requirements.txt        # Python dependencies
├─ data/                   # Golden dataset and user progress data
├─ output/                 # Generated problems and reports
├─ logs/                   # Runtime logs
├─ assets/screenshots/     # README screenshots
├─ t2p-web/                # Frontend workspace / build artifacts
└─ src/
   ├─ config.py            # Environment and path configuration
   ├─ batch_generator.py   # Generation orchestration
   ├─ generator.py         # Core problem generation logic
   ├─ gemini_client.py     # Gemini / Vertex AI integration
   ├─ data_loader.py       # Dataset loading and problem lookup
   ├─ user_session.py      # User progress and adaptive recommendation
   ├─ prompt_builder.py    # Prompt construction
   ├─ postprocessor.py     # Output parsing and cleanup
   └─ evaluator.py         # Quality evaluation
```

## Tech Stack

- Backend: FastAPI, Pydantic, Uvicorn
- AI: Google Gemini via `google-genai`, Vertex AI compatible config
- ML utilities: `sentence-transformers`, `scikit-learn`, `torch`
- Data / plotting: `numpy`, `matplotlib`
- Frontend: local web interface in `t2p-web`

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/T2P.git
cd T2P
```

### 2. Create a Python environment

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS / Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install backend dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GEMINI_MODEL=gemini-2.5-pro
GOOGLE_API_KEY=your-api-key-if-needed
```

Notes:

- The project prefers Vertex AI mode when `GOOGLE_API_KEY` is not provided.
- `GOOGLE_CLOUD_PROJECT` is required for Vertex AI authentication.

### 5. Run the backend

```bash
uvicorn api_server:app --reload
```

Default backend URL:

```text
http://127.0.0.1:8000
```

### 6. Run the frontend

If the frontend source is available in `t2p-web`, start it separately:

```bash
cd t2p-web
npm install
npm run dev
```

Default frontend URL:

```text
http://localhost:3000
```

## API Endpoints

### General

- `GET /` - service status and dataset summary
- `GET /topics` - list available topics

### User

- `POST /user/login` - login or create a user session
- `GET /user/progress/{user_id}` - fetch detailed user progress
- `POST /user/record` - record learning result

### Learning flow

- `POST /generate` - generate one or more questions
- `POST /audit` - audit a handwritten or text answer

## Example Request

### Generate a question

```bash
curl -X POST "http://127.0.0.1:8000/generate" \
  -H "Content-Type: application/json" \
  -d "{\"topics\": [\"Applications of Derivatives\"], \"num\": 1, \"mode\": \"drill\", \"difficulty\": 3, \"question_type\": \"calculation\", \"user_id\": \"zzh\"}"
```

### Audit a submission

```bash
curl -X POST "http://127.0.0.1:8000/audit" \
  -H "Content-Type: application/json" \
  -d "{\"problem_id\": \"example_id\", \"student_work_image\": \"A\", \"is_exam_mode\": false}"
```

## Use Cases

- AI-assisted calculus tutoring
- Handwritten solution review
- Adaptive practice systems
- Educational AI demos and coursework projects

## Current Notes

- The backend code is the main stable entry point for request handling and AI orchestration.
- The `t2p-web` directory in the current archive appears to contain frontend runtime artifacts; if you plan to open-source the full web app, include the full source version of the frontend as well.

## Roadmap Ideas

- Add Docker-based one-command startup
- Add unit and integration tests for API endpoints
- Improve deployment instructions for cloud hosting
- Add richer analytics dashboards for long-term learning progress

## License

Choose a license before publishing publicly, such as MIT, Apache-2.0, or GPL-3.0.

## Acknowledgements

This project combines LLM-based generation, multimodal auditing, and adaptive learning logic to explore how AI can support structured mathematics education workflows.
