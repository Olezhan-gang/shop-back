from flask import Flask, render_template, redirect, session,request,url_for, send_from_directory

from mysql import add_article, get_all_articles
from tgbot import send_notification

import uuid

import os


app = Flask(__name__)

def generate_uuid():
    return str(uuid.uuid4())

@app.route('/')
def index():
    return render_template('index.html', articles=get_all_articles())

@app.route('/add-article')
def add_articles():
    return render_template('add_article.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'uploads'), filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    uid = generate_uuid()
    if 'file' not in request.files:
        return 'File not chosen'
    name = request.form['name']
    price = request.form['price']
    file = request.files['file']
    try:
        if not os.path.exists('shop-back/uploads'):
             os.makedirs('shop-back/uploads')
        file.save(f'shop-back/uploads/{uid}.png')
        add_article(name,price,uid)
        print('Article seccsessfuly added')
    except Exception as ex:
         print(str(ex))
    return redirect(url_for('index'))

@app.route('/article/<string:uuid>')
def admin_panel(uuid):
    return render_template('article.html', image = uuid)


if __name__ == "__main__":
	app.run(debug=True)