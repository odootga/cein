#-*- coding: utf-8 -*-
from datetime import date, datetime, timedelta


from openerp import fields, models, api


class Tipo_Procedimiento(models.Model):
	_name = "cein.tipo_procedimiento"
	name= fields.Char(string="Tipo de Procedimiento",	 size=256, required=True)
	unidad_responsable= fields.Char(string="Unidad Responsable",  size=256, required=True)