from flask import render_template
from server import app

def errors(code):
    return render_template(f'errors/{code}.html')

@app.errorhandler(404)
def not_found_error(error):
    return errors(404)

@app.errorhandler(401)
def not_found_error(error):
    return errors(401)
