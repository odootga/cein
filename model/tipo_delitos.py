#-*- coding: utf-8 -*-

from openerp.osv import fields, osv

class Tipo_Delitos(osv.Model):
	_name = "cein.tipo_delitos"
	_columns = {
		'name': fields.char(string="Nombre del Delito",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas"),
		'capitulo': fields.char(string="Capitulo",	 size=500, required=False,help="Capito en codigo penal"),
		'modalidad': fields.char(string="Modalidad",	 size=500, required=False,help="Modalidad"),
		'modalidad_articulo': fields.char(string="Modalidad Articulo",	 size=500, required=False,help="Modalidad"),
		'caracteristica_articulo': fields.char(string="Caracteristica Articulo",	 size=200, required=False,help="Caracteristica articulo"),

		'activo': fields.boolean("Activado"),
		'descripcion': fields.text("Description corta del delito", required=False, help="Descripcion"),
	}
	_defaults = {
		'activo': True,	
	}

	#name,capitulo,modalidad,modalidad_articulo,descripcion,caracteristica_articulo