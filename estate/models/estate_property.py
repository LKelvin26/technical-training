from odoo import models, fields
from datetime import timedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Title', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    date_availability = fields.Date(string='Availability Date', copy=False, default=lambda self: fields.Date.today() + timedelta(days=90))
    bedrooms = fields.Integer(string='Bedrooms', default=2)