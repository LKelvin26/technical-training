from datetime import datetime, timedelta
from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Name')
    bedrooms = fields.Integer(string='Number of Bedrooms', default=2)
    date_availability = fields.Date(string='Date of Availability', default=lambda self: fields.Date.today() + timedelta(days=90))
    selling_price = fields.Float(string='Selling Price')
    postcode = fields.Integer(string="Post Code")
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='State', required=True, default='new', copy=False)
    
    # New fields
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)

    tag_ids = fields.Many2many('estate.property.tag', string='Tags')