from datetime import datetime
from http import HTTPStatus
import re
from turtle import update
from flask import jsonify, request, current_app
from itsdangerous import json
from sqlalchemy.exc import IntegrityError
from app.models.lead_model import LeadModel
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy import desc


def create_leads():
    try:
        data = request.get_json()

        if not re.fullmatch("^\([1-9]{2}\)[0-9]{5}\-[0-9]{4}$", data["phone"]):
            return {"Error": "Telefone Inválido"}
        leads = LeadModel(name=data["name"],
                          email=data["email"], phone=data["phone"])

        current_app.db.session.add(leads)
        current_app.db.session.commit()
        return jsonify(leads), HTTPStatus.CREATED
    except IntegrityError:

        return {"Error": "Email ou Telefone já cadastrados"}, HTTPStatus.BAD_REQUEST


def get_leads():
    session: Session = current_app.db.session

    base_query = session.query(LeadModel)
    print(base_query)
    leads = base_query.order_by(desc(LeadModel.visits)).all()
    if not leads:
        return {"Error" - "Nenhum dado encontrado"}
    return jsonify(leads), HTTPStatus.OK


def update_lead():

    data = request.get_json()

    leads = LeadModel.query.filter_by(email=data["email"]).one()

    if not leads:
        return {"Error" - "Nenhum dado encontrado"}

    updated = {"visits": leads.visits + 1, "last_visit": datetime.now()}

    for key, value in updated.items():
        setattr(leads, key, value)

    current_app.db.session.add(leads)
    current_app.db.session.commit()
    return ""


def delete_lead():
    try:
        data = request.get_json()

        leads = LeadModel.query.filter_by(email=data["email"]).one()

        current_app.db.session.delete(leads)
        current_app.db.session.commit()

        return "", HTTPStatus.NO_CONTENT
    except NoResultFound:
        return {"Error": "Email não encontrado"}, HTTPStatus.NOT_FOUND
