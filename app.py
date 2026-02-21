import streamlit as st
import json
import os

st.set_page_config(page_title="סוכן הטוטו של יקיר", page_icon="⚽")

st.title("⚽ סוכן הטוטו של יקיר")

# בדיקה אם הקובץ קיים בנתיב הנוכחי
if os.path.exists('agent_memory.json'):
    with open('agent_memory.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        if data and len(data) > 0:
            latest = data[0]
            st.success(f"📅 עדכון אחרון: {latest['time']}")
            st.markdown(latest['analysis'])
        else:
            st.warning("הקובץ קיים אבל הוא ריק. מריץ עדכון...")
else:
    st.error("הסוכן עדיין לא יצר את קובץ הזיכרון. וודא שהרצת את ה-Action ב-GitHub.")
