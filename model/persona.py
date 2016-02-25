#-*- coding: utf-8 -*-
from datetime import date, datetime, timedelta

import time

from openerp import fields, models, api


class Persona(models.Model):
	_name = "cein.persona"

	name= fields.Char(string="Nombres y apellidos",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas")
	displayname=  fields.Char(string="Nombre a mostrar",	 size=256, required=False,help="Nombre con acentos a mostrar")
	identidad= fields.Char(string="Identidad",	 size=15, required=False,help="Identificacion de la persona")	
	nacionalidad_id=  fields.Many2one('cein.nacionalidad','Nacionalidad')
	escolaridad_id=  fields.Many2one('cein.escolaridad','Escolaridad')
	estadocivil_id=  fields.Many2one('cein.estadocivil','Estado civil')
	ocupacion_id=  fields.Many2one('cein.ocupacion','Ocupacion')
	profesion_id=  fields.Many2one('cein.profesion','Profesion')
	raza_id=  fields.Many2one('cein.raza','Raza')
	tipo_documento_id=  fields.Many2one('cein.tipo_documento','Tipo documento de identidad')

	activo= fields.Boolean("Activado")
	descripcion = fields.Text("Description", required=False, help="Descripcion")

	_defaults = {
		'activo': True,	
		'nacionalidad_id': 1,
	}

	
