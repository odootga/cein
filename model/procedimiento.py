#-*- coding: utf-8 -*-

from openerp.osv import fields, osv


class Procedimiento(osv.Model):
	_name = "cein.procedimiento"
	
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
		'name': fields.many2one('cein.tipo_procedimiento','Tipo Procedimiento', required=True),
		'denuncia_id': fields.many2one('cein.denuncia','Número de Denuncia', required=True),
		'implicado_id': fields.many2one('cein.implicado','Implicado', required=True),
		'state': fields.selection([('solicitado','Solicitado'),('ejecutado','Realizada')], string="Estado", required=True, default='solicitado'),
		'solicitud': fields.text("Description", required=False, help="Descripcion de la solicitud"),
		'creador': fields.function(_get_metadata_dic,type="char",string="Creado por", store=False),
		'creacion_date': fields.function(_get_metadata_dic,type="date",string="Fecha creacion", store=False),
		'modificador': fields.function(_get_metadata_dic,type="char",string="Modificador por", store=False),
		'modificacion_date': fields.function(_get_metadata_dic,type="date",string="Fecha modificacion", store=False),
	}
	_defaults = {
		'activo': True,	
	}

	