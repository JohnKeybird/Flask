from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/touppercase')
def touppercase():
    return render_template('touppercase.html')

@app.route('/areaOfCircle')
def areaOfCircle():
    return render_template('areaOfCircle.html')

@app.route('/areaOfTriangle')
def areaOfTriangle():
    return render_template('areaOfTriangle.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/works')
def works():
    return render_template('works.html')

if __name__ == "__main__":
    app.run(debug=True)
