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

<img width="1919" height="888" alt="Screenshot 2025-11-09 235557" src="https://github.com/user-attachments/assets/df43ea7c-f264-48a1-ab15-9334c7ea02ba" />


---

### 🧰 Installation & Setup Guide

Follow these steps to set up and run the **AI Music Plagiarism Detector** on your system.

---

#### 🧩 Step 2: Setup Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # on Windows
source venv/bin/activate  # on Mac/Linux
```

---

#### 📦 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all necessary packages including Flask, TensorFlow, FAISS, OpenL3, and CustomTkinter.

---

#### ⚙️ Step 4: Run the Flask Backend

```bash
python app.py
```

Once started, the backend runs locally at:

```
http://127.0.0.1:5000
```

Keep this terminal open while the app is running.

---

#### 💻 Step 5: Launch the Frontend UI

```bash
python frontend_ui.py
```

This opens the interactive **GitHub-styled desktop interface** where you can:

* Upload audio and lyrics files
* Run plagiarism analysis
* View similarity results
* Save reports or screenshots

---

### 📂 Folder Structure

```
Plag/
│
├── app.py                         # Flask backend for AI processing
├── frontend_ui.py                 # CustomTkinter frontend (GitHub-style UI)
├── requirements.txt               # Python dependencies
│
├── scripts/                       # Core similarity logic
│   ├── check_audio_sim.py
│   ├── check_lyrics_similarity.py
│   └── check_hybrid_simf.py
│
├── utils/                         # Helper utilities
│   ├── openl3_utils.py
│   ├── lyrics_utils.py
│   └── ...
│
├── data/                          # Uploads & results
│   └── uploads/
│
├── github_icon.png                # GitHub logo icon used in UI
└── README.md                      # Project documentation
```

---

✅ After completing these steps, your AI Music Plagiarism Detector will be fully operational and ready for use.

