# -*- coding: utf-8 -*-

from odoo import fields, models


class GotaGotaPrestamo(models.Model):
    _name = 'gotagota.prestamo' #nombre de mi modelo
    _description = 'Prestamo' #describe los datos
    _order = 'name asc' #ordenamiento
    name = fields.Char(string='Descripción', required=True, size=150)
    fecha_prestamo = fields.Date(string='Fecha', required=True)