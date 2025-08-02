# -*- coding: utf-8 -*-
"""
Created on Wed May 14 00:55:26 2025

@author: HP
"""
from flask import Flask, request, jsonify
import threading
import time
import requests

app = Flask(__name__)


def get_bot_reply(message):
    msg = message.lower()
    if "mba" in msg:
        return "Eligibility for MBA is a bachelor's degree with 50% and a valid entrance exam score."
    elif "b.tech" in msg:
        return "Eligibility for B.Tech is 12th with PCM and minimum 60% marks."
    elif "fees" in msg:
        return "Fees vary by program. For MBA, it's ₹2,00,000 per year."
    elif "courses" in msg:
        return "Courses: B.Tech, BBA, MBA, M.Tech, PhD."
    elif "hostel" in msg:
        return "Yes, hostel facilities are available for both boys and girls."
    elif "placement" in msg:
        return "We have excellent placement records with top companies like TCS, Infosys, and Wipro."
    elif "last date" in msg or "deadline" in msg:
        return "The last date to apply is July 31st, 2025."
    else:
        return "I can answer questions about courses, eligibility, fees, hostel, or placements."


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    reply = get_bot_reply(user_message)
    return jsonify({'reply': reply})


def run_flask():
    app.run(debug=True, use_reloader=False)


def run_client():
    time.sleep(1)  
    print("🎓 Welcome to AdmissionBot via API")
    print("Ask questions like: MBA, fees, courses, hostel, etc.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break

        try:
           
            response = requests.post(
                "http://127.0.0.1:5000/chat",
                json={"message": user_input}
            )

            
            bot_reply = response.json().get("reply", "No reply")
            print("Bot:", bot_reply)

        except Exception as e:
            print("Error connecting to server:", e)
            break


def main():
    
    server_thread = threading.Thread(target=run_flask)
    client_thread = threading.Thread(target=run_client)

    
    server_thread.start()
    client_thread.start()

    
    server_thread.join()
    client_thread.join()


if __name__ == '__main__':
    main()

