# Data Analyst Agent

A FastAPI-based web service that uses Python (and optionally an LLM) to automatically source, prepare, analyze, and visualize data—returning JSON answers and base64-encoded plots within 3 minutes.

## 🔍 Features

- **/api/** endpoint accepting a plain-text task description
- **Web scraping** (e.g. Wikipedia tables) via HTTPX + BeautifulSoup
- **Data analysis** using Pandas, NumPy, DuckDB
- **Statistical modeling** (correlation, regression) with scikit-learn
- **Visualization** with matplotlib, returned as `data:image/png;base64,...`
- Optional **LLM integration** (OpenAI or local via Ollama) to generate/extract Python code dynamically

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git
- (Optional) OpenAI API key in `.env` if using LLM  
  ```env
  OPENAI_API_KEY=sk-…
