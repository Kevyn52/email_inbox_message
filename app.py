from flask import Flask, request, render_template



app = Flask(__name__)

@app.route('/inbox')
def index():
    emails = [
        {
            'name': 'John Doe',
            'company': 'Acme Inc.',
            'email': 'john.doe@example.com',
            'message': 'Hello! I need more info about your products.',
            'date': '2024-10-14'
        },
        {
            'name': 'Jane Smith',
            'company': 'Beta Ltd.',
            'email': 'jane.smith@beta.com',
            'message': 'Can we set up a meeting?',
            'date': '2024-10-15'
        }
    ]
    
    # Pass the email data to the template
    return render_template('inbox.html', emails=emails)

@app.route('/sent')
def sent():
    emails = [
        {
            'name': 'John Doe',
            'company': 'Acme Inc.',
            'email': 'john.doe@example.com',
            'message': 'Hello! I need more info about your products.',
            'date': '2024-10-14'
        },
        {
            'name': 'Jane Smith',
            'company': 'Beta Ltd.',
            'email': 'jane.smith@beta.com',
            'message': 'Can we set up a meeting?',
            'date': '2024-10-15'
        }
    ]
    
    # Pass the email data to the template
    return render_template('sent.html', emails=emails)

@app.route('/reply')
def reply():
    # Retrieve the query parameters
    name = request.args.get('name', 'Unknown')
    company = request.args.get('company', 'Unknown')
    email = request.args.get('email', 'Unknown')
    message = request.args.get('message', 'Unknown')
    date = request.args.get('date', 'Unknown')
    
    # Render the reply template with the received data
    return render_template('reply.html', name=name, company=company, email=email, message=message, date=date)

@app.route('/send_reply', methods=['POST'])
def send_reply():
    # Retrieve form data
    subject = request.form.get('subject', '')
    message = request.form.get('message', '')
    email = request.form.get('email', 'Unknown')
    name = request.form.get('name', 'Unknown')
    company = request.form.get('company', 'Unknown')
    original_message = request.form.get('original_message', 'Unknown')
    date = request.form.get('date', 'Unknown')

    # Here, you can add logic to send the email or process the reply
    # For now, let's just render a response page
    return render_template('reply_confirmation.html', subject=subject, message=message, email=email, name=name, company=company, original_message=original_message, date=date)

@app.route('/delete', methods=['GET'])
def delete():
    # Retrieve the query parameters
    name = request.args.get('name', 'Unknown')
    company = request.args.get('company', 'Unknown')
    email = request.args.get('email', 'Unknown')
    message = request.args.get('message', 'Unknown')
    date = request.args.get('date', 'Unknown')
    
    # Render the delete template with the received data
    return render_template('delete.html', name=name, company=company, email=email, message=message, date=date)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
