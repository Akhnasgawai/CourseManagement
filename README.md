# coursemanagement

create a virtual environment using the command: virtualenv venv
activate the virtual environment by using the command: venv\Scripts\activate
install the required libraries by running: pip install -r requirements.txt
start the celery worker by running the command: celery -A CourseManagement worker -l info --pool=solo
run the python server using the command: python manage.py runserver
