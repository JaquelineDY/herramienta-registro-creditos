from flask import request, jsonify, render_template
from . import db
from .models import Credito
from flask import current_app as app

# Ruta raíz
@app.route("/")
def index():
    return render_template("index.html")

# Creación de crédito
@app.route("/creditos", methods=["POST"])
def crear_credito():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No se recibieron datos JSON"}), 400
        
        # Validar campos requeridos
        campos_requeridos = ["cliente", "monto", "tasa_interes", "plazo", "fecha_otorgamiento"]
        campos_faltantes = [campo for campo in campos_requeridos if campo not in data or data[campo] is None]
        
        if campos_faltantes:
            return jsonify({
                "error": f"Faltan campos requeridos: {', '.join(campos_faltantes)}"
            }), 400
        
        nuevo = Credito(
            cliente=data["cliente"],
            monto=float(data["monto"]),
            tasa_interes=float(data["tasa_interes"]),
            plazo=int(data["plazo"]),
            fecha_otorgamiento=data["fecha_otorgamiento"]
        )
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"mensaje": "Crédito creado exitosamente", "id": nuevo.id}), 201
    
    except ValueError as e:
        return jsonify({"error": "Error en los tipos de datos. Verifique que monto y tasa_interes sean números y plazo sea entero"}), 400
    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

# Listado de créditos
@app.route("/creditos", methods=["GET"])
def listar_creditos():
    creditos = Credito.query.all()
    resultado = [
        {
            "id": c.id,
            "cliente": c.cliente,
            "monto": c.monto,
            "tasa_interes": c.tasa_interes,
            "plazo": c.plazo,
            "fecha_otorgamiento": c.fecha_otorgamiento
        }
        for c in creditos
    ]
    return jsonify(resultado)

# Edición de crédito
@app.route("/creditos/<int:id>", methods=["PUT"])
def editar_credito(id):
    try:
        credito = Credito.query.get_or_404(id)
        data = request.json
        
        if not data:
            return jsonify({"error": "No se recibieron datos JSON"}), 400
        
        # Actualización solo los campos que se enviaron
        if "cliente" in data:
            credito.cliente = data["cliente"]
        if "monto" in data:
            credito.monto = float(data["monto"])
        if "tasa_interes" in data:
            credito.tasa_interes = float(data["tasa_interes"])
        if "plazo" in data:
            credito.plazo = int(data["plazo"])
        if "fecha_otorgamiento" in data:
            credito.fecha_otorgamiento = data["fecha_otorgamiento"]
        
        db.session.commit()
        return jsonify({"mensaje": "Crédito actualizado exitosamente"})
    
    except ValueError as e:
        return jsonify({"error": "Error en los tipos de datos. Verifique que monto y tasa_interes sean números y plazo sea entero"}), 400
    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

# Eliminación de crédito
@app.route("/creditos/<int:id>", methods=["DELETE"])
def eliminar_credito(id):
    credito = Credito.query.get_or_404(id)
    db.session.delete(credito)
    db.session.commit()
    return jsonify({"mensaje": "Crédito eliminado"})
