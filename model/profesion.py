#-*- coding: utf-8 -*-

from openerp.osv import fields, osv

class Profesion(osv.Model):
	_name = "cein.profesion"
	_columns = {
		'name': fields.char(string="Nombre",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas"),
		'displayname': fields.char(string="Profesion",	 size=256, required=True,help="Nombre con acentos a mostrar"),		
		'activo': fields.boolean("Activado"),
		'descripcion': fields.text("Description", required=False, help="Descripcion"),
	}
	_defaults = {
		'activo': True,	
	}

	