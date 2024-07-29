# comite_24-25
Super secret website for comité_24-25

# Requirement
python >= 3.10
Flask (pip install Flask)

# Setup
```console
git clone https://github.com/riri-314/comite_24-25.git
cd comite_24-25
python3 app.py
```
The addresse of the local server should be printed in the terminal

# Files
1. app.py, the main python file with the flask server
2. people.py, contain the data of the people
3. templates/index.html is the html of the home
4. templates/people.html is the html template for a person
5. templates/404.html is the not found page
6. static/ contain all of the pictures and favicons

# Best practices
Pictures should not be larger than 100kB.
No more than 10 pictures by person.
Do not enter the person name in people.py if some pictures are too "guindaille". It prevent google from indexing.

