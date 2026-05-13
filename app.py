from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import os
import uuid

app = Flask(__name__)
app.secret_key = 'secretkey'

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'

# Load YOLO model
model = YOLO('best.pt')

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

# Dummy user database (use SQLite or other DB for production)
users = {}

# HOME PAGE
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

# LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))  # Redirect to detection page
        else:
            flash('Invalid credentials', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

# REGISTER PAGE
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash("Passwords do not match", 'danger')
            return redirect(url_for('register'))
        if username in users:
            flash("Username already exists", 'danger')
            return redirect(url_for('register'))
        users[username] = password
        flash("Registration successful. Please log in.", 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully", 'info')
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

# DETECTION PAGE
@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'user' not in session:
        flash("Please login to access detection", "warning")
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No image file selected', 'warning')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No image selected', 'warning')
            return redirect(request.url)

        if file:
            filename = str(uuid.uuid4()) + ".jpg"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            results = model(filepath)
            result_image_path = os.path.join(app.config['RESULT_FOLDER'], filename)
            results[0].save(filename=result_image_path)

            prediction_data = results[0].boxes.data.cpu().numpy()
            classes = results[0].names
            parsed_preds = []

            for pred in prediction_data:
                x1, y1, x2, y2, conf, cls = pred
                parsed_preds.append({
                    "class": classes[int(cls)],
                    "confidence": round(float(conf) * 100, 2)
                })

            return render_template("index.html", uploaded=True,
                                   original=url_for('static', filename='uploads/' + filename),
                                   result=url_for('static', filename='results/' + filename),
                                   predictions=parsed_preds)

    return render_template("index.html", uploaded=False)

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/performance')
def performance():
    return render_template('performance.html')

# RUN
if __name__ == '__main__':
    app.run(debug=True)
