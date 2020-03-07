# Now an OCR project
...built on top of a Flask.app

# To import dependencies:
pip install -r requirements.txt 

# To run the Flask App:
cd neural-net
source mtg-env-3/bin/activate
python run.py

# To create the database
export FLASK_APP=flaskapp  
flask database create

# Import card list
flask database import-cards