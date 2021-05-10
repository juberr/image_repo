# Justin's Image Repository

## Set Up Instructions

* Clone this repository from GitHub by running `git clone https://github.com/juberr/image_repo` in a new folder.

* To ensure compatibility I have included a requirements.txt file that can install any required Python libraries to your environment. To install run `pip install -r requirements.txt`

* Once requirements are installed run the flask application via `python app.py` 

## Features

* Live uploading and deleting of files without refreshing the page

* Multiple file uploads

* Visual preview of the current files in the repository below the upload field

* Creates thumbnails of all images using Python's Pillow library

## Future Additions

* Search field to filter by name/size/date

* More styling for user accessibility

* Live preview of files to be uploaded

## Tech Stack

This project employs the following tech stack:

Front end:

* Bootstrap CSS styling
* Jquery for live HTML updates

Back end:

* Flask API to interface with the front end, and update the system/database

* SQLite database to track file metadata



