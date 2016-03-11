#-*- coding: utf-8 -*-
from datetime import date, datetime, timedelta

import time

from openerp import fields, models, api


class Procedimiento(models.Model):
	#tomado de modulo mail
	_inherit = ['mail.thread']

	_name = "cein.procedimiento"
	_rec_name = "denuncia_id"
	
	@api.one
	def _get_metadata_dic(self):		
		for valor in self:
			self.creador = self.create_uid.name
			self.creacion_date = self.create_date
			self.modificador = self.write_uid.name
			self.modificacion_date = self.write_date
	
		#tomado del modulo mail
		#######################################################################################################
	notify_email= fields.Selection([
            ('none', 'Nunca'),
            ('always', 'Todos los mensajes'),
            ], 'Receive Inbox Notifications by Email', required=True,
            oldname='notification_email_send',
            help="Autorizacion para recibir notificaciones via correo electronico:\n"
                    "- Nunca: no se enviaran emails\n"
                    "- Todos los mensajes: se enviara un email para cada nueva entrada")
	#######################################################################################################
	state= fields.Selection([('solicitado','Solicitado'),('asignado','Asignado'),('finalizado','Finalizado')], required=True, string="Estado", index=True)
	tipo_procedimiento_id= fields.Many2one('cein.tipo_procedimiento','Tipo Procedimiento', required=True)
	denuncia_id= fields.Many2one('cein.denuncia','Número de Denuncia', required=True)
	implicado_id= fields.Many2one('cein.implicado','Implicado', required=True)
	solicitud= fields.Text("Solicitud", required=False, help="Descripcion de la solicitud")
	reporte= fields.Text("Reporte de investigación", required=False, help="Breve resumen de la investigacion")
	creador= fields.Char(compute="_get_metadata_dic", string="Creado por", store=False)
	creacion_date= fields.Datetime(compute="_get_metadata_dic", string="Fecha creacion", store=False)
	modificador= fields.Char(compute="_get_metadata_dic",string="Modificador por", store=False)
	modificacion_date= fields.Datetime(compute="_get_metadata_dic",string="Fecha modificacion", store=False)
	responsable_id= fields.Many2one('res.users',string="Responsable", required=False)
	

	_defaults = {
		'state': 'solicitado',
		'notify_email': lambda *args: 'always',
	}

	