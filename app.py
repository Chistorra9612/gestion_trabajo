from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from models import db, Cliente
from database import create_app

app = create_app()
api = Api(app)

class ClienteResource(Resource):
    def get(self, cliente_id):
        cliente = Cliente.query.get(cliente_id)
        if cliente:
            return jsonify({'id': cliente.id, 'nombre': cliente.nombre, 'email': cliente.email, 'telefono': cliente.telefono, 'direccion': cliente.direccion})
        return jsonify({'message': 'Cliente no encontrado'}), 404

    def post(self):
        data = request.get_json()
        nuevo_cliente = Cliente(
            nombre=data['nombre'],
            email=data['email'],
            telefono=data.get('telefono', ''),
            direccion=data.get('direccion', '')
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        return jsonify({'message': 'Cliente creado exitosamente'}), 201

    def put(self, cliente_id):
        cliente = Cliente.query.get(cliente_id)
        if cliente:
            data = request.get_json()
            cliente.nombre = data['nombre']
            cliente.email = data['email']
            cliente.telefono = data.get('telefono', '')
            cliente.direccion = data.get('direccion', '')
            db.session.commit()
            return jsonify({'message': 'Cliente actualizado exitosamente'})
        return jsonify({'message': 'Cliente no encontrado'}), 404

    def delete(self, cliente_id):
        cliente = Cliente.query.get(cliente_id)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()
            return jsonify({'message': 'Cliente eliminado exitosamente'})
        return jsonify({'message': 'Cliente no encontrado'}), 404

api.add_resource(ClienteResource, '/cliente', '/cliente/<int:cliente_id>')

if __name__ == '__main__':
    app.run(debug=True)
