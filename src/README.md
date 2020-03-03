Tea Shop
Installation
Installed virtualenv required

Linux:

virtualenv -p python3 .venv
source .venv/bin/activate
pip install requirements.txt
Windows:

virtualenv env
To activate virtualenv on Windows, activate script is in the Scripts folder :

full\path\to\env\Scripts\activate.bat
pip install -r requirements.txt
Run
For the first time don't forget:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Attention
To make a purchase, be sure to register on the site.