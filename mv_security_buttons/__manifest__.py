# -*- encoding: UTF-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################
{
    'name': 'Bloqueo boton Confirmar SO y Validar Invoice',
    'summary': """Boton Confirmar SO y Validar Invoice""",
    'version': '',
    'description': """Bloqueo Boton Confirmar SO y Validar Invoice""",
    'author': 'jgomez@xetechs.com',
    'maintainer': 'Xetechs S.A',
    'website': 'https://www.xetechs.com',
    'category': 'sale',
    'depends': ['base','sale','account'],
    'license': 'AGPL-3',
    'data': [
            'views/sale_order_button.xml',
            'views/invoice_button.xml',
            'security/security_group.xml',
             ],
    'demo': [],
    'sequence': 1,
    'installable': True,
    'auto_install': False,
    'application': True,

}
