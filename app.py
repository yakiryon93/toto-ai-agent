import streamlit as st
import json
import os

st.title("⚽ סוכן הטוטו של יקיר")
if os.path.exists('agent_memory.json'):
    with open('agent_memory.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        if data:
            st.info(f"📅 עדכון: {data[0]['time']}")
            st.markdown(data[0]['analysis'])
