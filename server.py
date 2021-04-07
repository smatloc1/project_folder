from flask import Flask, render_template, request, flash, redirect, session
from model import connect_to_db, Org, Mission

app = Flask(__name__)
app.secret_key = "2455LB"
