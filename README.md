# ChatBot

This project demonstrates how to build a basic chatbot using **Django** as the backend framework and **SpaCy** for Natural Language Processing (NLP). The chatbot responds to user inputs, including greetings and farewells. This project is perfect for anyone looking to integrate simple NLP functionalities into a web application.

## Features

- Simple conversational responses (e.g., greetings, farewells).
- Backend logic powered by **Django**.
- Natural Language Processing using **SpaCy**.
- Basic web interface using HTML and CSS.

## Tech Stack

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS
- **NLP**: SpaCy (Language processing)
- **Language Model**: `en_core_web_sm` (English language model)

## Installation

To run the project locally, follow these steps:

### 1. Clone the repository

Start by cloning this repository to your local machine:
git clone https://github.com/anageguchadze/ChatBot.git
cd ChatBot

 Create and activate a virtual environment
To avoid conflicts with other Python packages, it’s best to set up a virtual environment:
python -m venv venv
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

3. Install the dependencies
Use pip to install the required Python packages listed in the requirements.txt file:
pip install -r requirements.txt

4. Download the SpaCy language model
To enable the NLP functionality, you need to download the en_core_web_sm language model:
python -m spacy download en_core_web_sm

5. Apply migrations
Before running the project, apply the Django database migrations:
python manage.py migrate

6. Run the development server
Now, you're ready to run the project. Start the Django development server with:
python manage.py runserver

You can access the chatbot by opening your browser and visiting: http://127.0.0.1:8000/.

Project Structure
The directory structure of the project is as follows:
chatbot/
├── chatbot/                  # Main app folder
│   ├── migrations/           # Database migrations
│   ├── static/               # Static files (CSS, JS, images)
│   ├── templates/            # HTML templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py              # URL configuration
│   └── views.py             # Views for handling requests
├── manage.py                 # Django management commands
├── requirements.txt          # Project dependencies
└── venv/                     # Virtual environment
Contributing
Feel free to fork this repository, create a new branch, and submit a pull request with any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for more details.