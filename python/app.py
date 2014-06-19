#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template

#dados utilizados pela página
app_data = {}

#aplicação
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    app_data['isso'] = 'aquilo'
    return render_template('welcome.html', data=app_data)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
