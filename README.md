Использовать модули:

flask
flask-migrate
flask-sqlalchemy
flask-msearch
Bootstrap-Flask
python-dotenv
psycopg2-binary
gunicorn

Установка модулей:
pip install flask flask-migrate flask-msearch flask-sqlalchemy Bootstrap-Flask python-dotenv psycopg2-binary gunicorn

Cтруктура проекта:

mkdir english
mkdir templates static & cd static
mkdir css favicon img_404 img_500 search_404
cd css & echo. > style.css & cd .. & cd ..
cd templates & mkdir english & cd .. & cd ..
echo. > .gitignore & echo. > main.py
pip freeze > requirements.txt
cd english & echo. > .env

for %i in (__init__ models routes views settings) do echo. > %i.py
