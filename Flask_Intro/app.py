from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaofcircle', methods=['GET', 'POST'])
def works2():
    result = None
    if request.method == 'POST':
        input_radius = request.form.get('radius', '')
        result = 3.14 * (float(input_radius) ** 2)
    return render_template('areaofcircle.html', result=result)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def works3():
    result = None
    if request.method == 'POST':
        input_base = request.form.get('base', '')
        input_height = request.form.get('height', '')
        result = 0.5 * float(input_base) * float(input_height)
    return render_template('areaoftriangle.html', result=result)

@app.route('/contact')
def contact():
    return "Contact Page. please create me an html page with dummy contact info"

if __name__ == "__main__":
    app.run(debug=True)
