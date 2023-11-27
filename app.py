from flask import Flask, request, render_template, flash, redirect, send_file, url_for,session, Response, render_template_string
from subjective import SubjectiveTest
import nltk
import pdfkit

app = Flask(__name__)

app.secret_key= 'aica2'

# first run these three lines of code
# import nltk
# nltk.download("all")
# exit()

from PyPDF2 import PdfFileReader, PdfReader
from flask import Flask, request

from pdfminer.high_level import extract_text


@app.route('/')
def index():
	return render_template('front.html')

@app.route('/predict')
def index1():
     return render_template('predict.html')

@app.route('/test_generate', methods=["POST"])
def test_generate():
    if 'pdf_file' not in request.files:
        return "No file part"

    pdf_file = request.files['pdf_file']
    if pdf_file.filename == '':
        return "No selected file"

    if pdf_file:
        pdf = PdfReader(pdf_file)
        text = ""

        for page in pdf.pages:
            text += page.extract_text()

    no_of_questions = 100

    try:
        subjective_generator = SubjectiveTest(text, no_of_questions)
        question_list = subjective_generator.generate_questions()
        return render_template('predict.html', cresults=question_list)

    except:
        flash('Error Occurred!')
        return redirect(url_for('/predict'))

@app.route("/generate")
def gen():
     return render_template('generate.html')

@app.route("/generatepdf", methods=['POST'])

def generate():
    if request.method == "POST":
    
        name = request.form['Name']
        email = request.form['Email']
        linkedin = request.form['LinkedIn']
        experience = request.form['Experience']
        graduation = request.form['Graduation']
        cpga = request.form['CGPA']
        university = request.form['University']
        skills = request.form['Skills']
        internship = request.form['Internship']
        achievements = request.form['Achievements']
        course1 = request.form['course1']
        course2 = request.form['course2']
        course3 = request.form['course3']
        projects = request.form['projects']

        html_content = f"""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume</title>
</head>
<body>
    <div class="container">
        <h1 style="font-size: 45px;">{name}</h1>
        <p>Email: {email}</p>
        <p>{linkedin}</p>
        <p>Experience: {experience} years</p>

        <hr style="height: 2px; background-color: #000; border: none; margin-top: 20px; margin-bottom: 20px;">

        <h2>Education</h2>
        <p>{graduation} - {university}</p>
        <p>CGPA - {cpga}</p>

        <hr style="height: 2px; background-color: #000; border: none; margin-top: 20px; margin-bottom: 20px;">

        <h2>Projects</h2>
        <p>{projects}</p>

        <hr style="height: 2px; background-color: #000; border: none; margin-top: 20px; margin-bottom: 20px;">

        <h2>Skills</h2>
        <p>{skills}</p>

        <hr style="height: 2px; background-color: #000; border: none; margin-top: 20px; margin-bottom: 20px;">

        <h2>Internships</h2>
        <p>{internship}</p>

        <hr style="height: 2px; background-color: #000; border: none; margin-top: 20px; margin-bottom: 20px;">

        <h2>Achievements</h2>
        <p>{achievements}</p>

        <hr style="height: 2px; background-color: #000; border: none; margin-top: 20px; margin-bottom: 20px;">

        <h2>Courses</h2>
        <p>{course1}</p>
        <p>{course2}</p>
        <p>{course3}</p>
    </div>
</body>
</html>

        """

        pdf_path = 'resume.pdf'
        pdfkit.from_string(html_content, pdf_path)
        return render_template('downloadpdf.html', pdf_path=pdf_path)
    return render_template('cantdownload.html')

if __name__ == "__main__":
	app.run(debug=True)







    
