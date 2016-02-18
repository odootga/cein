#-*- coding: utf-8 -*-

from openerp.osv import fields, osv

class Persona(osv.Model):
	_name = "cein.persona"
	_rac_name='name'
	_columns = {
		'name': fields.char(string="Apellidos y Nombres",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas"),
		'displayname': fields.char(string="Apellidos y Nombres",	 size=256, required=True,help="Nombre con acentos a mostrar"),
		'nacionalidad_id': fields.many2one('cein.nacionalidad','Nacionalidad'),
		'escolaridad_id': fields.many2one('cein.escolaridad','escolaridad'),
		'estadocivil_id': fields.many2one('cein.estadocivil','estadocivil'),
		'ocupacion_id': fields.many2one('cein.ocupacion','ocupacion'),
		'profesion_id': fields.many2one('cein.profesion','profesion'),
		'raza_id': fields.many2one('cein.raza','raza'),
		'tipo_documento_id': fields.many2one('cein.tipo_documento','tipo_documento'),

		'activo': fields.boolean("Activado"),
		'descripcion': fields.text("Description", required=False, help="Descripcion"),
	}
	_defaults = {
		'activo': True,	
	}

	
