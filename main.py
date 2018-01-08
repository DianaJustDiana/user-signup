#Need to import request if using forms
#Need to import redirect if sending using to another page
#Need to import render_template if using simpler way to render templates

from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

"""Your assignment is simply to create a user signup form where users provide a username, password,
and, optionally, an email address. You must have an additional field to verify the password (the 
user must retype it exactly). Then you will validate the input and either redirect them to a welcome
page, or provide error information if any input is invalid."""

#Main page. User-signup form is displayed here. User submits and it goes 
#to /user-signup.html route.
@app.route("/", methods=['GET'])
def index():
    return render_template('user-signup.html')

#Comes from / route. Handler for results of user-signup.html form. Validates user input
#and goes to welcome.html route.
@app.route("/user-signup", methods=['POST'])
def user_signup():
    username = request.form['username']
    password = request.form['password']
    password_verify = request.form['password-verify']
    email = request.form['email']

    #Things to validate:
    #Fields can't be empty: username, password, verify password.
    #Email (if included) needs a single @, a single ., no spaces, 3-20 characters.
    #Password, password-verify must be 3-20 characters, no spaces.
    #Password and password-verify must match.

    #Use this on username.
    if len(username) == 0:
        username_blank_error = "Oops! You're too mysterious for me. This field can't be empty."
    else:
        username_blank_error = ""

    #Use this on password:
    if len(password) == 0:
        password_blank_error = "Oops! This field can't be empty. Please choose a password 3-20 characters long."
    else:
        password_blank_error = ""

    #Use this on password-verify:    
    if len(password_verify) == 0:
        password_verify_blank_error = "Oops! This field can't be empty. Please re-type the password you entered above."
    else:
        password_verify_blank_error = ""

    #Use this on password AND password-verify.
    if password != password_verify:
        passwords_must_match_error = "Whoops! These didn't match. Please try again."
        password = ""
        password_verify = ""
    else: 
        passwords_must_match_error = ""

    #Use this on password.
    if not 3 <= len(password) <= 20:
        password_wrong_length_error = "I'm sorry, but password must be 3-20 characters."
        password = ""
    else:
        password_wrong_length_error = ""

    if " " in password:
        password_no_space_error = "Hmm ... password can't contain a space."
        password = ""
    else:
        password_no_space_error = ""


    #Use this on email.
    if len(email) > 0:
    
        if "." not in email:
            email_needs_period_error = "Email address should contain one period (.) in it."
            email = ""
        else:
            email_needs_period_error = ""


        if "@" not in email:
            email_needs_at_symbol_error = "Email address should contain one @ in it."
            email = ""
        else:
            email_needs_at_symbol_error = ""


        if not 3 <= len(email) <= 20:
            email_wrong_length_error = "Email address must be 3-20 characters."
            email = ""
        else:
            email_wrong_length_error = ""

        if " " in email:
            email_cannot_have_space_error = "Hmm ... email address can't contain a space." 
            email = ""
        else:
            email_cannot_have_space_error = ""

        if not username_blank_error and not password_blank_error and not password_no_space_error and not password_verify_blank_error and not password_wrong_length_error and not passwords_must_match_error and not email_cannot_have_space_error and not email_needs_at_symbol_error and not email_needs_period_error and not email_wrong_length_error: 
            return redirect("/welcome")
        else:
            return render_template("/user-signup.html", username_blank_error=username_blank_error, password_blank_error=password_blank_error, password_no_space_error=password_no_space_error, password_verify_blank_error=password_verify_blank_error, password_wrong_length_error=password_wrong_length_error, passwords_must_match_error=passwords_must_match_error, email_cannot_have_space_error=email_cannot_have_space_error, email_needs_at_symbol_error=email_needs_at_symbol_error, email_needs_period_error=email_needs_period_error, email_wrong_length_error=email_wrong_length_error)


@app.route("/welcome", methods=['GET'])
def welcome():
    username = request.args.get('username')
    return render_template("welcome.html")

app.run()

    


