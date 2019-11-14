from flask import Flask, render_template
app = Flask(__name__)

student_list = []


@app.route('/')
def index():
    name = request.args.get('name')
    return render_template('index.html', name=name)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        student_list.append(name)
        return render_template("index.html", students=student_list)
    return "register"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
