#-*- coding: utf-8 -*-

from openerp.osv import fields, osv

class Tipo_Delitos(osv.Model):
	_name = "cein.tipo_delitos"
	_columns = {
		'name': fields.char(string="Nombre del Delito",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas"),
		'displayname': fields.char(string="Nombre a mostrar",	 size=256, required=False,help="Nombre con acentos a mostrar"),
		'activo': fields.boolean("Activado"),
		'descripcion': fields.text("Description corta del delito", required=False, help="Descripcion"),
	}
	_defaults = {
		'activo': True,	
	}

	