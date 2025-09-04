from flask import Flask, request, render_template
import pymysql

app=Flask(__name__)

db = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='test'
)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit',methods=['POST'])
def submit():
    with db.cursor() as cursor:
        name=request.form['name']
        email=request.form['email']
        insert_query="INSERT INTO users (name,email) VALUES (%s,%s)"
        cursor.execute(insert_query,(name,email))
        db.commit()
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)