from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

import pymysql

db = pymysql.connect(host="127.0.0.1",
                     user="root",
                     password="aluno",
                     database="Amenic")

@app.route('/')
def index():
    cursor = db.cursor()
    sql = "SELECT * FROM filmes;"
    cursor.execute(sql)
    filmes = cursor.fetchall()
    return render_template('index.html', filmes=filmes)

@app.route('/inputForms', methods=['POST'])
def input():
    movieTitle = request.form['movieTitle']
    movieGenre = request.form['movieGenre']

    cursor = db.cursor()
    sql = "INSERT INTO filmes (tituloFilme, generoFilme) VALUES (%s, %s);"
    cursor.execute(sql, (movieTitle, movieGenre))
    db.commit()

    return redirect(url_for('index'))

@app.route('/updateMovie', methods=['POST'])
def updateMovie():
    idMovie = request.form['idMovie']
    movieTitle = request.form['movieTitle']
    movieGenre = request.form['movieGenre']

    cursor = db.cursor()
    sql = "UPDATE filmes SET tituloFilme = %s, generoFilme = %s"
    sql += "WHERE id = " + idMovie + ";"
    cursor.execute(sql, (movieTitle, movieGenre))
    db.commit()

    return redirect(url_for('index'))

@app.route('/deleteMovie', methods=['POST'])
def deleteMovie():
    idMovie = request.form['idMovie']

    cursor = db.cursor()
    sql = "DELETE FROM filmes WHERE id = " + idMovie +";"
    cursor.execute(sql)
    db.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)