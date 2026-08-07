# 📚 AI Study Companion

An AI-powered study planning application that helps students generate personalized study schedules directly from their syllabus.

Instead of manually planning what to study each day, students can simply upload their syllabus as a PDF, choose the number of days they want to complete it, and receive a structured study plan generated using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs).

---

# ✨ Features

- 📄 Upload syllabus in PDF format
- ✂️ Automatically extract text from the uploaded document
- 🧩 Split the syllabus into semantic chunks
- 🧠 Generate embeddings using Sentence Transformers
- 🔎 Store embeddings inside Qdrant Vector Database
- ⚡ Retrieve the most relevant syllabus content using semantic search
- 🤖 Generate an AI-powered personalized study plan
- 📅 Plan based on the number of study days selected by the student
- 🎨 Clean and responsive Next.js frontend
- ⚙️ FastAPI backend for AI processing

---

# 🏗️ Project Architecture

```
                    User Uploads PDF
                            │
                            ▼
                  PDF Text Extraction
                            │
                            ▼
                    Text Chunking
                            │
                            ▼
             SentenceTransformer Embeddings
                            │
                            ▼
                  Qdrant Vector Database
                            │
                            ▼
                 Semantic Similarity Search
                            │
                            ▼
                Retrieved Relevant Chunks
                            │
                            ▼
          OpenRouter Free LLM (DeepSeek)
                            │
                            ▼
             Personalized Study Plan
                            │
                            ▼
                 Displayed on Frontend
```

---

# 🛠 Tech Stack

## Frontend

- Next.js 15
- React
- TypeScript
- Tailwind CSS

## Backend

- FastAPI
- Python
- Uvicorn

## AI

- SentenceTransformers
- all-MiniLM-L6-v2
- OpenRouter API
- DeepSeek (Free LLM)

## Vector Database

- Qdrant Cloud

## PDF Processing

- PyMuPDF (fitz)

---

# 📂 Project Structure

```
AI_Study_Companion
│
├── backend
│   ├── main.py
│   ├── gemini.py
│   ├── qdrant_db.py
│   ├── util.py
│   ├── requirements.txt
│   └── .env
│
├── frontend
│   ├── app
│   ├── public
│   ├── package.json
│   └── ...
│
└── README.md
```

---

# ⚙️ How It Works

## Step 1

The user uploads a syllabus in PDF format.

Example:

```
Operating Systems
Artificial Intelligence
Computer Networks
...
```

---

## Step 2

The backend extracts all text from the uploaded PDF.

---

## Step 3

The extracted text is divided into smaller chunks.

Example:

```
Chunk 1

Introduction to Operating Systems...

Chunk 2

CPU Scheduling...

Chunk 3

Deadlocks...

...
```

---

## Step 4

Each chunk is converted into a vector embedding using:

```
all-MiniLM-L6-v2
```

---

## Step 5

All embeddings are stored inside Qdrant Cloud.

---

## Step 6

The user enters the number of days.

Example

```
30 Days
```

---

## Step 7

The application searches Qdrant for the most relevant syllabus chunks.

---

## Step 8

Those chunks are sent to an LLM through OpenRouter.

The LLM generates a structured study plan based only on the uploaded syllabus.

---

## Step 9

The study plan is displayed on the frontend.

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI_Study_Companion.git

cd AI_Study_Companion
```

---

# Backend Setup

## 2. Navigate to backend

```bash
cd backend
```

---

## 3. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Create Environment Variables

Create a file named

```
.env
```

Add:

```env
OPENROUTER_API_KEY=your_openrouter_api_key

QDRANT_URL=your_qdrant_url

QDRANT_API_KEY=your_qdrant_api_key
```

---

## 6. Start Backend

```bash
uvicorn main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

Swagger documentation

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Open a new terminal.

---

## Navigate to frontend

```bash
cd frontend
```

---

## Install Dependencies

```bash
npm install
```

---

## Install Markdown Renderer

```bash
npm install react-markdown
```

---

## Run Frontend

```bash
npm run dev
```

Open

```
http://localhost:3000
```

---

# Using the Application

## Upload a PDF

Click

```
Upload Syllabus
```

Select your syllabus PDF.

Wait until upload completes.

---

## Enter Study Duration

Example

```
15

30

45
```

days.

---

## Generate Study Plan

Click

```
Generate Study Plan
```

The backend will

- Search Qdrant
- Retrieve relevant syllabus chunks
- Send them to the LLM
- Generate a personalized study schedule

---

## View Results

The generated study plan appears directly on the page.

---

# API Endpoints

## Upload PDF

```
POST /upload
```

Uploads a syllabus and stores embeddings.

---

## Ask Question

```
POST /ask
```

Answers questions using Retrieval-Augmented Generation.

---

## Generate Study Plan

```
POST /generate-study-plan
```

Generates a personalized study schedule.

---

# Requirements

## Python

Python 3.11+

---

## Node.js

Node.js 20+

---

## npm

Latest version recommended.

---

# Environment Variables

Backend requires

```
OPENROUTER_API_KEY

QDRANT_URL

QDRANT_API_KEY
```

Never commit your `.env` file.

---

# Future Improvements

- PDF study plan download
- Copy study plan
- Weekly calendar view
- Daily reminders
- User authentication
- Multiple uploaded syllabi
- Progress tracking
- Dark mode
- Editable study plans
- AI chat with uploaded syllabus
- Quiz generation
- Flashcard generation
- Study analytics

---

# Screenshots

You can add screenshots here after running the application.

Example

```
Home Page

Upload PDF

Generated Study Plan
```

---

# License

This project is open-source and available for educational purposes.

---

# Author

**Laiba Ausaf**

Computer Science Undergraduate

AI & Full Stack Developer

GitHub:
https://github.com/Laibaausaf

LinkedIn:
https://linkedin.com/in/laibaausaf