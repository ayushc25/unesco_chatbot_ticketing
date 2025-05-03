from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import json
import openai

app = Flask(__name__)
app.secret_key = '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'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///unesco_chatbot.db'
db = SQLAlchemy(app)

# OpenAI API Key
openai.api_key = 'your-openai-api-key-here'  # 🔥 Replace with your actual API Key

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(200), nullable=False)
    user = db.Column(db.String(150), nullable=False)

# Load UNESCO sites from local JSON
with open('unesco_sites.json', encoding='utf-8') as f:
    unesco_sites_data = json.load(f)
unesco_sites = unesco_sites_data['sites']

# Routes
@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    bookings = Booking.query.filter_by(user=session['user']).all()
    return render_template('index.html', bookings=bookings)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        if User.query.filter_by(username=username).first():
            return "⚠️ User already exists."

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_input = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password_input):
            session['user'] = user.username
            return redirect(url_for('index'))
        return "❌ Invalid credentials."

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/chat', methods=['POST'])
def chat():
    if 'user' not in session:
        return jsonify({'response': '⚠️ Please login to book tickets.'})

    data = request.get_json()
    user_input = data.get('message', '').lower()

    # Show list of UNESCO sites
    if "list sites" in user_input or "available sites" in user_input:
        sites_list = ', '.join(site['name'] for site in unesco_sites)
        return jsonify({'response': f"📍 Available Sites: {sites_list}"})

    # Book a ticket
    elif "book ticket" in user_input or "book tickets" in user_input:
        for site in unesco_sites:
            if site['name'].lower() in user_input:
                booking = Booking(site_name=site['name'], user=session['user'])
                db.session.add(booking)
                db.session.commit()
                return jsonify({'response': f"🎟️ Ticket booked for {site['name']}!"})
        return jsonify({'response': "❌ Sorry, I couldn't find that site. Try 'List Sites' first."})

    # Show user's bookings
    elif "show my bookings" in user_input or "my bookings" in user_input:
        user_bookings = Booking.query.filter_by(user=session['user']).all()
        if user_bookings:
            bookings_text = ', '.join(booking.site_name for booking in user_bookings)
            return jsonify({'response': f"📝 Your Bookings: {bookings_text}"})
        else:
            return jsonify({'response': "🛑 You have no bookings yet."})

    # If user says something random (like 'how's the weather')
    else:
        return jsonify({'response': "🤖 I can help you book UNESCO site tickets! Try typing: 'List sites' or 'Book ticket for Taj Mahal'."})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
