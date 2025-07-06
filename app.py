from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    error = ''

    if request.method == 'POST':
        length = int(request.form.get('length', 0))
        include_letters = 'letters' in request.form
        include_symbols = 'symbols' in request.form
        include_numbers = 'numbers' in request.form

        characters = ''
        if include_letters:
            characters += string.ascii_letters
        if include_symbols:
            characters += '!@#$%^&*()-_=+[]{}<>?/|'
        if include_numbers:
            characters += string.digits

        if not characters:
            error = 'Please select at least one character type.'
        elif length <= 0:
            error = 'Please enter a valid password length.'
        else:
            password = ''.join(random.choices(characters, k=length))

    return render_template('index.html', password=password, error=error)

if __name__ == '__main__':
    app.run(debug=True)
