import os
import google.generativeai as genai

# Step 1: Try a port like 5556, 10809, etc.
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10808'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10808'

# Step 2: Set your Gemini API key
genai.configure(api_key="AIzaSyC2jtGVDKW2tonJJN4aodHmeVZga1KYJoA")

# Step 3: Test summarization
try:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("Summarize this text: Hello, this is a test from Iran.")
    print("✅ SUCCESS:\n", response.text)
except Exception as e:
    print("❌ ERROR:", e)
