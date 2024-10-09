from flask import Blueprint
from controllers.client_controller import ClientController

client_bp = Blueprint('client_bp', __name__)

client_bp.route('/clients', methods=['POST'])(ClientController.create_client)
client_bp.route('/clients', methods=['GET'])(ClientController.get_clients)
client_bp.route('/clients/<int:client_id>', methods=['GET'])(ClientController.get_client_id)
client_bp.route('/clients/<int:client_id>', methods=['PUT'])(ClientController.update_client)
client_bp.route('/clients/<int:client_id>', methods=['DELETE'])(ClientController.delete_client) 