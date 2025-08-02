# -*- coding: utf-8 -*-
"""
Created on Wed May 14 01:04:52 2025

@author: HP
"""

import requests

print("🎓 Welcome to AdmissionBot via API")
print("Ask questions like: MBA, fees, courses, hostel, etc.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break

    try:
        # Send message to Flask API
        response = requests.post(
            "http://127.0.0.1:5000/chat",
            json={"message": user_input}
        )

        # Get reply from response
        bot_reply = response.json().get("reply", "No reply")
        print("Bot:", bot_reply)

    except Exception as e:
        print("Error connecting to server:", e)
        break
