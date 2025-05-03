🎟️ UNESCO Ticket Booking Chatbot
A full-stack web application that allows users to book tickets for UNESCO World Heritage Sites using an AI-powered chatbot interface.

🌐 Live Demo


📌 Features
🔐 User Signup, Login & Logout with secure session handling

🤖 Chatbot interface for interacting with users

🧠 Natural Language Processing using OpenAI API

🎟️ Book tickets dynamically based on user messages

📜 View booking history after login

🌍 List available UNESCO World Heritage Sites

💾 SQLite database for persistent storage

🎨 Beautiful and responsive UI with HTML, CSS, and JavaScript

🛠️ Tech Stack
Category	Technologies Used
Backend	Python, Flask, SQLAlchemy
Frontend	HTML, CSS, JavaScript
Database	SQLite
AI/NLP	OpenAI GPT API
Data Format	JSON (for site data)
Tools	VS Code, Postman, Browser Dev Tools

📂 Project Structure
php
Copy
Edit
unesco_chatbot_ticketing/
│
├── app.py                  # Main Flask application
├── templates/              # HTML templates
│   ├── index.html
│   ├── login.html
│   └── signup.html
├── static/                 # CSS, JS files
│   ├── style.css
│   └── script.js
├── unesco_sites.json       # Data file with site names and descriptions
└── README.md               # Project documentation
🔧 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/unesco-chatbot-ticketing.git
cd unesco-chatbot-ticketing
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
Set your OpenAI API key (if using GPT-based responses):

bash
Copy
Edit
export OPENAI_API_KEY=your_api_key_here  # or set in app.py
Run the application:

bash
Copy
Edit
python app.py
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
📋 License
This project is licensed under the MIT License.
