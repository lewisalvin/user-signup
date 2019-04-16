from flask import Flask, request, redirect, render_template
import cgi
import os
#import jinja2

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
app = Flask(__name__)

app.config['DEBUG'] = True



# a form for adding username
     

# a form for adding password
       
      
# a form for verifying password
  


# a form for email
       

# submit button

@app.route('/validate-username')
def display_username_form():
    return render_template('username_form.html')


@app.route('/add', methods=['POST'])
def validate_username():

    username = request.form['username']
    password = request.form['password']
    verifyPassword = request.form['verifyPassword']

    username_error = ''
    password_error = ''
    verifyPassword_error = ''
    email_error = ''
    space_char = ''

    if len(username) <= 0:
        
        username_error = 'Username must not be blank'
        #return render_template('username_form.html', username_error = username_error) 
        


    if verifyPassword != password:
        verifyPassword_error = 'Password does not match Verify Password'
    return render_template('username_form.html', verifyPassword_error = verifyPassword_error, username = username)

    #if spaces(username) == True:
     #   username_error = 'Invalid username'

    

#def spaces(var):
 #   space = ''
    

 #   if space in var:
  #      return True




#@app.route('/validate-username')
#def display_password_form():
#    return add_password_form.format(password='', password_error='')

#@app.route('/validate-username')
#def display_verifyPassword_form():
#    return verify_password_form.format(verifyPassword='', verifyPassword_error='')  


#@app.route('/validate-username')
#def email_form():
#    return email_form.format(email='', email_error='')


#@app.route('/validate-username', methods=['POST'])
#def validate_username():

#    username = request.form['username']
#    password = request.form['password']

#    username_error = ''
#    password_error = ''












#@app.route('/valid-username')
#def valid_username():
#    return <h1>Welcome!  Thanks for signing up!</h1>     

app.run()