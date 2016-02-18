#-*- coding: utf-8 -*-
from datetime import date, datetime, timedelta


from openerp import fields, models, api


class Turno(models.Model):
	_name = "cein.turno"
	name= fields.Char(string="Frecuencia",	 size=256, required=True)
	hora_inicio= fields.Char(string="Hora de Inicio",  size=256, required=True)
	hora_final= fields.Char(string="Hora Final",	 size=256, required=True)