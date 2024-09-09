from odoo import models, fields

class MiModelo(models.Model):
    _name = 'mi.modelo'
    _description = 'Descripción de Mi Modelo'

    name = fields.Char(string='Nombre')