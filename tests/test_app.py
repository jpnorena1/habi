import pytest
from app import app
from models.inmueble import consultar_inmuebles


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Pruebas del modelo


def test_consultar_inmuebles_sin_filtros():
    results = consultar_inmuebles()
    assert isinstance(results, list)
    # Agrega más aserciones según los resultados esperados


def test_consultar_inmuebles_con_filtros():
    results = consultar_inmuebles(city='bogota', year=20222)
    assert isinstance(results, list)
    # Agrega más aserciones según los resultados esperados

# Pruebas del controlador


def test_consulta_inmuebles_controller_sin_filtros(client):
    response = client.get('/inmuebles')
    assert response.status_code == 400
    assert b'Se requiere al menos un filtro' in response.data


def test_consulta_inmuebles_controller_con_filtros(client):
    response = client.get('/inmuebles?city=bogota&year=2000')
    assert response.status_code == 200
    # Agrega más aserciones según la respuesta esperada
