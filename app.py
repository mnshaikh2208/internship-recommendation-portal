from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    skills = request.form.get("skills", "")
    interest = request.form.get("interest", "")

    recommendations = []

    if "python" in skills.lower():
        recommendations.append("Python Developer Intern")
    if "java" in skills.lower():
        recommendations.append("Java Developer Intern")
    if "web" in skills.lower() or "html" in skills.lower():
        recommendations.append("Web Developer Intern")
    if "data" in interest.lower():
        recommendations.append("Data Analyst Intern")
    if "ml" in interest.lower():
        recommendations.append("Machine Learning Intern")

    return render_template("result.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
