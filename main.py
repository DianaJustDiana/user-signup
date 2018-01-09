from flask import Flask, request, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

"""Your assignment is simply to create a user signup form where users provide a username, password,
and, optionally, an email address. You must have an additional field to verify the password (the 
user must retype it exactly). Then you will validate the input and either redirect them to a welcome
page, or provide error information if any input is invalid."""

#Main page. User-signup form is displayed here. User submits and it goes 
#to /user-signup.html route.
@app.route('/', methods=['GET'])
def index():
    return render_template('signup.html')

#Comes from / route. Handler for results of user-signup.html form. Validates user input
#and goes to welcome.html route.
@app.route('/', methods=['GET', 'POST'])
def validate_input():
    username = request.form['username']
    username_error = ""

    password = request.form['password']
    password_error = ""
    
    password_verify = request.form['password-verify']
    password_verify_error = ""

    email = request.form['email']
    email_error = ""

    #Things to validate:
    #Fields can't be empty: username, password, verify password.
    #Email (if included) needs a single @, a single ., no spaces, 3-20 characters.
    #Password, password-verify must be 3-20 characters, no spaces.
    #Password and password-verify must match.

    #Use this on username.
    if len(username) == 0:
        username_error = "Oops! You're too mysterious for me. This field can't be empty."

    #Use this on password:
    if len(password) == 0:
        password_error = "Oops! This field can't be empty. Please choose a password 3-20 characters long."
    if not 3 <= len(password) <= 20:
        password_error = "I'm sorry, but password must be 3-20 characters."  
    if " " in password:
        password_error = "Hmm ... password can't contain a space."

    #Use this on password-verify.
    if password != password_verify:
        passwords_verify_error = "Whoops! These didn't match. Please try again."
   
    #Use this on email.
    if len(email) > 0:
    
        if "." not in email:
            email_error = "Email address should contain one period (.) in it."
        if "@" not in email:
            email_error = "Email address should contain one @ in it."
        if not 3 <= len(email) <= 20:
            email_error = "Email address must be 3-20 characters."
        if " " in email:
            email_error = "Hmm ... email address can't contain a space." 
            
    if not username_error and not password_error and not password_verify_error and not email_error: 
        return render_template('welcome.html', username=username)
    else:
        return render_template('signup.html', username=username, email=email, username_error=username_error, password_error=password_error, password_verify_error=password_verify_error, email_error=email_error)


#@app.route('/welcome', methods=['GET'])
#def welcome():
#    username = request.args.get('username')
#    return render_template('welcome.html', username=username)

app.run()

    


