# -*- coding: utf-8 -*-
{
    'name': "Cliente / Proveedor extras",

    'summary': """Agregar campos extras en modelos y vistas""",

    'description': """
       Agregar campos
       Modelo: res.partner
    """,

    'author': 'Jonathan Guacaràn --> jguacaran@xetechs.com',
	'maintainer': 'XETECHS, S.A.',
	'website': 'https://www.xetechs.com',
    'category': 'General',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sales_views.xml',
    ]
}