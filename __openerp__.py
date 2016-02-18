#-*- coding: utf-8 -*-
{
	'name' : 'Centro Integrado de Desarrollo Institucional-CEIN',
	'depends' : ['base'],
	'category': 'Project Management Module',
	'description' :'''Desarrollo Exclusivo''',
	'author': 'Marco Rios, Allan Maradiaga',
	'data': [
		'view/tipo_denuncia_view.xml',
		'view/escolaridad_view.xml',
		'view/ocupacion_view.xml',
		'view/nacionalidad_view.xml',
		'view/tipo_documento_view.xml',		
		'view/profesion_view.xml',	
		'view/estadocivil_view.xml',	
		'view/raza_view.xml',	
		'view/persona_view.xml',	
		'view/denuncia_view.xml',
		'view/tipo_implicados_view.xml',
		'view/tipo_delitos_view.xml',
		'view/tipo_departamentos_view.xml',
		'view/tipo_municipios_view.xml',
		'security/res_groups.xml',
		'security/ir.model.access.csv',
######################### SECUENCIAS #########################
		'data/denuncia_sequence.xml',
####################### DATA DEMO #########################
		'data/departamento_data.xml',
		'data/municipio_data.xml',
		'data/escolaridad_data.xml',
		'data/ocupacion_data.xml'

		],
	'installable': True,	
} 	 	 	
