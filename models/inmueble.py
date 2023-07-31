from db.db_utils import execute_query


class ConsultaError(Exception):
    pass


def consultar_inmuebles(year=None, city=None, label=None):
    try:
        # Construir la consulta SQL según los filtros proporcionados
        query = "SELECT P.address, P.year, P.description, P.price, P.city, SH.update_date, S.label FROM property P INNER JOIN (SELECT property_id, MAX(update_date) AS max_update_date FROM status_history GROUP BY property_id) MaxDates ON P.id = MaxDates.property_id INNER JOIN status_history SH ON P.id = SH.property_id AND SH.update_date = MaxDates.max_update_date INNER JOIN status S ON S.id = SH.status_id WHERE S.label IN ('Inmueble vendido', 'Inmueble publicado en venta', 'Inmueble publicado en preventa')"
        args = []
        if year is not None:
            query += " AND year = %s"
            args.append(year)
        if city is not None:
            query += " AND city = %s"
            args.append(city)
        if label is not None:
            query += " AND label = %s"
            args.append(label)

        # Ejecutar la consulta a la base de datos
        results = execute_query(query, args)

        return results
    except Exception as e:
        raise ConsultaError(e, 'Error al consultar inmuebles')
