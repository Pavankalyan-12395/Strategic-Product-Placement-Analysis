"""
=============================================================
  SALES — Strategic Product Placement Analysis
  Python Flask Web Server
  Author : E. Pavan Kalyan
  Email  : pavan9010044875@gmail.com
  Location: Sarojini Nagar, KADAPA - 516002
=============================================================

HOW TO RUN:
  1. Install dependencies:
       pip install flask

  2. Make sure this file is in the SAME folder as:
       index.html
       styles.css
       theme-gold.css      (or whichever theme you chose)

  3. Run the server:
       python app.py

  4. Open in browser:
       http://localhost:5000

  FOLDER STRUCTURE:
  project/
  ├── app.py              ← this file
  ├── index.html
  ├── styles.css
  ├── theme-gold.css
  ├── theme-blue.css
  ├── theme-purple.css
  └── theme-crimson.css
=============================================================
"""

from flask import Flask, send_from_directory, jsonify, request
import os

# ── App setup ──────────────────────────────────────────────
app = Flask(__name__, static_folder='.', template_folder='.')

# Directory where all your website files live
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ── Routes ─────────────────────────────────────────────────

@app.route('/')
def home():
    """Serve the main HTML page."""
    return send_from_directory(BASE_DIR, 'index.html')


@app.route('/<path:filename>')
def static_files(filename):
    """Serve CSS, JS, images, and any other static files."""
    return send_from_directory(BASE_DIR, filename)


@app.route('/contact', methods=['POST'])
def contact():
    """
    Handle contact form submissions.
    Receives JSON: { name, email, subject, message }
    Extend this to send email via smtplib or store in a database.
    """
    data = request.get_json(silent=True) or request.form.to_dict()

    name    = data.get('name', '').strip()
    email   = data.get('email', '').strip()
    subject = data.get('subject', '').strip()
    message = data.get('message', '').strip()

    # Basic validation
    if not name or not email or not message:
        return jsonify({'status': 'error', 'msg': 'Name, email and message are required.'}), 400

    # ── TODO: Replace this block with real email sending ──────
    # Example using smtplib (Gmail):
    #
    # import smtplib
    # from email.mime.text import MIMEText
    #
    # sender   = "your_gmail@gmail.com"
    # password = "your_app_password"         # use Gmail App Password
    # receiver = "pavan9010044875@gmail.com"
    #
    # body = f"From: {name} <{email}>\nSubject: {subject}\n\n{message}"
    # msg  = MIMEText(body)
    # msg['Subject'] = subject or 'New Contact Form Submission'
    # msg['From']    = sender
    # msg['To']      = receiver
    #
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #     smtp.login(sender, password)
    #     smtp.send_message(msg)
    # ──────────────────────────────────────────────────────────

    # For now, just log the submission
    print(f"\n📩 New Contact Submission")
    print(f"   Name   : {name}")
    print(f"   Email  : {email}")
    print(f"   Subject: {subject}")
    print(f"   Message: {message}\n")

    return jsonify({'status': 'success', 'msg': 'Message received!'})


@app.route('/health')
def health():
    """Simple health check endpoint."""
    return jsonify({'status': 'ok', 'server': 'SALES — E. Pavan Kalyan'})


# ── Run ────────────────────────────────────────────────────
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'true').lower() == 'true'

    print("=" * 55)
    print("  SALES — Strategic Product Placement Analysis")
    print(f"  Server running at: http://localhost:{port}")
    print(f"  Author: E. Pavan Kalyan")
    print(f"  Debug mode: {debug}")
    print("=" * 55)

    app.run(host='0.0.0.0', port=port, debug=debug)