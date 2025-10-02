from flask import Flask, render_template, request, redirect, url_for, flash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "replace_this_with_a_random_secret"  # for flash messages

# Path to store contact messages
MESSAGES_FILE = os.path.join(os.path.dirname(__file__), "messages.txt")

@app.route("/")
def index():
    # You can pass data to template (projects, skills, etc.)
    projects = [
        {"title": "Employee Management System", "desc": "Django + MySQL project"},
        {"title": "E-commerce Project", "desc": "Full stack e-commerce demo"},
        {"title": "School Management System", "desc": "Admin panel & reports"}
    ]
    skills = ["Python", "Django", "HTML", "CSS", "JavaScript", "SQL"]
    return render_template("index.html", projects=projects, skills=skills)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # Basic validation
        if not name or not email or not message:
            flash("Please fill all fields.", "error")
            return redirect(url_for("contact"))

        # Save the message to a file (simple persistence)
        entry = f"{datetime.now().isoformat()} | {name} | {email} | {message}\n"
        with open(MESSAGES_FILE, "a", encoding="utf-8") as f:
            f.write(entry)

        flash("Thank you! Your message has been received.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
