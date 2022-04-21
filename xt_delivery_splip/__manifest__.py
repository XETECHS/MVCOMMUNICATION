# -*- coding: utf-8 -*-
{
    'name': "Report Delivery Slip XT",

    'summary': """New Report Delivery Slip""",

    'description': """
       New Report Delivery Slip
    """,

    'author': 'Jonathan Guacarán --> jguacaran@xetechs.com',
	'maintainer': 'XETECHS, S.A.',
	'website': 'https://www.xetechs.com',
    'category': 'General',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','report_xlsx'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/report.xml',
        'views/deliveryslip_report.xml',
    ]
}