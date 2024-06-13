from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Establish database connection

def get_db_connection():
    conn = sqlite3.connect('recipeDB.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route to get all recipes
@app.route('/api/recipes', methods = ['GET'])
def get_recipes():
    conn = get_db_connection()
    recipes = conn.execute('SELECT * FROM Recipe').fetchall()
    conn.close()
    return jsonify([dict(index) for index in recipes])

# Route to get one recipe
@app.route('/api/recipes/<int:id>', methods = ['GET'])
def get_recipe(id):
    conn = get_db_connection()
    recipe = conn.execute('SELECT * FROM Recipe WHERE Recipe_id = ?', (id,)).fetchone()[0]
    conn.close()
    if recipe is None:
        return jsonify({'error': 'Finner ikke oppskrift'}), 404
    return jsonify(dict(recipe))

# Route to create a new recipe
@app.route('/api/recipes', method = ['POST'])
def create_recipe():
    new_recipe = request.get_json() # converts JSON data sent in the POST rquest to dictionary
    conn = get_db_connection()
    conn.execute(
        '''INSERT INTO Recipe VALUES (Name, Time, Difficulty, Instructions) 
        VALUES (?, ?, ?, ?)''', 
        (new_recipe['Name'], new_recipe['Time'], new_recipe['Difficulty'], new_recipe['Instructions'])
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Recipe created!'}), 201