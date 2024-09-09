from odoo import models, fields

class MiModelo(models.Model):
    _name = 'mi.modelo'
    _description = 'Descripción del modelo'

    name = fields.Char(string='Nombre')
    description = fields.Text(string='Descripción')
