# 🎧 AI Music Plagiarism Detector

> **Analyze and detect music plagiarism using AI-powered audio and lyrics similarity models.**

---

## 🧠 Overview

The **AI Music Plagiarism Detector** is a deep-learning-based desktop application designed to detect plagiarism between audio tracks and lyrics.  
It uses **OpenL3 embeddings**, **FAISS similarity search**, and **semantic text analysis** to evaluate originality in music content — combining **audio signal features** and **lyrical meaning** into a single hybrid similarity score.

This project is built with a **Flask backend (Python)** for model processing and a **CustomTkinter frontend** styled like **GitHub’s dark dashboard** for an elegant and interactive user experience.

---

## ⚙️ Tech Stack

| Layer | Technology | Description |
|-------|-------------|-------------|
| 🎵 **Audio Embedding** | OpenL3 + Librosa | Converts audio into high-dimensional feature embeddings |
| 🧩 **Similarity Engine** | FAISS | Fast vector similarity comparison |
| 🗣️ **Lyrics Analysis** | SentenceTransformer | Computes semantic similarity of lyrics |
| 🔧 **Backend** | Flask (Python) | Handles API requests and analysis logic |
| 🖥️ **Frontend** | CustomTkinter | GitHub-style UI with modern design |
| 🧠 **ML Framework** | TensorFlow / Keras | Underlying model backend for embedding extraction |

---

## ✨ Key Features

| Feature | Description |
|----------|-------------|
| 🎚️ **Hybrid Similarity Check** | Compares both audio and lyrics for more accurate plagiarism detection |
| 📊 **Dynamic Similarity Meter** | Displays similarity percentage with color-coded results |
| 📂 **Upload Support** | Accepts `.mp3`, `.wav`, `.txt` files for dual analysis |
| 💾 **Save & Log** | Automatically logs previous results and allows saving reports |
| 📸 **Screenshot Feature** | Export current UI state as an image |
| 🌈 **GitHub-Themed UI** | Dark, sleek, responsive interface modeled after GitHub’s design |
| 🧭 **Top Navigation Bar** | Includes Home, Docs, About, and Support links |
| 🪶 **Lyrics Intelligence** | Uses language models to find textual resemblances beyond surface-level matching |

---

## ⚡ How It Works

1. **Upload** your audio file and optional lyrics file.  
2. The backend extracts **audio embeddings** using OpenL3 and **text embeddings** using SentenceTransformer.  
3. Both embeddings are compared using **FAISS** for vector similarity.  
4. Results are combined into a final plagiarism score (0–100%).  
5. The UI displays a **color-coded similarity bar** and logs the results automatically.

---

## 🖥️ Frontend Preview

> _(Use the built-in 📸 Screenshot button in the app to take and upload a preview image here.)_

Example:
![Preview UI])

---

## 🧰 Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/AashirZayd/music-plagiarism-detector.git
cd music-plagiarism-detector

### Setup Virtual Environment
