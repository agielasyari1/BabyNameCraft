from flask import Flask, render_template, request, jsonify
import pandas as pd
import random
from googletrans import Translator
import os

app = Flask(__name__)
translator = Translator()

UPLOAD_FOLDER = 'uploads'
MALE_DATA_FILE = os.path.join(UPLOAD_FOLDER, 'boys_data.csv')
FEMALE_DATA_FILE = os.path.join(UPLOAD_FOLDER, 'girls_data.csv')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/choose_data', methods=['POST'])
def choose_data():
    selected_data = request.form.get('data_choice')
    if selected_data == 'male':
        data = pd.read_csv(MALE_DATA_FILE)
    elif selected_data == 'female':
        data = pd.read_csv(FEMALE_DATA_FILE)
    else:
        return 'Invalid choice.'

    combined_names, combined_contents = generate_combinations(data, 10)
    results = list(zip(combined_names, combined_contents))
    return render_template('results.html', results=results, data=data.to_dict(orient='records'))

@app.route('/generate_combinations', methods=['POST'])
def generate_combinations_endpoint():
    selected_data = request.json.get('data_choice')
    if selected_data == 'male':
        data = pd.read_csv(MALE_DATA_FILE)
    elif selected_data == 'female':
        data = pd.read_csv(FEMALE_DATA_FILE)
    else:
        return jsonify([])
    
    combined_names, combined_contents = generate_combinations(data, 10)
    results = list(zip(combined_names, combined_contents))
    return jsonify(results)

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '').lower()
    selected_data = request.json.get('data_choice')
    if selected_data == 'male':
        data = pd.read_csv(MALE_DATA_FILE)
    elif selected_data == 'female':
        data = pd.read_csv(FEMALE_DATA_FILE)
    else:
        return jsonify([])

    filtered_data = data[data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    combined_names, combined_contents = generate_combinations(filtered_data, 10)
    results = list(zip(combined_names, combined_contents))
    return jsonify(results)

def generate_combinations(data, count):
    combined_names = []
    combined_contents = []

    for _ in range(count):
        indices = random.sample(range(len(data)), 3)

        name1, content1 = data.iloc[indices[0]]['Name'], data.iloc[indices[0]]['Content']
        name2, content2 = data.iloc[indices[1]]['Name'], data.iloc[indices[1]]['Content']
        name3, content3 = data.iloc[indices[2]]['Name'], data.iloc[indices[2]]['Content']

        translation1 = translator.translate(content1, src='en', dest='id').text
        translation2 = translator.translate(content2, src='en', dest='id').text
        translation3 = translator.translate(content3, src='en', dest='id').text

        combined_name = f"{name1} {name2} {name3}"
        combined_content = f"{translation1} {translation2} {translation3}"

        combined_names.append(combined_name)
        combined_contents.append(combined_content)

    return combined_names, combined_contents

if __name__ == '__main__':
    app.run(debug=True)
