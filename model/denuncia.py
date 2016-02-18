#-*- coding: utf-8 -*-
from datetime import date, datetime, timedelta

import time

from openerp import fields, models, api


class Denuncia(models.Model):
	_name = "cein.denuncia"
	name= fields.Char(string="Codigo Oficial",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas")
	code_temporal= fields.Char(string="Codigo Temporal",	 size=256, required=True,help="Nombre con acentos a mostrar")
	tipo_denuncia_id= fields.Many2one('cein.tipo_denuncia','Tipo de Denuncia')
	fecha_denuncia= fields.Date('Fecha Toma de Denuncia', required=False)
	state= fields.Selection([('generada','Ingresada'),('oficial','En Proceso Legal'),('cerrada','Cerrada')], string="Estado", index=True, default='generada')
	relacion_id= fields.One2many('cein.implicado','name_id','Implicados en la Denuncia')
	relatoshechos_id= fields.One2many('cein.hechos','hechos_id','Relato de Hechos, Datos Geográficos, Fecha y Hora del Suceso')
	activo= fields.Boolean("Activado", default=True)

	

class Implicados(models.Model):
	_name = "cein.implicado"
	name_id= fields.Many2one('cein.denuncia','Many2one obligado',help="obligado por one2many, no necesario aparezca en vista")
	nombre = fields.Many2one('cein.persona','Relacion Persona')
	relacion= fields.Many2one('cein.tipo_implicados','Implicación en la denuncia')
	

class Hechos(models.Model):
	_name = "cein.hechos"	
	hechos_id= fields.Many2one('cein.denuncia','Many2one obligado',help="obligado por one2many, no necesario aparezca en vista")
	relato= fields.Text('Relato de Hechos', required=False)
	observaciones= fields.Text('Observaciones', required=False)
	comentarios= fields.Text('Comentarios', required=False)
	delitosimplicados_id= fields.One2many('cein.delitosimplicado','name_id','Delitos Implicados')
	fecha= fields.Date('Fecha del Hecho', required=False)
	direccion= fields.Text("Dirección de Lugar de los Hechos", required=False, help="Descripcion del departamento")
	municipio_id= fields.Many2one('cein.geomunicipios','Municipio', required=True)					
	
	

class  Delitos_implicados(models.Model):
	_name = "cein.delitosimplicado"	
	name_id = fields.Many2one('cein.hechos','Many2one obligado',help="obligado por one2many, no necesario aparezca en vista")
	delitosimplicados = fields.Many2one('cein.tipo_delitos','Tipos de Delito')