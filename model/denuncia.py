#-*- coding: utf-8 -*-
from datetime import date, datetime, timedelta

import time

from openerp import fields, models, api


class Denuncia(models.Model):
	_name = "cein.denuncia"

	#este campo sirve para dejar una bitacora que pueda servir a los fiscales a agregar procedimientos a denuncias comodamente
	def computed_get_hechos(self):
		self.computed_resumen_hechos = ""
		contador = 0

		for hecho in self.relatoshechos_id:	
			self.computed_resumen_hechos += "<strong>Hecho #"+str(contador+1)+": </strong>"+str(hecho.fechahora) + "\n"
			self.computed_resumen_hechos +=  hecho.relato+"\n"
			self.computed_resumen_hechos += "<br /><strong>Delitos implicados: </strong>"

			#este es un contador para saber cuantos delitos implicados hay
			contador_delitos = len(hecho.delitosimplicados_id)
			for delitosimplicado in hecho.delitosimplicados_id:
				self.computed_resumen_hechos += delitosimplicado.delitosimplicados.name
				if contador_delitos !=1:
					self.computed_resumen_hechos += ", "
				contador_delitos-=1

			self.computed_resumen_hechos +="<br /><br />"
			contador+=1




	name= fields.Char(string="Codigo Oficial",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas")
	code_temporal= fields.Char(string="Codigo Temporal",	 size=256, required=True,help="Nombre con acentos a mostrar")
	tipo_denuncia_id= fields.Many2one('cein.tipo_denuncia','Tipo de Denuncia')
	fecha_denuncia= fields.Date('Fecha Toma de Denuncia', required=False, default=fields.date.today())
	state= fields.Selection([('generada','Ingresada'),('oficial','En Proceso Legal'),('cerrada','Cerrada')], string="Estado", index=True, default='generada')
	relacion_id= fields.One2many('cein.implicado','name_id','Implicados en la Denuncia')
	relatoshechos_id= fields.One2many('cein.hechos','hechos_id','Relato de Hechos, Datos Geográficos, Fecha y Hora del Suceso')
	activo= fields.Boolean("Activado", default=True)
	computed_resumen_hechos = fields.Html("Resumen de los hechos",compute="computed_get_hechos")
	procedimiento_ids= fields.One2many('cein.procedimiento','denuncia_id','Procedimiento de la denuncia')

class Implicados(models.Model):
	_name = "cein.implicado"
	_rec_name = 'nombre'

	name_id= fields.Many2one('cein.denuncia','Many2one obligado',help="obligsado por one2many, no necesario aparezca en vista")
	nombre = fields.Many2one('cein.persona','Relacion Persona')
	relacion= fields.Many2one('cein.tipo_implicados','Implicación en la denuncia')
	

class Hechos(models.Model):
	_name = "cein.hechos"	
	hechos_id= fields.Many2one('cein.denuncia','Many2one obligado',help="obligado por one2many, no necesario aparezca en vista")
	relato= fields.Text('Relato de Hechos', required=False)
	observaciones= fields.Text('Observaciones', required=False)
	comentarios= fields.Text('Comentarios', required=False)
	delitosimplicados_id= fields.One2many('cein.delitosimplicado','name_id','Delitos Implicados')
	fechahora= fields.Datetime('Fecha del Hecho', required=False)
	direccion= fields.Text("Dirección de Lugar de los Hechos", required=False, help="Descripcion del departamento")
	municipio_id= fields.Many2one('cein.geomunicipios','Municipio', required=True)					
	
	

class  Delitos_implicados(models.Model):
	_name = "cein.delitosimplicado"	
	name_id = fields.Many2one('cein.hechos','Many2one obligado',help="obligado por one2many, no necesario aparezca en vista")
	delitosimplicados = fields.Many2one('cein.tipo_delitos','Tipos de Delito')