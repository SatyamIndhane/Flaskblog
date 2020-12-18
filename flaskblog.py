from flask import Flask, render_template
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)