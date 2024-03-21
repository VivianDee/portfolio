from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_info')
def get_info():
    section = request.args.get('section').lower()
    # Call the appropriate function based on the section
    result = ""
    if section in ["intro", "1"] :
        result = intro()
    elif section in ["experience", "2"]:
        result = experience()
    elif section in ["education", "3"]:
        result = education()
    elif section in ["skills", "4"]:
        result = skills()
    elif section in ["projects", "5"]:
        result = projects()
    elif section in ["interests", "6"]:
        result = interests()
    return result

def intro():
    return """
<div>--- Intro ---</div>
<div>I am deeply passionate about coding and obsessed with delivering exceptional software solutions.
I strive to write clean, maintainable, and efficient code that exceeds expectations.</div>

<div>If you were to ask me to describe myself, I would say I am someone who is always thinking outside the box.
I will always find an easier yet efficient way to do things, even when those things are said to be impossible.
I thrive when faced with doubt and succeed despite hardships. And when I commit to a task, I don't give up until I get it done.</div>

<div>In my free time, I indulge in reading books, conducting research, and learning new things.
I also write articles on Medium about the psychology and workings of the mind, which is a topic that fascinates me.</div>

<div>Overall, I approach both my personal and professional life with a commitment to excellence and a passion for making a positive impact.
I am excited to see where this drive takes me and to be a part of projects that challenge and inspire me.</div>
"""

def experience():
    return """
--- Experience ---<br>
Backend Developer Intern<br>
TechProsNaijia<br>
11/2023 - 12/2023<br>
<br>- Developed a Wordpress plugin to sync data between EDD and MailerLite.<br>
- Designed and implemented EDD secure checkout, sign up, login in, orders, and downloads custom pages.<br>
- WordPressed a site from provided frontend designs.<br>
- Implemented Git for version control across the company.<br>
"""

def education():
    return """
--- Education ---<br>
Chemistry / Bachelor of Science<br>
Second Class Upper<br>
University of Benin<br>
09/2017 - 12/2021<br>
ALX Full Stack Software Engineering<br>
ALX Africa<br>
02/2023 - 02/2024<br>
"""

def skills():
    return """
--- Skills ---<br>
Backend Development: Flask Django Node.js Express Framework RESTful API<br>
Others: Ubuntu, Windows, Unittest and Shell scripting for automation<br>
Server Administration: Ubuntu Server<br>
Version Control: Git<br>
Programming: Python JavaScript f PHP<br>
Web Server Administration: Docker Nginx Haproxy<br>
Database: SQL MySQL<br>
Frontend Development: HTML CSS<br>
"""

def projects():
    return """
--- Projects ---<br>
AirBnB Clone Project<br>
TechProsNaija Backend Team Project<br>
Custom _printf() Function and Simple Shell Project in C<br>
Responsive Websites Development<br>
Cash Register & Caesars Cipher<br>
"""

def interests():
    return """
--- Interests ---<br>
Volunteering,<br> Programming,<br> Research, <br>Reading & Writing
"""

if __name__ == '__main__':
    app.run(debug=True)
