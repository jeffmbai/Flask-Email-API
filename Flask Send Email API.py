import os
from flask import Flask, request, jsonify
from flask_mail import Mail, Message 

# Initialize Flask app
app = Flask(__name__)

# Initialize Flask Mail
# Configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app) # instantiate the mail class   

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Flas EMAIL API! "


#################### Help Messages API ############################
@app.route('/helpmessages', methods=['POST'])
def post_help_message():
    try:
        data = request.get_json()
        # Create email content using the provided template
        email_content = f"""
        <h1>New Help Message</h1>
        <p>
          <b>Name:</b> {data.get('name', 'N/A')}<br>
          <b>Email:</b> {data.get('email', 'N/A')}<br>
          <b>Phone Number:</b> {data.get('mobileNumber', 'N/A')}<br>
          <b>Message:</b> {data.get('message', 'N/A')}<br>
        </p>
        """

        # Prepare email
        msg = Message(
            'New Help Message Submitted',
            sender= "sender email",
            recipients=['receiver email']
        )
        msg.html = email_content

        # Send email
        mail.send(msg)

        return jsonify({"success": True, "message": "Help message added successfully"}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 400


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
