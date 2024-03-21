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
    else:
        result = "Invalid Command<br>"
    return result

def intro():
    return """
--- Intro ---<br>
I am deeply passionate about coding and obsessed with delivering exceptional software solutions.
I strive to write clean, maintainable, and efficient code that exceeds expectations.<br>

If you were to ask me to describe myself, I would say I am someone who is always thinking outside the box.
I will always find an easier yet efficient way to do things, even when those things are said to be impossible.
I thrive when faced with doubt and succeed despite hardships. And when I commit to a task, I don't give up until I get it done.<br>

In my free time, I indulge in reading books, conducting research, and learning new things.
I also write articles on Medium about the psychology and workings of the mind, which is a topic that fascinates me.<br>

Overall, I approach both my personal and professional life with a commitment to excellence and a passion for making a positive impact.
I am excited to see where this drive takes me and to be a part of projects that challenge and inspire me.<br>
"""

def experience():
    return """
--- Experience ---<br>
Software Engineer<br>                                       
BEMA<br>
01/2024 - present<br>

- Developed a Wordpress plugin to sync data between EDD and MailerLite, creating a customer relationship model.<br>
- Designed and implemented EDD secure checkout, sign up, login in, orders, and downloads custom pages for improved user experience.<br>
- WordPressed a site from provided frontend designs, showcasing proficiency in WordPress development.<br>
- Quickly became the go-to person for information within a month of joining the startup company, highlighting effective collaboration and quick learning.<br>
- Implemented Git for version control across the company, providing training sessions for team members, including the CEO.<br>
<br><br>
TechProsNaijia<br>
11/2023 - 12/2023<br>
<br>- Gained hands-on experience with Node.js, Express, MySQL and knex.js.<br>
- Hosted the backend application on the server and resolved a critical server issue saving the company significant time and money.<br>
"""

def education():
    return """
--- Education ---<br>
ALX Africa<br>
02/2023 - 02/2024<br>
ALX Full Stack Software Engineering<br>
<br>freeCodeCamp<br>
05/2022 -  03/2023<br>
JavaScript Algorithms and Data Structures<br>
Responsive Web Design<br>
<br>University of Benin<br>
09/2017 - 12/2021<br>
Chemistry / Bachelor of Science<br>
Second Class Upper<br>
"""

def skills():
    return """
--- Skills ---<br>
<br>Programming: Python JavaScript PHP<br>
<br>Backend Development: Flask Django Node.js Express Framework RESTful API<br>
<br>Frontend Development: HTML CSS<br>
<br>Database: SQL MySQL<br>
<br>Web Server Administration: Docker Nginx Haproxy<br>
<br>Version Control: Git<br>
<br>Server Administration: Ubuntu Server<br>
<br>Others: Ubuntu, Windows, Unittest and Shell scripting for automation<br>
"""

def projects():
    return """
--- Projects ---<br>
<a class="project" href="https://github.com/VivianDee/AirBnB_clone"  target="_blank">AirBnB Clone Project<br></a>
<a class="project" href="https://techprosnaija.com" target="_blank">TechProsNaija Backend Team Project<br></a>
<a class="project" href="https://github.com/VivianDee/printf" target="_blank">Custom _printf() Function<br></a>
<a class="project" href="https://github.com/VivianDee/simple_shell"  target="_blank">Simple Shell Project in C<br></a>
<a class="project" href="https://www.freecodecamp.org/certification/fccb57bc24d-114f-484e-83d9-dad32eb6684c/responsive-web-design" target="_blank">Responsive Websites Development<br></a>
<a class="project" href="https://www.freecodecamp.org/certification/fccb57bc24d-114f-484e-83d9-dad32eb6684c/javascript-algorithms-and-data-structures" target="_blank">Cash Register & Caesars Cipher<br></a><br>
"""

def interests():
    return """
--- Interests ---<br>
Volunteering,<br> Programming,<br> Research, <br>Reading & Writing
"""

if __name__ == '__main__':
    app.run(debug=True)
