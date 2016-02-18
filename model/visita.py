#-*- coding: utf-8 -*-
from datetime import date, datetime, timedelta

import time

from openerp import fields, models, api


class Visita(models.Model):
	_name = "cein.visita"
	name= fields.Char(string="Auto Generado",	 size=256, required=True,help="Nombre sin acentos opcionalmente para optimizar busquedas")
	fecha_visita= fields.Date('Fecha de Visita', required=True)
	hora_visita= fields.Char('Hora de Visita', required=True)
	tipo_visita= fields.Char(string="Tipo de Visita", size=256, required=True,help="Nombre con acentos a mostrar")
	visitado= fields.Char(string="A quien visita", size=256, required=True,help="Nombre con acentos a mostrar")
	duracion= fields.Char(string="Duración", size=256, required=True,help="Nombre con acentos a mostrar")
	partipantes_id= fields.One2many('cein.participantes','visita_id','Personas')


class Participantes(models.Model):
	_name = "cein.participantes"
	visita_id= fields.Many2one('cein.visita','Many2one obligado',help="obligado por one2many, no necesario aparezca en vista")
	nombre= fields.Many2one('cein.persona','Nombre')
	