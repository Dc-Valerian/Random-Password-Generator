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

        char_pool = ''
        if include_letters:
            char_pool += string.ascii_letters
        if include_symbols:
            char_pool += '!@#$%^&*()-_=+[]{}<>?/|'
        if include_numbers:
            char_pool += string.digits

        if not char_pool:
            error = 'Please select at least one character type.'
        elif length <= 0:
            error = 'Password length must be greater than 0.'
        else:
            password = ''.join(random.choice(char_pool) for _ in range(length))

    return render_template('index.html', password=password, error=error)

if __name__ == '__main__':
    app.run(debug=True)
