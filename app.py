from flask import Flask, render_template, redirect, session,request,url_for

import uuid

import os

app = Flask(__name__)

uid = uuid.uuid4()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-article')
def add_article():
    return render_template('add_article.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'File not chosen'
    file = request.files['file']
    try:
        if not os.path.exists('shop-back/uploads'):
             os.makedirs('shop-back/uploads')
        file.save(f'shop-back/uploads/{uid}.png')
        print(os.path.exists(f'shop-back/uploads/{uid}.png'))
    except Exception as ex:
         print(str(ex))
    return redirect(url_for('index'))
if __name__ == "__main__":
	app.run(debug=True)