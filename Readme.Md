Flask API to send emails using GMAIl

1) enter your credentials on 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

2) installations
Flask_Cors==3.0.10
Flask_RESTful==0.3.9
Flask==2.0.1
gunicorn
Werkzeug==2.2.2
Flask-Mail == 0.10.0

3) Enter Receiver email and sender email
 sender= "sender email",
recipients=['receiver email']


4) Test with postman
5) Tune to your design