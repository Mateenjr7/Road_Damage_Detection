from flask import Flask, render_template, request, redirect, url_for, session, flash
from ultralytics import YOLO
import os
import uuid

app = Flask(__name__)
app.secret_key = 'secretkey'

# Upload and Result folders
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'

# Create folders if not exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

# Load YOLO model
model = YOLO('best.pt')

# Dummy user database
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
            return redirect(url_for('index'))
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
        flash("Registration successful. Please login.", 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully", 'info')
    return redirect(url_for('home'))

# ABOUT PAGE
@app.route('/about')
def about():
    return render_template('about.html')

# DETECTION PAGE
@app.route('/index', methods=['GET', 'POST'])
def index():

    if 'user' not in session:
        flash("Please login first", "warning")
        return redirect(url_for('login'))

    if request.method == 'POST':

        if 'image' not in request.files:
            flash('No image uploaded', 'warning')
            return redirect(request.url)

        file = request.files['image']

        if file.filename == '':
            flash('No image selected', 'warning')
            return redirect(request.url)

        # Generate unique filename
        filename = str(uuid.uuid4()) + ".jpg"

        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save uploaded image
        file.save(upload_path)

        # YOLO prediction
        results = model(upload_path)

        # Save result image
        result_path = os.path.join(app.config['RESULT_FOLDER'], filename)
        results[0].save(filename=result_path)

        # Extract predictions
        prediction_data = results[0].boxes.data.cpu().numpy()
        classes = results[0].names

        parsed_predictions = []

        for pred in prediction_data:
            x1, y1, x2, y2, conf, cls = pred

            parsed_predictions.append({
                "class": classes[int(cls)],
                "confidence": round(float(conf) * 100, 2)
            })

        return render_template(
            "index.html",
            uploaded=True,
            original=url_for('static', filename='uploads/' + filename),
            result=url_for('static', filename='results/' + filename),
            predictions=parsed_predictions
        )

    return render_template("index.html", uploaded=False)

# CHARTS PAGE
@app.route('/charts')
def charts():
    return render_template('charts.html')

# PERFORMANCE PAGE
@app.route('/performance')
def performance():
    return render_template('performance.html')

# RUN APP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)