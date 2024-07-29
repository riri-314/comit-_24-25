from flask import Flask, render_template

app = Flask(__name__)

visibility = False  # Set to True to enable the people pages to be listed on the home page. False by default

# Comitards data, hard-coded baby
people = {
    '123abc': {
        'name': 'Camart',
        'description': "J'aime la chope et la guindaille. Yahouuuu",
        'age': 3.14,
        'post': 'Sys admin',
        'height': "3 futs",
        'pictures': [
            'static/1.jpg',
            'static/2.jpg',
            'static/3.jpg',
            'static/4.jpg',
            'static/3.jpg',
            'static/2.jpg',
            'static/1.jpg',
        ]
    },
}

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
