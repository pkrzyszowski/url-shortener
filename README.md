# url-shortener

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
