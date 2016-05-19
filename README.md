wt-tests
gunicorn myproject.wsgi
This will start one process running one thread listening on 127.0.0.1:8000.
It requires that your project be on the Python path; the simplest
way to ensure that is to run this command from the same directory as your
manage.py file.


