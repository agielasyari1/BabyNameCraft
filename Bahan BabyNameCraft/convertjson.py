import pandas as pd

def convert_csv_to_json(csv_file_path, json_file_path):
    df = pd.read_csv(csv_file_path)
    df.to_json(json_file_path, orient='records')

#convert_csv_to_json('uploads/boys_data_translated.csv', 'uploads/boys_data.json')
convert_csv_to_json('uploads/girls_data_translated.csv', 'uploads/girls_data.json')
