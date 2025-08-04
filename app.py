from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {"name": "AI Chatbot", "description": "A chatbot using GPT APIs", "link": "#"},
    {"name": "Weather App", "description": "Fetches live weather data", "link": "#"},
    {"name": "Portfolio Site", "description": "Personal website built with Flask", "link": "#"}
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def project_list():
    return render_template("projects.html", projects=projects)

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
