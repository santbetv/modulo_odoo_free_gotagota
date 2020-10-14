# -*- coding: utf-8 -*-
{
    'name': 'Gota a Gota',
    'version': '12.0.1.0.1',
    'summary': """Modulo para gestionar cobros, y NO dar dedo""",
    'category': 'Cobros',
    'author': 'Santiago Betancur Villegas',
    'company': 'umanizales',
    'website': 'https://www.umanizales.com',
    'description': """Realizar cobros y todos sus procesos financieros""",
    'depends': ['mass_mailing'],
    'data': [
        'security/gotagota_security.xml',
        'security/ir.model.access.csv',
        'views/gotagota_prestamo_view.xml',
        'views/gotagota_parametricas_view.xml',
        'views/gotagota_cobrador_view.xml',
        'views/gotagota_menu.xml',
        #'views/captcha_views.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}