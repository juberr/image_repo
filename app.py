from flask import Flask, request, jsonify, make_response, render_template, Response
from werkzeug.utils import secure_filename
import sqlite3
import os
import datetime
from queries import * 
import requests as req

UPLOAD_PATH = './images'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

def get_conn():

    conn = sqlite3.connect('image_repo.db')
    cursor = conn.cursor()

    return conn, cursor

# create connection to database and table if necessary
def db_init():
    conn, cursor = get_conn()

    conn.execute(create_query)
    conn.commit()
    conn.close()
    print('Database initialized')

@app.route('/images')
def get_images():

    conn, cursor = get_conn()

    resp = conn.execute(get_all_query)

    data = resp.fetchall()
    conn.close()
    
    return {'response': data}

@app.route('/upload', methods=['GET', 'POST'])
def upload_images():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            conn, cursor = get_conn()

            size = os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], filename))/1000000

            date = str(datetime.datetime.now())

            data = (date, size, filename, os.path.join(app.config['UPLOAD_FOLDER'], filename))

            conn.execute(update_query, data)
            conn.commit()
            conn.close()
            return 'uploaded!'

    return  'something went wrong'

@app.route('/remove/<id>', methods=['DELETE'])
def delete(id):

    # connect to db
    conn, cursor = get_conn()
    #identify file path of id that needs to be deleted
    index = req.get("http://127.0.0.1:5000/images").json()
    delete_path = index['response'][0][-1]
    delete_index = index['response'][0][0]
    # delete from storage
    try:
        os.remove(delete_path)
    except FileNotFoundError: 
        print('file not found, skipping')
    # delete SQL indexing   
    conn.execute(destroy_query, (delete_index,))
    conn.commit()
    conn.close()

    return f'deleted file {id} from {delete_path}'  

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    db_init()
    app.run()