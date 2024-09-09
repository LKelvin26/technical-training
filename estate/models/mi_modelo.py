from odoo import models, fields

class MiModelo(models.Model):
    _name = 'mi.modelo'
    _description = 'Descripción de Mi Modelo'

    name = fields.Char(string='Nombre')
    description =fields.Text()
    postcode = fields.Char()
    date_availability =fields.Float()
    expected_price = fields.Date()
    selling_price = fields.Float()
    bedrooms = fields.integer()
    living_area = fields.integer()
    facades = fields.integer()
    garage = fields.Boolean()
    garden_area = fields.integer()
    garden_orientation=fields.Selection()
    
