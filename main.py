from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    markers = json.load(open('markers.json'))
    
    for marker in markers['Marcadores']:
        html_string = ''
        for necessidade in marker['necessidades']:
            html_string += f'{necessidade}<br>'
        marker['necessidades'] = html_string
    riskareas = json.load(open('riskareas.json'))
    return render_template('index.html', markers=markers, riskareas=riskareas)

@app.route('/telefones')
def telefones():
    return render_template('telefones.html')
    
@app.route('/grupos')
def grupos():
    return render_template('grupos.html')


if __name__ == '__main__':
    app.run()