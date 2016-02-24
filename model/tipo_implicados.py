#-*- coding: utf-8 -*-

from openerp.osv import fields, osv

class Tipo_Implicados(osv.Model):
	_name = "cein.tipo_implicados"
	_columns = {
		'name': fields.char(string="Tipos de Implicados",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas"),
		'displayname': fields.char(string="Tipos de Implicados",	 size=256, required=False,help="Nombre con acentos a mostrar"),
		'activo': fields.boolean("Activado"),
		'descripcion': fields.text("Description", required=False, help="Descripcion"),
	}
	_defaults = {
		'activo': True,	
	}

	