from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest

from src.validators.subscribers_creator_validator import subscribers_creator_validator

from src.model.repositories.subscribers_repository import SubscribersRepository

from src.controllers.subscribers.subscribers_creator import SubscribersCreator


subs_route_bp = Blueprint("subs_route", __name__)


@subs_route_bp.route("/subscriber", methods=['POST'])
def create_new_subs():
    subscribers_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    subscribers_repo = SubscribersRepository()
    subscribers_creator = SubscribersCreator(subscribers_repo)

    http_response = subscribers_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code
