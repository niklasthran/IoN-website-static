from flask import Flask, render_template
import json
import os
data_location = "./static"

# List all photos in photo_archive directory
photo_list = []
photo_format = ["jpg", "jpeg", "gif", "png"]
for photo in os.listdir(f"{data_location}/data"):
    if photo.lower().endswith(tuple(photo_format)):
        #print(photo)
        photo_list.append(f"{data_location}/data/{photo}")
photo_list.sort(reverse=False)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("photo_archive.html", photo_list=photo_list)

if __name__ == "__main__":
    app.run(debug = True)