from flask import Flask, render_template, request, url_for, redirect, jsonify, flash
from flask_mysqldb import MySQL

app = Flask (__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'sepomex'


conexion = MySQL(app)

@app.route('/')
def index():
    data= {}
        
    cursor = conexion.connection.cursor()
    sql = "SELECT d_estado FROM estado ORDER BY d_estado ASC"
    cursor.execute(sql)
    estados = cursor.fetchall()
    data['estados'] = estados 
    
    
    return render_template('index.html', data = data)

@app.route("/estado" , methods=['GET', 'POST'])
def estado():
    select = request.form.get('comp_select')

    return(str(select))



if __name__ == '__main__':
    app.run(debug=True, port=5000)