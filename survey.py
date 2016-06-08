from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/results', methods=['POST'])
def ninja():

    name = request.form['name']
    location = request.form['location']
    language = request.form['location']
    comment = request.form['comment']
    return render_template('result.html', username=name, user_loc=location, user_lang=language, user_comment=comment)

app.run(debug=True)
