#-*- coding: utf-8 -*-

from openerp.osv import fields, osv

class Escolaridad(osv.Model):
	_name = "cein.escolaridad"
	_columns = {
		'name': fields.char(string="Nombre",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas"),
		'displayname': fields.char(string="Nombre a Mostrar",	 size=256, required=False,help="Nombre con acentos a mostrar"),
		'codlegado': fields.integer('Codigo Legado',required=True, help="Codigo legado"),
		'activo': fields.boolean("Activado"),
		'descripcion': fields.text("Description", required=False, help="Descripcion"),
	}
	_defaults = {
		'activo': True,	
	}

	_sql_constraints = [
	('cod_legado_unique',	
	'UNIQUE(codlegado)',
	'¡No se permite duplicar ID legados!'),
	('name_unique',	
	'UNIQUE(name)',
	'¡No se permite duplicar Nombre!'),
	('displayname_unique',	
	'UNIQUE(displayname)',
	'¡No se permite duplicar displayname!'),
]