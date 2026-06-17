from flask import Flask, render_template, request
import data_redundancy_system

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    unique = []
    duplicates = []

    if request.method == 'POST':
        user_input = request.form['data']
        unique, duplicates = data_redundancy_system.process_data(user_input)

    return render_template('index.html', unique=unique, duplicates=duplicates)

if __name__ == '__main__':
    app.run(debug=True)