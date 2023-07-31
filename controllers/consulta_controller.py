from flask import Blueprint, request, jsonify
from models.inmueble import consultar_inmuebles, ConsultaError

bp = Blueprint('consulta', __name__)

@bp.route('/inmuebles', methods=['GET'])
def consultar_inmuebles_controller():
    try:
        # Obtener los filtros desde la URL (parámetros)
        year = request.args.get('year', type=int)
        city = request.args.get('city', type=str)
        label = request.args.get('label', type=str)

        # Validar los filtros
        if year is None and city is None and label is None:
            raise ConsultaError('Se requiere al menos un filtro')
    
        # Consultar los inmuebles utilizando el modelo
        results = consultar_inmuebles(year, city, label)

        # Devolver los resultados en formato JSON
        return jsonify(results)
    except ConsultaError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Ha ocurrido un error en el servidor'}), 500
