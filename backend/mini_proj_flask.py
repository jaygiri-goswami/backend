from flask import Flask,request
from crypt import methods
import json

app=Flask(__name__)

a ={"one":1,"two":2}

@app.route('/post', methods=['POST','GET'])
def post_json():
    data=request.get_json()
    if request.method == 'POST':
        a.update(data)
        return a
        # b=a.update(payload)

@app.route('/get', methods=['POST','GET'])
def get_json():  
    data=request.get_json()     
    if request.method == 'GET' :
        # return a
        s1 = json.dumps(a)
        # d2 = json.loads(s1)
        return s1
        

# @app.route('/get_json', methods=['GET'])
# def get_json():
#     content_type = request.headers.get('Content-Type')
#     if (content_type == 'application/json'):
#         json = request.get_json()
#         return json
#     else:
#         return 'Content-Type not supported!'

if __name__ == '__main__':
	# app.run(host="0.0.0.0",port=5000)
	app.run(host="0.0.0.0", port=5000)
