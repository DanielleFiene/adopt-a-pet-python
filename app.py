from flask import Flask

from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
    return f'''
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend: </p>
    <ul>
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href="/animals/cats">Cats</a></li>
    <li><a href="/animals/rabbits">Rabbits</a></li>
    </ul>
    '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
    # Check if the pet_type exists in the `pets` dictionary
    if pet_type in pets:
        pet_list = pets[pet_type]  # Get the list of pets for the given type
        html = f'<h1>List of {pet_type.capitalize()}</h1>'
        html += '<ul>'  # Start the unordered list

        # Loop through the list of pets and add each name as a <li> with a link to their profile
        for i, pet in enumerate(pet_list):
            html += f'<li><a href="/animals/{pet_type}/{i}">{pet["name"]}</a></li>'

        html += '</ul>'  # Close the unordered list
    else:
        # If pet_type is not found, show a not found message
        html = f'<h1>Sorry, we don’t have any {pet_type} available for adoption.</h1>'

    return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    # Check if pet_type exists and pet_id is valid
    if pet_type in pets and 0 <= pet_id < len(pets[pet_type]):
        pet = pets[pet_type][pet_id]  # Get the pet's dictionary

        # Create HTML for the pet's profile
        html = f'''
        <h1>{pet["name"]}</h1>
        <p><strong>Age:</strong> {pet["age"]}</p>
        <p><strong>Breed:</strong> {pet["breed"]}</p>
        <p><strong>Description:</strong> {pet["description"]}</p>
        <img src="{pet["url"]}" alt="Image of {pet["name"]}">
        '''
    else:
        # If pet_type or pet_id is invalid, show an error message
        html = f'<h1>Sorry, we couldn’t find the pet you were looking for.</h1>'

    return html

if __name__ == '__main__':
    app.run(debug=True)
