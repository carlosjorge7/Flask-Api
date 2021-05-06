from flask import Flask, jsonify, request

app = Flask(__name__)

from productos import productos

@app.route('/bienvenido', methods=['GET'])
def bienvenido():
    return jsonify({'message': 'Bienvenido a mi primera API con Python y Flask'})

@app.route('/productos', methods=['GET'])
def getProductos():
    return jsonify({'productos': productos, 'mensaje': 'status ok 200'})

@app.route('/productos/<int:Id>', methods=['GET'])
def getProducto(Id):
    # productoEncontrado es una lista
    productoEncontrado = [producto for producto in productos if producto['Id'] == Id]
    if len(productoEncontrado) > 0:
        productoEncontrado[0]['nombre'] = request.json['nombre']
        productoEncontrado[0]['precio'] = request.json['precio']
        productoEncontrado[0]['cantidad'] = request.json['cantidad']
        return jsonify({
            'mensaje': 'Producto actualizado',
            'producto': productoEncontrado[0]
        })
    return jsonify({'mensaje': 'Producto no encontrado'})

@app.route('/productos', methods=['POST'])
def createProducto():
    producto = request.json
    productos.append(producto)
    return jsonify({'mensaje': 'Producto creado', "productos": productos})

@app.route('/productos/<int:Id>', methods=['PUT'])
def updateProducto(Id):
    productoEncontrado = [producto for producto in productos if producto['Id'] == Id]
    if len(productoEncontrado) > 0:
        productoEncontrado[0]['nombre'] = request.json['nombre']
        productoEncontrado[0]['precio'] = request.json['precio']
        productoEncontrado[0]['cantidad'] = request.json['cantidad']
        return jsonify({
            'producto actualizado': productoEncontrado[0],
            'productos': productos})
    return jsonify({'mensaje': 'producto no encontrado'})

@app.route('/productos/<int:Id>', methods=['DELETE'])
def deleteProducto(Id):
    productoEncontrado = [producto for producto in productos if producto['Id'] == Id]
    if len(productoEncontrado) > 0:
        productos.remove(productoEncontrado[0])
        return jsonify({
            'mensaje': 'producto eliminado',
            'productos': productos})
    return jsonify({'mensaje': 'producto no encontrado'})

if __name__ == '__main__':
    app.run(debug=True, port=4000)

# Flask - > framwork, jsonify -> Para devolver jsons, Request - > Para los post, recibir datos