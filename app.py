from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
import os, json
#SQL ALcbhemy
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config	

app = Flask(__name__)

app.config.from_object(config)
#Bootstrap(app)	
db = SQLAlchemy(app)

libros = {}
nuevo_id=0
archivo = os.path.join(app.static_folder, 'datos', 'libros.json')
def guardar_libros(libros):
	global archivo
	with open(archivo, 'w') as outfile:
		json.dump(libros, outfile)

@app.route('/')
def principal():
	global archivo
	global libros
	if not os.path.exists(archivo):
		guardar_libros(libros)
	with open(archivo) as json_file:
		libros = json.load(json_file)
	return render_template("libros/libros.html",libros=libros)

@app.route("/libro/<int:id_libro>/")
def mostrar_libro(id_libro):
	global archivo
	libro_elegido={}
	with open(archivo) as json_file:
		libros = json.load(json_file)
	for key, value in libros.items():
		if libros[key]['id']==id_libro:
			libro_elegido=value
	return render_template("libros/ver_libro.html", libro=libro_elegido)

from flask import request, redirect
@app.route("/libros/libro/", methods=["GET", "POST"])
@app.route("/libros/libro/<int:libro_e>/", methods=["GET", "POST"])
def form_libro(libro_e=None):
	libro={}
	global archivo
	if request.method == "POST":
		global nuevo_id
		global libros
		with open(archivo) as json_file:
			libros = json.load(json_file)
		nuevo_id=len(libros)+1
		if libro_e:
			nuevo_id = libro_e
		else:
			nuevo_id += 1
		libro["id"] = nuevo_id
		libro["titulo"] = request.form['titulo']
		libro["descripcion"] = request.form['descripcion']
		
		libros[libro["id"]] = libro
		
		guardar_libros(libros)
		return redirect(url_for("principal"))
		#print(libros)
	else:
		if libro_e:
			with open(archivo) as json_file:
				libros = json.load(json_file)
			for key, value in libros.items():
				#print(libros[key]['id'])
				if libros[key]['id']==libro_e:
					libro_e=value
	return render_template("libros/form_libro.html", libro_e=libro_e)



if __name__ == '__main__':
   		#app.run()
   		app.run(debug=True)