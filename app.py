from flask import Flask, request, jsonify, make_response, render_template, Response
from flask_cors import CORS
from werkzeug.utils import secure_filename
import sqlite3
import os
import datetime
from queries import * 
import requests as req
from PIL import Image

UPLOAD_PATH = './images'
app = Flask(__name__)
CORS(app) # emplying flask_cors for local functionality
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

def get_conn():
    #returns a connection to the database
    conn = sqlite3.connect('image_repo.db')
    cursor = conn.cursor()

    return conn, cursor


def db_init():
    # create SQL table if necessary
    conn, cursor = get_conn()

    conn.execute(create_query)
    conn.commit()
    conn.close()
    print('Database initialized')

@app.route('/images')
def get_images():
    # returns all images currently in database
    conn, cursor = get_conn()

    resp = conn.execute(get_all_query)

    data = resp.fetchall()
    conn.close()
    
    return {'response': data}

@app.route('/upload', methods=['POST'])
def upload_images():
    if request.method == 'POST':
        file = request.files['file'] # receive file from the request
        if file:
            save_path = os.path.join('static/', app.config['UPLOAD_FOLDER']) # path string where file will be saved
            filename = secure_filename(file.filename)
            if filename not in os.listdir(save_path): # verify there isn't a file with the same name in the directory

                file.save(os.path.join(save_path, filename)) # save the file
                pic = Image.open(os.path.join(save_path, filename))
                pic.thumbnail(size=(680, 400))
                pic.save(f'./static/thumbnails/{filename}')


                conn, cursor = get_conn() # update the database indexç

                size = os.path.getsize(os.path.join('static/',app.config['UPLOAD_FOLDER'], filename))/1000000

                date = str(datetime.datetime.now())

                data = (date, size, filename, os.path.join('static/',app.config['UPLOAD_FOLDER'], filename))

                conn.execute(update_query, data)
                resp = conn.execute('SELECT COUNT (*) from images')
                count = resp.fetchall()
                conn.commit()
                conn.close()

                return jsonify(count=count, data=data)
            else: return jsonify({'response': 'File name already exists.'})

    return  jsonify({'response':'File upload error'})

@app.route('/remove/<id>', methods=['DELETE'])
def delete(id):

    # connect to db
    conn, cursor = get_conn()
    
    #identify file path of id that needs to be deleted
    resp = conn.execute(find_query, id)
    data = resp.fetchall()
    

    delete_path = data[0][4]
    file_name = data[0][3]
    # delete from storage
    try:
        os.remove(delete_path)
        os.remove('static/thumbnails/' + file_name)
    except FileNotFoundError: 
        print('file not found, skipping')
    # delete SQL indexing   
    conn.execute(destroy_query, id)
    conn.commit()
    conn.close()

    return f'deleted file {id} from {delete_path}'  

@app.route('/')
def home():
    # render front end with all current images
    images = req.get('http://127.0.0.1:5000/images').json()['response']
    return render_template('index.html', images=images)

if __name__ == '__main__':
    db_init()
    app.run()