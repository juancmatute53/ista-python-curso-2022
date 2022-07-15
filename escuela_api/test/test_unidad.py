from asyncio.windows_events import NULL
from escuela_api import api

def test_lista_estudiante():
    assert api.buscar_dato_repetido('1161314550') == '<h1>DATO EXITE</h1>'