from flask import Flask, render_template
from people import people

app = Flask(__name__)

visibility = True  # Set to True to enable the people pages to be listed on the home page. False by default

@app.route('/')
def index():
    if visibility:
        return render_template('index.html', people=people)
    else:
        return render_template('index.html')

@app.route('/<person_id>')
def person_page(person_id):
    if person_id in people:
        person = people[person_id]
        return render_template('person.html', person=person)
    else:
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
