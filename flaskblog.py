from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] ='3a4dc33f5c7a3b772f03800d2b3ecf98'

posts = [

        {
            'author':'Dog',
            'title':'Lost Bone',
            'content':'First post content',
            'date posted':'17-Dec-2020'
        },        
        {
            'author':'Cat',
            'title':'Lost Fish',
            'content':'Second post content',
            'date posted':'18-Dec-2020'
        }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts = posts)


@app.route('/about')
def about():
    return render_template('about.html',title = 'ABT')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))

    return render_template('register.html',title = 'Register', form = form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'dog@123.com' and form.password.data == '12345':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password','danger')

    return render_template('login.html',title = 'Login', form = form)



if __name__ == '__main__':
    app.run(debug=True)