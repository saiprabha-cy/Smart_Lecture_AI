import speech_recognition as sr
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

# Extra weak words to ignore
CUSTOM_IGNORE = {
    "today", "learn", "about", "will", "also", "into", "vice", "versa"
}

def sentence_split(text):
    return [s.strip() for s in re.split(r"[.!?]", text) if s.strip()]

def word_tokenize_safe(text):
    return re.findall(r"\b[a-zA-Z]+\b", text.lower())

def process_lecture(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        transcript = recognizer.recognize_google(audio)

    sentences = sentence_split(transcript)
    words = word_tokenize_safe(transcript)

    stop_words = set(stopwords.words("english"))

    keywords = [
        w for w in words
        if w not in stop_words
        and w not in CUSTOM_IGNORE
        and len(w) > 4
    ]

    # Pick top technical concepts
    concepts = list(dict.fromkeys(keywords))[:5]

    summary = sentences[0] if sentences else transcript

    questions = [
        f"Explain the concept of {concept}."
        for concept in concepts[:3]
    ]

    return {
        "transcript": transcript,
        "summary": summary,
        "concepts": concepts,
        "questions": questions
    }
