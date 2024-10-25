import pymysql
from flask import Flask, request, render_template

def get_db_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="test",
            passwd="1234",
            port=3306,
            database="tks_official"
        )
        return conn
    except Exception as e:
        print(f"連線錯誤: {e}")
        return None

app = Flask(__name__)

@app.route('/inbox')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "USE tks_official"
    cursor.execute(sql)
    cursor.callproc('get_all_message')
    result = cursor.fetchall()
    messages = []
    for row in result:
        message = {
            'name': row[1],         # customer_name
            'company': row[2],      # company_name
            'email': row[3],        # email
            'message': row[4],       # subject（假设这里是 message）
            'date': row[0].strftime('%Y-%m-%d %H:%M:%S'),         # timestamp
        }
        messages.append(message)
    return render_template('inbox.html', emails=messages)

@app.route('/sent')
def sent():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "USE tks_official"
    cursor.execute(sql)
    cursor.callproc('get_sent_message')
    result = cursor.fetchall()
    messages = []
    for row in result:
        message = {
            'name': row[1],         # customer_name
            'company': row[2],      # company_name
            'email': row[3],        # email
            'message': row[4],       # subject（假设这里是 message）
            'date': row[0].strftime('%Y-%m-%d %H:%M:%S'),         # timestamp
        }
        messages.append(message)
    return render_template('sent.html', emails=messages)

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
    
    # conn = get_db_connection()
    # cursor = conn.cursor()
    # sql = "USE tks_official"
    # cursor.execute(sql)
    # sql = "CALL move_customer_info(%s)"
    # cursor.execute(sql, (move_timestamp,))

    subject = request.form.get('subject', '')
    message = request.form.get('message', '')
    email = request.form.get('email', 'Unknown')
    name = request.form.get('name', 'Unknown')
    company = request.form.get('company', 'Unknown')
    original_message = request.form.get('original_message', 'Unknown')
    date = request.form.get('date', 'Unknown')
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "USE tks_official"
    cursor.execute(sql)
    sql = "CALL move_customer_info(%s, %s, %s)"
    print(date, subject, message)
    cursor.execute(sql, (date, subject, message, ))
    conn.commit()

    # Add your logic to send the email or process the reply here.

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
