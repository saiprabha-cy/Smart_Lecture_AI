# 🎓 Smart Lecture AI Assistant

**AI-Based Lecture Audio Understanding System**

---

## 📌 Overview

Smart Lecture AI Assistant is an **Artificial Intelligence–based educational tool** that converts recorded lecture audio into structured study material. The system automatically generates **lecture transcripts, summaries, key concepts, and exam-oriented questions** using **Speech Recognition and Natural Language Processing (NLP)** techniques.

This project aims to reduce the manual effort involved in revising long lecture recordings and improve learning efficiency for students.

---

## 🚀 Features

* 🎧 Upload lecture audio files (WAV format)
* 🗣️ Speech-to-Text conversion using ML-based ASR
* 🧠 NLP-based concept extraction
* 📝 Automatic summary generation
* ❓ Exam-oriented question generation
* 🌐 Simple and interactive web interface

---

## 🧠 AI / ML Components Used

* **Automatic Speech Recognition (ASR)** using pretrained machine learning models (VOSK)
* **Natural Language Processing (NLP)** using NLTK:

  * Tokenization
  * Stopword removal
  * Keyword extraction
  * Sentence scoring
* Rule-based NLP logic for educational content generation

> ✔ This project uses **pretrained AI models**, which is a standard and accepted AI application approach.

---

## 🏗️ System Architecture

```
Lecture Audio (.wav)
        ↓
Speech Recognition (VOSK - ML)
        ↓
Text Preprocessing (NLP)
        ↓
Concepts | Summary | Questions
        ↓
Streamlit Web Interface
```

---

## 🛠️ Technologies Used

* Python 3.x
* VOSK (Speech Recognition – Machine Learning)
* NLTK (Natural Language Processing)
* Streamlit (Web UI)
* WAV Audio Processing

---

## 📂 Project Structure

```
smart-lecture-ai/
│
├── app.py                 # Streamlit web application
├── processor.py           # NLP processing logic
├── transcriber.py         # Speech-to-text logic
├── sample_audio/
│   └── demo_lecture.wav   # Sample lecture audio
├── outputs/
│   └── sample_output.txt
├── requirements.txt
└── README.md
```

---

## 📊 Dataset / Data Source

* **Input Data:** Real lecture audio recordings (WAV format)
* **Source:** Classroom-style or recorded lectures
* **Dataset Type:** Real-time input data

> 📌 No Kaggle dataset is used because the system is designed to process **real-world lecture audio**, making it more practical and application-oriented.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/smart-lecture-ai.git
cd smart-lecture-ai
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🖥️ Output

The system generates:

* Lecture transcript
* Important concepts
* Concise summary
* Exam-oriented questions

These outputs are displayed directly on the web interface.

---

## ✅ Results

* Successfully transcribes lecture audio
* Generates meaningful summaries
* Extracts key educational concepts
* Produces relevant questions for revision

---

## ⚠️ Limitations

* Best performance with clear audio
* Currently supports English language only
* Question generation is rule-based (can be improved using LLMs)

---

## 🔮 Future Enhancements

* Multilingual lecture support
* PDF / PPT export of notes
* Integration with Learning Management Systems (LMS)
* Advanced AI-based question generation
* Cloud deployment

---

## 🎯 Applications

* Engineering education
* Online learning platforms
* Exam preparation tools
* Digital classrooms

---

## 📚 References

* VOSK Speech Recognition Toolkit
* NLTK Documentation
* Streamlit Documentation
* AICTE Educational AI Guidelines

---

## 🙏 Acknowledgment

This project was developed as part of the **AICTE – EduNet / IBM Internship Program** to demonstrate the practical application of Artificial Intelligence in education.

---

## 👤 Author

**SaiPrabha C Y**
Electronics and Communication Engineering
*(Add LinkedIn / GitHub link if you want)*

---

⭐ *If you find this project useful, please give it a star!*
