import pandas as pd
import matplotlib.pyplot as plt

estudiante_datos = pd.read_csv('datos\estudiante.csv')
print('ESTUDIANTES')
print(estudiante_datos)

estudiante_asistencias = pd.read_csv('datos\datosasistencia.csv')
print('ASISTENCIAS')
print(estudiante_asistencias)


datos_y_asistencias = pd.merge(estudiante_datos,estudiante_asistencias,  how="right" )
print('ASISTENCIAS Y ESTUDIANTES')
print(datos_y_asistencias)

print('CEDULA = 1161314550')
print(datos_y_asistencias[datos_y_asistencias.cedula == 1161314550])

datos_y_asistencias[datos_y_asistencias.cedula == 1161314550].to_csv('datos\datosreporte_1161314550.csv', index=True)

datos_y_asistencias[datos_y_asistencias.cedula == 1161314550]['materia'].value_counts().plot(kind='bar')
plt.show()