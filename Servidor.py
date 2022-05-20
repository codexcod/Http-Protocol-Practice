from flask import Flask, session, request, url_for, redirect
from markupsafe import escape

import random
import json

# Inspirado en https://flask.palletsprojects.com/en/2.1.x/quickstart/
# En un cmd:
#   > pip install flask
#   > set FLASK_APP=Servidor
#   > flask run
# En el browser, entrar a http://localhost:5000

app = Flask(__name__)

# generar con
#         python -c 'import secrets; print(secrets.token_hex())'
# o con 
#         python3 -c 'import secrets; print(secrets.token_hex())'
app.secret_key = "887e18e60395e07dd96ed8bafcc219d29d697aee814a01bde5f9c8e4236293b6"

class DB:
    def __init__(self, ruta='db.json'):
        self.ruta = ruta
        try:
            with open(self.ruta) as f:
                self.data = json.loads(f.read())
        except:
            # nueva base de datos
            self.data = {}
            self.data.setdefault('userdata', {})

    def guardar(self):
        with open(self.ruta, 'w') as f:
            f.write(json.dumps(self.data, indent=4, sort_keys=True))

    def nuevo_user(self):
        # userId numerico
        numberUserId = self.data.get('user_id_next', 1)
        self.data['user_id_next'] = numberUserId + 1

        # userId como string (las claves de un json van a ser string)
        userId = str(numberUserId)

        data = self.data['userdata'][userId] = {}

        palabraAleatoria = random.choice([
                    "que",
                    "y",
                    "despues",
                    "la",
                    random.randint(1, 1000),
                    random.randint(100, 1000),
                    random.randint(500, 1000)
                    ])
       
        

        data['palabra'] = palabraAleatoria

        self.set_userdata(userId, data)  # guarda
        return userId

    def get_userdata(self, userId):
        return self.data['userdata'].get(userId)

    def set_userdata(self, userId, data):
        self.data['userdata'][userId] = data
        self.guardar()

db = DB()

def ensure_valid_userid():
    if 'userid' in session:
        userId = session['userid']
        if db.get_userdata(userId) is not None:
            # el userid de la sesion ya estaba en la db
            return

    # generar uno nuevo
    session['userid'] = db.nuevo_user()
        
@app.route('/')
def index():
    ensure_valid_userid()
    return redirect(url_for("palabras"))

@app.route('/palabras', methods=['GET', 'POST'])
def palabras():
    ensure_valid_userid()

    userId = session['userid']
    data = db.get_userdata(userId)

    if request.method == 'POST':
        data["palabra"] = request.form['userpalabra']
        db.set_userdata(userId, data)
        return redirect(url_for('palabras'))

    palabra = data["palabra"]
    return f'''
        <p>Tu user id es {userId}, y la palabra aleatoria es: <b>{escape(palabra)}</b></p>
        <form method="post">
            <p>Nueva palabra <input type=text name=userpalabra>
            <p><input type=submit value=Cambiar>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('userid', None)
    return redirect(url_for('index'))