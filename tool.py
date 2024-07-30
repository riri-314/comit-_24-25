import pandas as pd

# Existing Python object
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

# Load the Excel file
file_path = 'polo_comité_24-25.csv'
excel_data = pd.read_csv(file_path)

# Function to convert row to dictionary
def row_to_person(row):
    return {
        'name': row.get('Nom', ''),
        'description': '',  # Placeholder for description
        'age': None,        # Placeholder for age
        'post': row.get('Poste', ''),
        'height': '',       # Placeholder for height
        'pictures': []      # Placeholder for pictures
    }

# Adding each row to the people dictionary
for index, row in excel_data.iterrows():
    person_id = row['ID']
    people[person_id] = row_to_person(row)

# Display the updated people dictionary
import pprint
pprint.pprint(people)
