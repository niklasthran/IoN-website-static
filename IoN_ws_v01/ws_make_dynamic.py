from flask import Flask, render_template
import json
import os
data_location = "./static"

# List all photos in photo_archive directory
photo_list = []
for photo in os.listdir(f"{data_location}/photo_archive"):
    if ".DS_Store" not in photo:
        photo_list.append(f"{data_location}/photo_archive/{photo}")
photo_list.sort(reverse=True)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("photo_archive.html", photo_list=photo_list)

if __name__ == "__main__":
    app.run(debug = True)