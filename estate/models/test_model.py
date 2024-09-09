from odoo import models, fields

class TestModel(models.Model):
    _name = 'test_model'
    _description = 'Descripción de Mi Modelo'

    name = fields.Char(string='Nombre')
   
    
