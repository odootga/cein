#-*- coding: utf-8 -*-

from openerp.osv import fields, osv

class Tipo_Documento(osv.Model):
	_name = "cein.tipo_documento"
	_columns = {
		'name': fields.char(string="Nombre",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas"),
		'displayname': fields.char(string="Tipo Documento",	 size=256, required=True,help="Nombre con acentos a mostrar"),
		'activo': fields.boolean("Activado"),
		'descripcion': fields.text("Description", required=False, help="Descripcion"),
	}
	_defaults = {
		'activo': True,	
	}

	