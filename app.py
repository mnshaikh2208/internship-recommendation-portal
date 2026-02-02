from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    skills = request.form.get("skills", "").lower()
    interest = request.form.get("interest", "").lower()

    internships = [
        {
            "title": "Python Developer Intern",
            "company": "Infosys",
            "location": "Remote",
            "stipend": "₹10,000 / month",
            "skills": ["python", "flask", "backend"],
            "interest": ["software", "backend"],
            "desc": "Work on backend systems using Python and Flask.",
            "url": "https://www.infosys.com/careers"
        },
        {
            "title": "Web Developer Intern",
            "company": "TCS",
            "location": "Mumbai",
            "stipend": "₹8,000 / month",
            "skills": ["html", "css", "javascript", "web"],
            "interest": ["frontend", "ui"],
            "desc": "Build responsive websites and UI components.",
            "url": "https://www.tcs.com/careers"
        },
        {
            "title": "Data Analyst Intern",
            "company": "Deloitte",
            "location": "Bangalore",
            "stipend": "₹12,000 / month",
            "skills": ["python", "sql", "data"],
            "interest": ["data", "analysis"],
            "desc": "Analyze datasets and generate business insights.",
            "url": "https://www2.deloitte.com/careers"
        },
        {
            "title": "Machine Learning Intern",
            "company": "Microsoft",
            "location": "Hyderabad",
            "stipend": "₹15,000 / month",
            "skills": ["python", "ml", "machine learning"],
            "interest": ["ml", "ai"],
            "desc": "Train ML models and work on AI-driven solutions.",
            "url": "https://careers.microsoft.com"
        },
        {
            "title": "Cloud Computing Intern",
            "company": "Amazon AWS",
            "location": "Remote",
            "stipend": "₹14,000 / month",
            "skills": ["aws", "cloud", "docker"],
            "interest": ["cloud", "devops"],
            "desc": "Assist in cloud infrastructure and deployment tasks.",
            "url": "https://www.amazon.jobs"
        }
    ]

    recommendations = []

    for internship in internships:
        score = 0

        for skill in internship["skills"]:
            if skill in skills:
                score += 2

        for intr in internship["interest"]:
            if intr in interest:
                score += 1

        if score > 0:
            internship["score"] = score
            recommendations.append(internship)

    recommendations = sorted(
        recommendations,
        key=lambda x: x["score"],
        reverse=True
    )

    if not recommendations:
        recommendations = [{
            "title": "General Software Intern",
            "company": "Tech Company",
            "location": "Remote",
            "stipend": "Unpaid",
            "desc": "Explore various domains of software development.",
            "url": "#"
        }]

    return render_template("result.html", recommendations=recommendations)


if __name__ == "__main__":
    app.run(debug=True)


