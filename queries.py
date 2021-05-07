create_query = """
CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY NOT NULL, date DATETIME, size_mb REAL, name VARCHAR(100), image_path VARCHAR(100))
"""

get_all_query = 'SELECT * FROM images'

update_query = """
INSERT INTO images (date, size_mb, name, image_path) VALUES (?,?,?,?)"""

destroy_query = """DELETE FROM images WHERE id = ?;"""
