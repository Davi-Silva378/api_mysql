from flask import jsonify, request
from repositories.client_repository import ClientRepository

class ClientController:

    @staticmethod
    def create_client():
        data = request.get_json()
        ClientRepository.create_client(data['name'], data['email'], data['phone'])
        return jsonify({'message': 'Client created successfully!'}), 201
    
    @staticmethod
    def get_clients():
        clients = ClientRepository.get_clients()
        return jsonify(clients), 200
    
    @staticmethod
    def get_client_id(client_id):
        client = ClientRepository.get_client_id(client_id)
        if client:
            return jsonify(client), 200
        return jsonify({'message': 'Client not found'}), 404
    
    @staticmethod
    def update_client(client_id):
        data = request.get_json()
        ClientRepository.update_client(client_id, data['name'], data['email'], data['phone'])
        return jsonify({'message': 'Client updated successfully!'}), 200
    
    @staticmethod
    def delete_client(client_id):
        ClientRepository.delete_clients(client_id)
        return jsonify({'message': 'Client deleted successfully!'}), 200
