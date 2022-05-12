from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
app = Flask(__name__)	

@app.route('/hola/')
@app.route('/hola/<name>')
def hello(name=None):
	url_for('static', filename='style.css')
	return render_template('hello.html', name=name)

@app.route('/')
def hola_mundo():
	url_for('static', filename='style.css')
	return 'Hola, Clase de Desarrollo de sistemas multimediales!'

@app.route('/paginaEstatica')
def pagina1():
    return 'Esta es una página estática mostrada en la url /paginaEstatica'

@app.route('/usuario/<nombre>')
def mostrar_perfil(nombre):
    # Muestra un perfil del usuario
    return f'Usuario {escape(nombre)}'

@app.route('/post/<int:post_id>')
def mostrar_post(post_id):
    # Mostrar un post con un ID entero
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def mostrar_subruta(subpath):
    # Mostrar una subruta
    return f'suburuta {escape(subpath)}'

if __name__ == '__main__':
   		#app.run()
   		app.run(debug=True)