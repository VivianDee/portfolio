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
    elif section in ["chat", "7"]:
        result = chat()
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
PHP Laravel Developer<br>                                       
Bakkaz Information And Technology, Nigeria 
<br>05/2024 - present<br>

- Developed Laravel-based microservices to enhance key functionalities for Authentication,  payments, advertisements, and user preferences across multiple applications, significantly reducing app development time.<br>
-Enhanced code maintainability and scalability by allowing independent updates to each microservice, thereby reducing the probability of Single Point of Failure (SPOF) .<br>
- Collaborated with a team of frontend and backend developers, designers and a project manager to ensure seamless app development.<br>
- Contributed to the DevOps process by selecting Vultr as the hosting platform and managing the server using Laravel Forge, enhancing security, reliability, and resource management for hosted microservices.<br>
- Engaged in regular code reviews and knowledge-sharing sessions with the team, fostering a culture of continuous learning and improvement.<br>
<br><br>
Software Engineer<br>                                       
BEMA Integrated Services, Nigeria
<br>01/2024 - 05/24<br>

- Developed a Wordpress plugin to sync data between EDD and MailerLite, creating a customer relationship model.<br>
- Customized Easy Digital Downloads Plugin.<br>
- Collaborated with frontend and designers to create the backend of a custom WordPress theme from provided designs, showcasing proficiency in WordPress development.<br>
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
<br>Programming: PHP Python JavaScript <br>
<br>Backend Development: Laravel Flask Django<br>
<br>Frontend Development: HTML CSS<br>
<br>Database: SQL MySQL SQLAlchemy SQLite ERDL<br>
<br>Web Server Administration: Nginx HAProxy Gunicorn Docker  SSH  cPanel  SSL<br>
<br>Version Control: Git Github<br>
<br>API Development and Integration: RESTful APIs Integration of third-party APIs Postman<br>
<br>Others: CI/CD  TDD   Unit Testing   Code Reviews<br>
"""

def projects():
    return """
--- Projects ---<br>
<a class="project" href="https://www.recenthpost.com/home" target="_blank">Recenth Posts<br></a>
<a class="project" href="https://github.com/VivianDee/Bakkaz" target="_blank">Authentication MicroService<br></a>
<a class="project" href="https://github.com/VivianDee/Bakkaz" target="_blank">Ads MicroService<br></a>
<a class="project" href="https://github.com/VivianDee/Bakkaz" target="_blank">Payment MicroService<br></a>
<a class="project" href="https://github.com/VivianDee/Bakkaz" target="_blank">User Preferences MicroService<br></a>
<a class="project" href="https://techprosnaija.com" target="_blank">TechProsNaija Backend Team Project<br></a>
<a class="project" href="https://github.com/VivianDee/AirBnB_clone_v4"  target="_blank">AirBnB Clone Project<br></a>
<br>
"""

def interests():
    return """
--- Interests ---<br>
Volunteering,<br> Programming,<br> Research, <br>Reading & Writing
"""

def chat():
    return """
    <div class="chatbox"><iframe
    src="https://www.chatbase.co/chatbot-iframe/nT8oEBgwYQx58HuWpipqH"
    title="Vee"
    width="100%"
    style="height: 400px; padding: 10px"
    frameborder="0"
    ></iframe>
    </div>
    <br>
    """

if __name__ == '__main__':
    app.run(debug=True)
