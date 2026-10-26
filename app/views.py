from app import app
import datetime
from datetime import date
from flask import render_template, request, redirect, url_for, flash


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile')
def profile():
    return render_template('profile.html',date=format_date_joined(2018,5,12))

def format_date_joined(year,month,day):
    
    date_joined = datetime.date(year,month,day)
    return "Joined " + date_joined.strftime("%B,%Y")

@app.route('/group')
def group():
    return render_template('group.html',curr= duty(mm,dd))

today= str(date.today())
datex=[int(x) for x in today.split('-')]
curr_year,mm,dd= datex

def duty(mm,dd):
    groups= [[1,'Chambers','Dewar','Geo','Samuel'],
             [2,'Clarke','Hayden','Nathaniel','Ashauni'],
             [3,'Chambers','Clarke','Nethaneel','Joseph'],
             [4,'Dewar','Hayden','Geo','Nathaniel'],
             [5,'Chambers','Hayden','Samuel','Ashauni'],
             [6,'Dewar','Clarke','Nethaneel','Joseph']
             ]

    dim= [31,28,31,30,31,30,31,31,30,31,30,31]
    count=0
    addm= 0
    for i in dim:
        count+=1
        if  count < mm:
            addm += i
        
        
        #print(i,count)
    nday = addm + dd
    #find the number of weeks
    wks= nday/7
    #print(wks)
    grp = int(wks % 6)
    grp+=1
    if grp == 0:
        ans= groups[-1]
    else:
        #original commented return
        #return groups[grp-1]
        ans =groups[grp-1]
    c=1
    dic = {}
    for i in ans:
        if (type(i)==int):
            dic.update({"Group":i})
        else:
            dic.update({c:i})
            c+=1
    return dic
        
    




###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
