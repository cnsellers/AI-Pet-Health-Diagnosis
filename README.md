# 🐾 AI Pet Health Diagnosis

This is an AI-powered web app that helps diagnose pet health issues using **Google Gemini AI**. Users can **enter symptoms** or **upload pet images**, and the AI will provide potential health conditions.

## 🚀 Features
✅ **Text-Based Diagnosis** – Enter symptoms and get AI-generated health insights.  
✅ **Image-Based Analysis** – Upload an image of your pet’s condition for AI evaluation.  
✅ **Diagnosis History** – Stores past diagnoses for reference.  
✅ **Modern UI** – Interactive, user-friendly design.  

## 💻 Setup & Installation
1. Clone the repository:  
       git clone https://github.com/cnsellers/AI-Pet-Health-Diagnosis.git  
       cd AI-Pet-Health-Diagnosis
2. Install dependencies:
       Make sure you have Python 3.10+ installed, then run: pip install -r requirements.txt
3. Add your Gemini API Key:
       You'll need a Google Gemini AI API key to run the app.  
       1. Get your API key from [Google AI Studio](https://ai.google.dev/).  
       2. Open app.py and find this line: genai.configure(api_key="YOUR_OWN_KEY")  
       3. Replace "YOUR_OWN_KEY" with your actual Gemini API key.

## ▶️ Running the App
1. Run the Flask server: python app.py
2. Open your browser and go to: [http://127.0.0.1:5000/](https://ai.google.dev/)

## 🛠️ Technologies Used
* Flask – Backend API
* Google Gemini AI – AI-powered diagnosis
* SQLite – Stores past diagnoses
* JavaScript, HTML, CSS – Frontend

