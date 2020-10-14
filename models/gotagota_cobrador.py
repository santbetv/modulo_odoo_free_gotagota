# -*- coding: utf-8 -*-

from odoo import fields, models


class GotaGotaCobrador(models.Model):
    _name = 'gotagota.cobrador' #nombre de mi modelo
    _description = 'Cobrador' #describe los datos
    _order = 'name asc' #ordenamiento
    name = fields.Char(string='Nombre', required=True, size=150, index=True)
    last_name = fields.Char(string='Apellido', required=True, size=150, index=True)
    price = fields.Char(string='Valor cobrado', required=True, size=150, index=True)
    # Relacion estatica
    # Indicamos seguimiento a la visibilidad con metodo onchange
    # Orden la accion con track_sequence
    # valor con por defecto en caja default
    tipo_documento = fields.Selection(
        [('1', 'Cédula de ciudadania'),
         ('2', 'NIT'),
         ('3', 'Cédula de extranjeria'),
         ('4', 'Pasaporte'),
         ], string='Tipo de Documento', required=True, index=True, track_visibility='onchange',
        track_sequence=3, default="1")
    documento = fields.Char(string='Numero de documento', required=True, size=150, index=True)
    fecha_prestamo = fields.Date(string='Fecha', required=True)
    #  traigo las ciudades donde yo soy el cobrador de ese modelo
    ciudades_ids = fields.One2many('gotagota.cobrador.ciudad', 'cobrador_id', 'Ciudades', track_visibility='onchange')
    _sql_constraints = {('cobrador_uniq', 'unique(documento)', 'El numero de documento debe ser Único')}



class GotaGotaDepartamento(models.Model):
    _name = 'gotagota.departamento'  # nombre de mi modelo
    _description = 'Departamento'  # describe los datos
    _order = 'name asc'  # ordenamiento
    name = fields.Char(string='Nombre', required=True, size=150, index=True)
    codigo = fields.Char(string='Codigo', required=True, size=150, index=True)
    _sql_constraints = {('departamento_uniq', 'unique(codigo)', 'El codigo del departamento debe ser Único')}

class GotaGotaCiudad(models.Model):
    _name = 'gotagota.ciudad'  # nombre de mi modelo
    _description = 'Ciudad'  # describe los datos
    _order = 'name asc'  # ordenamiento
    name = fields.Char(string='Nombre', required=True, size=150, index=True)
    codigo = fields.Char(string='Codigo', required=True, size=150, index=True)
    # Relación una a muchas
    departamento_id =  fields.Many2one('gotagota.departamento', 'Departamento', required=True)
    cobradores_ids = fields.One2many('gotagota.cobrador.ciudad', 'ciudad_id', 'Cobradores', track_visibility='onchange')
    _sql_constraints = {('ciudad_uniq', 'unique(codigo)', 'El codigo de la ciudad debe ser Único')}

class GotaGotaCobrardorCiudad(models.Model):
    _name = 'gotagota.cobrador.ciudad'  # nombre de mi modelo
    _description = 'Relacion Cobrador Ciudad'  # describe los datos
    cobrador_id = fields.Many2one('gotagota.cobrador', 'Cobrador', required=True, index=True)
    ciudad_id = fields.Many2one('gotagota.ciudad', 'Ciudad', required=True, index=True)
    _sql_constraints = [('cobrador_ciudad_uniq', 'unique(cobrador_id,ciudad_id)',
                         'Ya existe la asociación cobrador y ciudad debe ser Único')]