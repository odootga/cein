#-*- coding: utf-8 -*-

from openerp.osv import fields, osv


class Tipo_Denuncia(osv.Model):
	_name = "cein.tipo_denuncia"
	
	def _get_metadata_dic(self, cr, uid,ids,field,arg,context=None):
		result = {}
		#print '***'*40
		#print self
		#print cr
		#print uid
		#print ids
		#print field
		#print arg
		#print context
		for valor in self.browse(cr,uid,ids, context=context):
			if field == "creador":
				result[valor.id] = valor.create_uid.name
			elif field == "modificador":
				result[valor.id] = valor.write_uid.name
			elif field == "modificacion_date":
				result[valor.id] = valor.write_date
			elif field == "creacion_date":
				result[valor.id] = valor.create_date
			
		return result
	
	_columns = {
		'name': fields.char(string="Nombre",	 size=256, required=True,help="Nombre"),
		'codlegado': fields.char('Codigo',size=20, required=True, help="Codigo legado"),
		'active': fields.boolean("Activado"),
		'descripcion': fields.text("Description", required=False, help="Descripcion del departamento"),
		'creador': fields.function(_get_metadata_dic,type="char",string="Creado por", store=False),
		'creacion_date': fields.function(_get_metadata_dic,type="date",string="Fecha creacion", store=False),
		'modificador': fields.function(_get_metadata_dic,type="char",string="Modificador por", store=False),
		'modificacion_date': fields.function(_get_metadata_dic,type="date",string="Fecha modificacion", store=False),
	}
	_defaults = {
		'activo': True,	
	}

	_sql_constraints = [
	('cod_legado_unique',	
	'UNIQUE(codlegado)',
	'¡No se permite duplicar codigos legados!'),
	('name_unique',	
	'UNIQUE(name)',
	'¡No se permite duplicar Nombre!'),
]