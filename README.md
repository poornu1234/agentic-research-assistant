# 📌 Agentic Research Assistant

This project implements an autonomous **research assistant API** using **FastAPI**, **Wikipedia**, and **HuggingFace Transformers (BART)**.  
It accepts a research topic and generates a structured, human-readable report — including source URL, citation, related topics, and useful stats.

---

## 🚀 Features
✅ Autonomous multi-step agent: search → summarize → structure  
✅ No paid APIs — fully free using open models  
✅ Returns:
- 📌 Structured report (Intro, Key Points, Conclusion)
- 🔗 Source URL
- 📚 Suggested related topics
- ✏️ Citation (ready to paste)
- 📊 Summary statistics  

✅ Exposes a REST API endpoint `/analyze/`  

---

## ⚙️ Tech stack
- **Python 3.x**
- **FastAPI**
- **Wikipedia API (via `wikipedia` lib)**
- **HuggingFace Transformers (`facebook/bart-large-cnn`)**
- **Uvicorn**




