from flask import Blueprint
from app.controllers import leads_controler

bp_leads = Blueprint("bp_leads", __name__, url_prefix="/leads")

bp_leads.get("")(leads_controler.get_leads)
bp_leads.post("")(leads_controler.create_leads)
bp_leads.patch("")(leads_controler.update_lead)
bp_leads.delete("")(leads_controler.delete_lead)
