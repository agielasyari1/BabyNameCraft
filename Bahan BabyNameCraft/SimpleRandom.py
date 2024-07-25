import pandas as pd
import random
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Load the CSV file
file_path = 'detail_data.csv'  # Update with your actual file path
data = pd.read_csv(file_path)

# Check the content of the CSV to ensure it has the "Name" and "Content" columns
if 'Name' in data.columns and 'Content' in data.columns:
    combined_names = []
    combined_contents = []
    
    for _ in range(10):
        # Randomly select two rows
        indices = random.sample(range(len(data)), 2)
        
        name1, content1 = data.iloc[indices[0]]['Name'], data.iloc[indices[0]]['Content']
        name2, content2 = data.iloc[indices[1]]['Name'], data.iloc[indices[1]]['Content']
        
        # Translate content to Bahasa Indonesia
        translation1 = translator.translate(content1, src='en', dest='id').text
        translation2 = translator.translate(content2, src='en', dest='id').text
        
        # Combine the names and their translations
        combined_name = f"{name1} {name2}"
        combined_content = f"{translation1} {translation2}"
        
        combined_names.append(combined_name)
        combined_contents.append(combined_content)
    
    for i in range(10):
        print(f"Combined Name {i+1}: {combined_names[i]}")
        print(f"Combined Content {i+1}: {combined_contents[i]}")
else:
    print("The 'Name' and/or 'Content' column is not present in the CSV file.")
