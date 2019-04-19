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
    email = request.form['email']

    username_error = ''
    password_error = ''
    verifyPassword_error = ''
    email_error = ''
    space_char = ' '
    at_sign = '@'
    period = '.'
   
   

    if len(username) <= 0:
        
        username_error = 'Username must not be blank'
        # return render_template('username_form.html', username_error = username_error) 

    if verifyPassword != password:
        verifyPassword_error = 'Password does not match Verify Password'

    if len(password) <=0:

        password_error = 'Username must have more than 3 characters'   

    if len(password) <3 or len(password) >20:

        password_error = 'Password must be longer than 3 char and less than 20 char'     

    if len(verifyPassword) <3 or len(verifyPassword) >20:

        verifyPassword_error = 'Password must be longer than 3 char and less than 20 char'        

    if len(verifyPassword) <=0:

        verifyPassword_error = 'Password must have more than 3 characters'    

    if password.isspace():
        password_error = 'Password must not contain any spaces'

    if not at_sign in email and len(email) >=1:

        email_error = 'Email must contain @ sign'

    if not period in email and len(email) >=1:

        email_error = 'Email must contain a period'

    if space_char in email and len(email) >=1:

        email_error = 'Email must have no spaces' 

    if len(email) >= 1 and len(email) <3 or len(email) >20:
        email_error = 'Email must have more than 3 char and less than 20 char'
        
    
                   




     

            
        
        # return render_template('username_form.html', verifyPassword_error = verifyPassword_error, 
        # username = username)
    if not username_error and not password_error and not verifyPassword_error and not email_error:
        return redirect('/welcome')
    else:    
        return render_template('username_form.html', username_error=username_error,
                           password_error=password_error, verifyPassword_error=verifyPassword_error,
                           email_error=email_error)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


        

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