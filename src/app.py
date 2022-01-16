from flask import Flask, request
import os
from controller.test import myFuc


app = Flask(__name__)

@app.route('/')
def index():
    return myFuc()



@app.route('/upload', methods=['POST'])
def upload():
  request.files['file'].save(request.files['file'].filename)
  return "Uploaded!"



if __name__ == '__main__':
    try:
      os.mkdir('uploads')
    except:
      print("Folder Already Created")
    app.run(debug=True, port=7000)
