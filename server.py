from flask import Flask, render_template, request, flash, redirect, session
from model import connect_to_db, Org, Mission

app = Flask(__name__)
app.secret_key = "2455LB"




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)