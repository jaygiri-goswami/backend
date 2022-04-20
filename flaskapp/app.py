from flask import Flask, render_template, request, redirect
from google.cloud import datastore
import os


app = Flask(__name__)

project_id = "robust-seat-338513"

credentials_path = 'robust-seat-338513-e1cb147a2181.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

# Instantiates a client
datastore_client = datastore.Client(project_id)

# The kind for the new entity
kind = "Task_x"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        coins = userDetails['coins']

        task_key = datastore_client.key(kind,name)

        # Prepares the new entity
        task = datastore.Entity(key=task_key)
        task["value"] = coins

        # Saves the entity
        datastore_client.put(task)

    return render_template('index.html')

# @app.route('/users')
# def users():
#     cur = mysql.connection.cursor()
#     resultValue = cur.execute("SELECT * FROM users")
#     if resultValue > 0:
#         userDetails = cur.fetchall()
#         return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
