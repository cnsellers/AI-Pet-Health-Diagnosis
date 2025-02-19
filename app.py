from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
from PIL import Image
import io
import datetime
import sqlite3

app = Flask(__name__)

# Set up Google Gemini API Key
genai.configure(api_key="YOUR_OWN_KEY")  # Replace with your OWN Gemini API key

# Initialize database
def init_db():
    with sqlite3.connect("diagnoses.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS diagnoses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symptoms TEXT,
                image BLOB,
                diagnosis TEXT,
                timestamp TEXT
            )
        """)
        conn.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose_pet():
    symptoms = request.form.get('symptoms', '')
    image = request.files.get('image')
    image_data = None
    
    # Ensure there is always a text parameter
    if not symptoms:
        symptoms = "Analyze the provided image for any visible pet health issues."

    inputs = [symptoms]

    if image:
        img = Image.open(image)
        img = img.convert("RGB")
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        image_bytes = buffered.getvalue()

        # Properly format image data for Gemini
        image_data = {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }

        inputs.append(image_data)  # Append image data directly to input list

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(inputs)  # Ensure correct format: list of text + images

        diagnosis = response.text.strip()

        # Store in database
        with sqlite3.connect("diagnoses.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO diagnoses (symptoms, image, diagnosis, timestamp) VALUES (?, ?, ?, ?)",
                           (symptoms, image_bytes if image else None, diagnosis, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()

        return jsonify({"diagnosis": diagnosis})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/history')
def history():
    with sqlite3.connect("diagnoses.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT symptoms, diagnosis, timestamp FROM diagnoses ORDER BY timestamp DESC LIMIT 10")
        diagnoses = cursor.fetchall()
    return render_template("history.html", diagnoses=diagnoses)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
