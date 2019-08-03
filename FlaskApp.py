from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = ''      #Write your mail_server detail#
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = ''    #Write your username(email-address)#
app.config['MAIL_SENDER'] = ''      #Write your Gmail Password#

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hey  There', recipients=[''])    #Write your recippient's email-address#
    mail.send(msg)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)