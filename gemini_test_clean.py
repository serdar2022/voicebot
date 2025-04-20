import requests

api_key = "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"  # Your actual OpenRouter key

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "anthropic/claude-3-sonnet",
    "messages": [
        {"role": "user", "content": "Summarize this: Hello, this is a test from Iran."}
    ],
    "max_tokens": 1000  # 👈 safer token limit for free usage
}


response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
result = response.json()

if "error" in result:
    print("❌ API Error:", result["error"]["message"])
else:
    try:
        summary = result["choices"][0]["message"]["content"]
        print("✅ SUMMARY RESULT:\n", summary)
    except KeyError:
        print("❌ ERROR PARSING RESPONSE: 'choices'")
        print("FULL RAW JSON:\n", result)



