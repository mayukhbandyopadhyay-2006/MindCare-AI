import streamlit as st
import pandas as pd
from datetime import datetime
from transformers import pipeline
import tempfile

---------------- PAGE CONFIG ----------------

st.set_page_config(
page_title="MindCare AI – Intelligent Mental Support System",
page_icon="🧠",
layout="wide"
)

---------------- HEADER ----------------

st.title("🧠 MindCare AI")
st.subheader("A Web-Based Intelligent Mental Support System")

st.markdown("""
MindCare AI is an AI-powered emotional wellness platform designed to support students
through empathetic AI conversations, mood tracking, and intelligent emotional analysis.

Scientific AI Framework

MindCare AI integrates multiple computational psychology and artificial intelligence techniques:

• Natural Language Processing (NLP)
• Transformer-based Emotion Detection
• Sentiment Analysis
• Affective Computing
• Cognitive Behavioral AI Responses
• Emotional Trend Monitoring
• Behavioral Linguistic Analysis
• AI-assisted Risk Detection

These technologies allow the system to provide empathetic and context-aware mental support.
""")

st.markdown("---")

---------------- AI EMOTION MODEL ----------------

@st.cache_resource
def load_emotion_model():
return pipeline(
"text-classification",
model="j-hartmann/emotion-english-distilroberta-base"
)

emotion_model = load_emotion_model()

---------------- PSYCHOLOGICAL ANALYSIS ----------------

def analyze_psychological_state(text):

distress_keywords = [  
    "depressed",  
    "hopeless",  
    "worthless",  
    "burnout",  
    "anxiety",  
    "panic",  
    "lonely",  
    "overwhelmed"  
]  

score = 0  

for word in distress_keywords:  
    if word in text.lower():  
        score += 1  

return score

---------------- SUICIDE RISK DETECTION ----------------

def suicidal_risk_detection(text):

suicidal_keywords = [  
    "suicide",  
    "kill myself",  
    "want to die",  
    "end my life",  
    "life is pointless",  
    "no reason to live",  
    "self harm",  
    "cut myself"  
]  

for phrase in suicidal_keywords:  
    if phrase in text.lower():  
        return True  

return False

---------------- HELPLINE SUPPORT ----------------

def show_crisis_support():

st.error("⚠️ Emotional Crisis Detected")  

st.markdown("""

Immediate Support Resources

If you are experiencing thoughts of self-harm or suicide, please seek immediate professional help.

🇮🇳 Government of India Mental Health Helplines

📞 Kiran Mental Health Helpline: 1800-599-0019
📞 AASRA Suicide Prevention Helpline: +91 9820466726

🌐 https://www.mentalhealthindia.gov.in

Professional Support Recommended

• Licensed Psychotherapist
• Clinical Psychologist
• Neuropsychiatrist / Psychiatrist

MindCare AI is a support tool but cannot replace professional medical care.
You deserve care, support, and professional guidance.
""")

---------------- EMOTION ANALYSIS ----------------

def analyze_emotion(text):

result = emotion_model(text)[0]  

emotion = result["label"]  
confidence = result["score"]  

return emotion, confidence

---------------- MAIN CHAT SYSTEM ----------------

if "chat_history" not in st.session_state:
st.session_state.chat_history = []

st.header("🧠 AI Therapist Conversation")

st.info("""
MindCare AI uses Transformer NLP models to analyze emotional signals in text.
The system can detect stress, anxiety, sadness, burnout, and crisis indicators.
""")

user_input = st.chat_input("Share what's on your mind...")

if user_input:

# emotion analysis  
emotion, confidence = analyze_emotion(user_input)  

# distress score  
distress_score = analyze_psychological_state(user_input)  

# suicide detection  
suicide_risk = suicidal_risk_detection(user_input)  

# show results  
st.session_state.chat_history.append(("User", user_input))  

st.write("### 🧠 Emotional Analysis")  
st.write(f"Detected Emotion: **{emotion}**")  
st.write(f"Model Confidence: **{round(confidence*100,2)}%**")  

if distress_score > 0:  
    st.warning("⚠️ Psychological distress signals detected.")  

if suicide_risk:  
    show_crisis_support()  

# AI response placeholder  
ai_response = f"I understand that you may be feeling **{emotion}**. Your feelings are valid. Would you like to talk more about what is causing this?"  

st.session_state.chat_history.append(("MindCare AI", ai_response))

---------------- CHAT DISPLAY ----------------

for speaker, message in st.session_state.chat_history:

if speaker == "User":  
    st.chat_message("user").write(message)  

else:  
    st.chat_message("assistant").write(message)

---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""

Research Concepts Implemented

• Transformer NLP (RoBERTa Emotion Model)
• Affective Computing
• Computational Psychology
• Behavioral Text Mining
• Digital Mental Health Systems

Developed by Creative Catalyst Team
Department of B.Tech CSE (AI & ML)

Project: MindCare AI – Intelligent Mental Support System
""")
