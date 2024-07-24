from flask import Flask, render_template, request, jsonify
import json
import random
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
MALE_DATA_FILE = os.path.join(UPLOAD_FOLDER, 'boys_data.json')
FEMALE_DATA_FILE = os.path.join(UPLOAD_FOLDER, 'girls_data.json')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/choose_data', methods=['POST'])
def choose_data():
    selected_data = request.form.get('data_choice')
    if selected_data == 'male':
        data = load_data(MALE_DATA_FILE)
    elif selected_data == 'female':
        data = load_data(FEMALE_DATA_FILE)
    else:
        return 'Invalid choice.'

    combined_names, combined_contents = generate_combinations(data, 10)
    results = list(zip(combined_names, combined_contents))
    return render_template('results.html', results=results, data_choice=selected_data)

@app.route('/generate_combinations', methods=['POST'])
def generate_combinations_endpoint():
    selected_data = request.json.get('data_choice')
    if selected_data == 'male':
        data = load_data(MALE_DATA_FILE)
    elif selected_data == 'female':
        data = load_data(FEMALE_DATA_FILE)
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
        data = load_data(MALE_DATA_FILE)
    elif selected_data == 'female':
        data = load_data(FEMALE_DATA_FILE)
    else:
        return jsonify([])

    filtered_data = [
        row for row in data 
        if (row.get('Name') and query in row['Name'].lower()) or (row.get('Content') and query in row['Content'].lower())
    ]

    if not filtered_data:
        return jsonify([])

    try:
        combined_names, combined_contents = generate_combinations(filtered_data, 10)
        results = list(zip(combined_names, combined_contents))
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/search_results', methods=['POST'])
def search_results():
    selected_data = request.form.get('data_choice')
    query = request.form.get('query', '').lower()
    if selected_data == 'male':
        data = load_data(MALE_DATA_FILE)
    elif selected_data == 'female':
        data = load_data(FEMALE_DATA_FILE)
    else:
        return 'Invalid choice.'

    filtered_data = [
        row for row in data 
        if (row.get('Name') and query in row['Name'].lower()) or (row.get('Content') and query in row['Content'].lower())
    ]

    combined_names, combined_contents = generate_combinations(filtered_data, 10)
    results = list(zip(combined_names, combined_contents))
    return render_template('results.html', results=results, data_choice=selected_data, query=query)

def generate_combinations(data, count):
    if not data:
        return [], []

    combined_names = []
    combined_contents = []

    for _ in range(count):
        if len(data) < 3:
            sampled_data = data * (3 // len(data)) + data[:3 % len(data)]
        else:
            sampled_data = random.sample(data, 3)
        
        combined_name = " ".join(item.get('Name', '') for item in sampled_data)
        combined_content = " ".join(item.get('Content', '') for item in sampled_data)

        combined_names.append(combined_name)
        combined_contents.append(combined_content)

    return combined_names, combined_contents

if __name__ == '__main__':
    app.run(debug=True)
