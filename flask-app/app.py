from flask import Flask, render_template, redirect, url_for, flash
from users import users
from forms import ContactForm
from flask_frozen import Freezer

app = Flask(__name__)
app.secret_key = 'BlHDg8mcJX'

@app.route('/')
def hello_world():
    username = 'John Doe'
    return render_template('index.html', username=username)

@app.route('/about')
def about():
    return render_template('about.html', team_members=users)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        # process the form data
        print(f'Name: {name}, Email: {email}, Message: {message}')
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

# Configuration for Frozen-Flask
app.config['FREEZER_DESTINATION'] = 'build' # Directory where static files will be generated
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze() # Freezes the app to generate static files