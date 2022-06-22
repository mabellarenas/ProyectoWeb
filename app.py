from crypt import methods
from itertools import product
from flask import Flask, request, jsonify
from flask import render_template
from flask_migrate import Migrate
from models import db, Producto , Usuario
from flask_cors import CORS, cross_origin



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

# Creacion de ruta por defecto prueba app 
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')


#RUSTA USUARIOS

@app.route('/usuarios' , methods=['GET'])
def getUsuarios():
    user = Usuario.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

@app.route('/usuarios' , methods=['POST'])
def addUsuario():
    user = Usuario()

    user.tipo = request.json.get('tipo')
    user.rut = request.json.get('rut')
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.apellido_paterno = request.json.get('apellido_paterno')
    user.apellido_materno = request.json.get('apellido_materno')
    user.direccion = request.json.get('direccion')
    user.fono = request.json.get('fono')
    user.correo = request.json.get('correo')
    user.constraseña = request.json.get('contraseña')
    user.estado = request.json.get('estado')
    user.suscrito = request.json.get('susctrito')


#RUTA PRODUCTOS

@app.route('/productos' , methods=['GET'])
def getProducto():
    product = Producto.query.all()
    product = list(map(lambda x: x.serialize(), product))
    return jsonify(product),200


@app.route('/productos' , methods=['POST'])   
def addProducto():
    product = Producto()

    product.codigo = request.json.get('codigo')
    product.nombre = request.json.get('nombre')
    product.categoria = request.json.get('categoria') 
    product.valor_venta = request.json.get('valor_venta')
    product.stock = request.json.get('stock')
    product.estado = request.json.get('estado')

    Producto.save(product)
    
    return jsonify(product.serialize()),200

@app.route('/productos/<id>', methods=['DELETE'])
def deleteProductos(id):
    product = Producto.query.get(id)
    Producto.delete(product)
    return jsonify(product.serialize()),200
















#Configuracion de puertos app
if __name__ == '__main__':
    app.run( port=5000 ,debug=True)

