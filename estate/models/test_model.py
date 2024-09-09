from odoo import models, fields

class TestModel(models.Model):
    _name = 'test.model'
    _description = 'Descripción de Mi Modelo'

    name = fields.Char(string='Nombre')
    description = fields.Text(string='Descripción')
    postcode = fields.Char(string='Código Postal')
    date_availability = fields.Date(string='Fecha de Disponibilidad',default=fields.Datetime.now)
    expected_price = fields.Float(string='Precio Esperado')
    selling_price = fields.Float(string='Precio de Venta')
    bedrooms = fields.Integer(string='Número de Habitaciones',default=2)
    living_area = fields.Integer(string='Área de Estar')
    facades = fields.Integer(string='Número de Fachadas')
    garage = fields.Boolean(string='Garage')
    garden_area = fields.Integer(string='Área del Jardín')
    garden_orientation = fields.Selection([
        ('north', 'Norte'),
        ('south', 'Sur'),
        ('east', 'Este'),
        ('west', 'Oeste')
    ], string='Orientación del Jardín')
    status = fields.Selection([
        ('Nuevo'),
        ('Usado?')
    ])

