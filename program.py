# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:54:14 2019

@author: AndreasK
"""

from flask import Flask
from flask import render_template
from tv_spored import programi_df


app = Flask(__name__)

@app.route('/')
def about():
    #ura = programi_df['Ura']
    #trenutno = programi_df['Trenutno']    
    
    return render_template('program.html',  tables=[programi_df.to_html(classes='table-striped table-dark')], header="true")


