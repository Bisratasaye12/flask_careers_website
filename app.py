from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {"id": 1, "title": "Software Engineer", "location": "San Francisco, CA", "salary": "$120,000"},
    {"id": 2, "title": "Data Scientist", "location": "New York, NY", "salary": "$110,000"},
    {"id": 3, "title": "Backend Developer", "location": "Austin, TX", "salary": "$105,000"},
    {"id": 4, "title": "Frontend Developer", "location": "Seattle, WA", "salary": "$100,000"},
    {"id": 5, "title": "DevOps Engineer", "location": "Chicago, IL", "salary": "$115,000"},
    {"id": 6, "title": "Product Manager", "location": "Boston, MA", "salary": "$130,000"},
    {"id": 7, "title": "UX Designer", "location": "Los Angeles, CA", "salary": "$90,000"},
    {"id": 8, "title": "Full Stack Developer", "location": "Denver, CO", "salary": "$108,000"},
    {"id": 9, "title": "Machine Learning Engineer", "location": "San Jose, CA", "salary": "$125,000"},
    {"id": 10, "title": "Cybersecurity Analyst", "location": "Washington, D.C.", "salary": "$95,000"}
]


@app.route("/")
def hello():
    return render_template('index.html', jobs= jobs)



if __name__ == "__main__":
    app.run("0.0.0.0", debug= True)