from enrutamiento import app
from flask import render_template

@app.route('/')          #El decorador "@" asocia esta ruta con la función inmediatamente siguiente.
def hola_mundo():
    return 'Hola Mundo!'  #Devuelve la cadena '¡Hola Mundo!' como respuesta.

@app.route('/dojo')     #Sentencias import, tal vez algunas otras rutas??
def dojo():
    return "¡Dojo!"       # # app.run(debug=True) debería ser la última sentencia??

@app.route('/say/<name>') #Para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def say(name):
    print(name)
    return "¡Hola, " + name + "!"

@app.route('/repeat/<int:numero>/<palabra>')
def index(numero, palabra):
    return render_template("index.html", frase=palabra, times=numero)

@app.errorhandler(404)     #Establecimos el estado 404 explicitamente.
def page_not_found(e):
    return "NOT FOUND ERROR 404"        #return render_template('404.html'),404
