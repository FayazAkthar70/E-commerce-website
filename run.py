from .market import create_app

app = create_app()

gunicorn run:app
