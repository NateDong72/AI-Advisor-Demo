from flask import render_template, flash, request, url_for
from app import app
#from app.models import User, Post
from datetime import datetime



@app.route('/')
@app.route('/index')
#@login_required
def index():
    return render_template('index.html')

@app.route('/reports')
def reports():    
    return render_template('reports.html')

@app.route('/annotations')
def annotations():    
    return render_template('annotations.html')

@app.route('/models')
def models():    
    return render_template('models.html')

@app.route('/events')
def events():    
    return render_template('events.html')

