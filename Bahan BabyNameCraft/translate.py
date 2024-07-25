import pandas as pd
from googletrans import Translator

# Load the CSV file
file_path = 'uploads/girls_data.csv'
data = pd.read_csv(file_path)

# Initialize the translator
translator = Translator()

# Translate the "Content" column
data['Content'] = data['Content'].apply(lambda x: translator.translate(x, src='en', dest='id').text)

# Keep only the "Name" and "Content" columns
final_data = data[['Name', 'Content']]

# Save the translated data to a new CSV file
final_data.to_csv('uploads/girls_data_translated.csv', index=False)

print("Translation complete. Translated file saved as 'girls_data_translated.csv'.")
