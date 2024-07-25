# Baby Name Generator

A simple Flask web application that provides a list of names and their translations. The app allows users to choose between male and female names, generate new combinations, and search for keywords in the results.

## Features

- **Generate Names**: Generate new combinations of names with their translations.
- **Search**: Search for specific names or keywords in the results.
- **User Interface**: Simple and intuitive interface with Bootstrap styling.

## Installation

To get started with this project, follow these instructions to set up your development environment.

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Setting Up

1. **Clone the Repository**

    ```bash
    git clone https://github.com/agielasyari1/BabyNameCraft.git
    cd BabyNameCraft
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On Windows:
    
      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:
    
      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up Environment Variables**

    Ensure you have the following environment variables set, if necessary:

    - `UPLOAD_FOLDER`: Directory where CSV files are stored.

6. **Run the Application**

    ```bash
    flask run
    ```

    Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage

1. **Choose Data**: Select whether you want to work with male or female names.
2. **Generate Combinations**: Click the "Generate New Combinations" button to generate new name combinations.
3. **Search**: Use the search bar to find specific names or keywords in the results.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. **Fork the Repository**: Create your own fork of the repository.
2. **Create a Branch**: Create a new branch for your changes.
3. **Make Changes**: Implement your changes and test them.
4. **Submit a Pull Request**: Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Flask**: A lightweight WSGI web application framework.
- **Pandas**: Data manipulation and analysis library.
- **Googletrans**: Library for Google Translate API.

---

Feel free to customize the content to better fit your project's specifics and any additional information you want to provide.
