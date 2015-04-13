"""
import random
from interpolate_plotting import*
import re
from flask import Flask,url_for,request,render_template
ctr=0
app=Flask(__name__)
#in url_for name of function comes in form of string
@app.route('/',methods=['GET','POST'])
def hello():
    createLink1="<a href='"+url_for('take')+"'>CALCULATE AVERAGE</a>"
    createLink2="<a href='"+url_for('show')+"'>NUMPY PLOTTING</a>"
    createLink3="<a href='"+url_for('profile')+"'>Harpreet Singh</a>"
    return """<HTML>
                <head>
                  <title>web assignment</title>
                </head>
                <body>
                     <div id="title"><h1>WEB DESIGNING ASSIGNMENT</h1></div>
                     <div>
                     <h2><i><u>DEVELOPERS</u></i></h2><br>
                     </div>
                     <h2>"""+createLink3+"""</h2>
                     <div>
                     <h2>""" + createLink1 + """</h2></a><br/>
                     <h2>""" + createLink2 + """</h2></a><br/>
                     </div>   
                </body>
                </html>"""
@app.route('/plot',methods=['GET','POST'])
def take():
    if request.method=='GET':
        #send the user the form
        return render_template('calculating_average.html');
    elif request.method=='POST':
        #read form data and save it
        str=request.form['string']
        L=re.split(r'[,]',str)
        L=map(int,L)
        L=list(L)
        av=sum(L)/len(L)
        return render_template('output_average.html',average=av)
        #store data in data store
    else:
        return "<h2>Invalid request</h2>"

@app.route('/make',methods=['GET','POST'])
def show():
    if request.method=='GET':
        #send the user the form
        return render_template('plotting.html');
    elif request.method=='POST':
        render_template('return_plot.html',figure="")
        #read form data and save it
        x_coordinates=request.form['list1']
        y_coordinates=request.form['list2']
        x_coordinates=re.split(r'[,]',x_coordinates)
        y_coordinates=re.split(r'[,]',y_coordinates)
        x_coordinates=map(int,x_coordinates)
        y_coordinates=map(int,y_coordinates)
        x_coordinates=list(x_coordinates)
        y_coordinates=list(y_coordinates)
        ctr=random.randint(0,100)        
        #algorithm for interpolate
        apx=Interpolate()
        apx.plot(x_coordinates,y_coordinates,ctr)
        xx='this_plot'+str(ctr)+'.png'                                                          
        return render_template('return_plot.html',figure=url_for('static',filename=xx))
        #store data in data store
    else:
        return "<h2>Invalid request</h2>"
@app.route('/profile')
def profile():
    if request.method=='GET':
        #send the user the form
        return render_template('Harpreet Singh.html',path=url_for('static',filename='profilepic.jpg'));
