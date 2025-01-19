set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
    python manage.py createsuperuser --no-input
fi
