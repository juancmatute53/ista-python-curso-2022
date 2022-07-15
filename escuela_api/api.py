from calendar import c
from cmath import pi
from doctest import OutputChecker
from flask import Flask, request
import csv
import json

app = Flask(__name__)


@app.route('/datos_leer_estudiante')
def datos_leer_estudiante():
    with open('datos\estudiante.csv') as archivo:
        lector = csv.reader(archivo)
        next(lector)
        list_estudiante = []
        for fila in lector:
            list_estudiante.append({
                'cedula': fila[0],'primer_apellido': fila[1],'segundo_apellido': fila[2],'primer_nombre': fila[3],'segundo_nombre': fila[4]
            })
    return json.dumps(sorted(list_estudiante, key=lambda x: x['cedula']))


@app.route('/datos_crear_asistencia', methods=['POST'])
def datos_crear_asistencia():
    with open('datos\listado_de_asistencia.csv', 'a', newline='') as archivo:
        wirte = csv.writer(archivo, delimiter=',')
        wirte.writerow([request.json['cedula'], request.json['materia'],request.json['fecha_anio'], request.json['fecha_mes'], request.json['fecha_dia']])
    return '<h1>REGISTRO COMPLETO</h1>'


@app.route('/buscar_dato_repetido/<cedula>')
def buscar_dato_repetido(cedula):
    with open('datos\estudiante.csv') as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for fila in lector:
            if fila[0] == cedula:
                msj = '<h1>DATO EXITE</h1>'
            else:
                msj = '<h1>DATO NO EXITE</h1>' 
    return msj


if __name__ == '__main__':
    app.run(debug=True)
        



