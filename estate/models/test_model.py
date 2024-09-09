from odoo import models, fields

from odoo import models, fields

class TestModel(models.Model):
    _name = 'test.model'
    _description = 'Reservación de Hotel'

    name = fields.Char(string='Nombre del Cliente', required=True)
    description = fields.Text(string='Notas Adicionales')
    date_reservation = fields.Date(string='Fecha de la Reserva', default=fields.Datetime.now, required=True)
    expected_price = fields.Float(string='Precio Estimado', required=True)
    selling_price = fields.Float(string='Precio Final', required=True)
    bedrooms = fields.Integer(string='Número de Habitaciones', default=1, required=True)
    status = fields.Selection([
        ('new', 'Nueva'),
        ('confirmed', 'Confirmada'),
        ('canceled', 'Cancelada'),
    ], string='Estatus de la Reservación', required=True, default='new', copy=False)
