#!/bin/bash
lsof -ti:8501 | xargs kill -9 2>/dev/null
cd /Users/willmanicom/StatsAutomator
streamlit run app.py &
sleep 2
open http://localhost:8501
osascript -e 'tell application "Terminal" to quit' &