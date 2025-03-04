##############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2021-Today Trey, Kilobytes de Soluciones <www.trey.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Connector Beezup',
    'summary': '''
Create a controller for download Beezup CSV with product information.''',
    'author': 'Trey (www.trey.es)',
    'website': 'https://www.trey.es',
    'license': 'AGPL-3',
    'category': 'Website',
    'version': '12.0.2.8.0',
    'depends': [
        'account',
        'account_payment_mode',
        'account_payment_sale',
        'base_manage_exception',
        'base_location',
        'delivery',
        'import_template',
        'product',
        'payment_direct_order',
        'payment_redsys',
        'payment_transaction_confirm_picking',
        'product_custom_info',
        'sale',
        'sale_manual_payment_draft_picking',
        'stock',
        'uom',
        'website_sale',
    ],
    'external_dependencies': {
        'python': [
            'pandas',
        ]
    },
    'data': [
        'security/ir.model.access.csv',
        'data/connector_beezup_cron.xml',
        'data/data.xml',
        'views/product_product_views.xml',
        'views/product_template_views.xml',
        'views/res_company_views.xml',
        'views/sale_order_views.xml',
        'wizards/import_template_sale_beezup.xml',
    ],
}
