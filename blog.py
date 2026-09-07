from flask import Flask, render_template, url_for, flash, redirect
from forms import Registration_Form, Login_Form
app = Flask(__name__) #special variable in python that is the name of the module

app.config['SECRET_KEY'] = '3192e70280e26652984eaf747a84d6d2'

# List of dictionaries that represents a single blog post
posts = [
    {
        'author' : 'abdul mueed booley',
        'title' : 'Blog post 1',
        'date_posted' : '6 september 2026',
        'content' : '1st blog post'
    },
    {
        'author' : 'nala booley',
        'title' : 'Blog post 2',
        'date_posted' : '7 september 2026',
        'content' : '2nd blog post'
    }

]
# Home page route
@app.route("/")
@app.route("/home") # Route decorator
def home():
    return render_template('home.html', posts=posts, title='Home') # Import render template function from flask

# About page route
@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration_Form()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # name of home page function
    return render_template('register.html', title='register', form=form)

@app.route("/login")
def login_form():
    form = Login_Form()
    return render_template('login.html', title='Login', form=form)

# So flask knows where to look for static and template files
# This condition is only true if the script is ran directly
if __name__ == '__main__':
    app.run(debug=True)
