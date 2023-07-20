from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    # Retrieve form data
    
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    summary=request.form['summary']
    education=request.form['education']
    experience=request.form['experience']
    hobbies=request.form['hobbies']

    # Generate the resume (example: store the data in a dictionary)
    resume_data = {
        'name': name,
        'email': email,
        'phone': phone,
        'summary':summary,
        'education':education,
        'experience':experience,
        'hobbies':hobbies
                
    }

    # Render the resume template with the generated data
    return render_template('resume.html', resume_data=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
