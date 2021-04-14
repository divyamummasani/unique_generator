from flask import Blueprint, request, jsonify
from common import AppConstants
from scripts.handler import unique_token_generator,assign_unique_token,delete_token,re_assigned_token
blueprint = Blueprint("unique_token_blueprint", __name__)


@blueprint.route(AppConstants.unique_generator, methods=['GET'])
def unique_generator():
    try:
        data = unique_token_generator()
        return data
    except Exception as e:
        return jsonify({"status": "failed",
                        "message": str(e)})
@blueprint.route(AppConstants.assigne_unique_token, methods=['POST'])
def assigne_unique_token():
    try:
        input_data = request.get_json()
        data,code = assign_unique_token(input_data)
        return data,code
    except Exception as e:
        return jsonify({"status": "failed",
                        "message": str(e)})
@blueprint.route(AppConstants.re_assigned_token, methods=['POST'])
def re_assigne_unique_token():
    try:
        input_data = request.get_json()
        data = re_assigned_token(input_data)
        return data
    except Exception as e:
        return jsonify({"status": "failed",
                        "message": str(e)})
@blueprint.route(AppConstants.delete_token, methods=['POST'])
def delete_toke():
    try:
        input_data = request.get_json()
        data = delete_token(input_data)
        return data
    except Exception as e:
        return jsonify({"status": "failed",
                        "message": str(e)})

