#-*- coding: utf-8 -*-

from openerp.osv import fields, osv


class Procedimiento(osv.Model):
	_name = "cein.procedimiento"
	_rec_name = "denuncia_id"
	
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
		'state': fields.selection([('solicitado','Solicitado'),('asignado','Asignado'),('finalizado','Finalizado')], required=True, string="Estado", index=True),
		'tipo_procedimiento_id': fields.many2one('cein.tipo_procedimiento','Tipo Procedimiento', required=True),
		'denuncia_id': fields.many2one('cein.denuncia','Número de Denuncia', required=True),
		'implicado_id': fields.many2one('cein.implicado','Implicado', required=True),		
		'solicitud': fields.text("Solicitud", required=False, help="Descripcion de la solicitud"),
		'reporte': fields.text("Reporte de investigación", required=False, help="Breve resumen de la investigacion"),
		'creador': fields.function(_get_metadata_dic,type="char",string="Creado por", store=False),
		'creacion_date': fields.function(_get_metadata_dic,type="date",string="Fecha creacion", store=False),
		'modificador': fields.function(_get_metadata_dic,type="char",string="Modificador por", store=False),
		'modificacion_date': fields.function(_get_metadata_dic,type="date",string="Fecha modificacion", store=False),
		'responsable_id': fields.many2one('res.users',string="Responsable", required=True),		
	}

	_defaults = {
		'state': 'solicitado',
	}

	