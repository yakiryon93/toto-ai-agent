import os
import google.generativeai as genai
import json
from datetime import datetime

# הגדרת ה-AI
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def analyze_and_predict():
    prompt = "אתה מומחה AI לטוטו. סקור את משחקי ליגת העל הקרובים (דגש על ביתר ירושלים), תן עדכון קצר והימור ל-3 משחקים מרכזיים בעברית."
    try:
        response = model.generate_content(prompt)
        # יצירת האובייקט עם המידע
        new_data = {
            "time": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "analysis": response.text
        }
        
        # שמירה לקובץ בתיקייה הראשית
        with open('agent_memory.json', 'w', encoding='utf-8') as f:
            json.dump([new_data], f, ensure_ascii=False, indent=4)
        print("Success: Memory updated!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_and_predict()
