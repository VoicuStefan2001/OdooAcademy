# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'LKtesting',
    'version' : '1.0',
    'summary': 'Lyall\'s testing module',
    'sequence': 100,
    'description': """
Testing space
====================

The primary testspace module for Lyall to experiment on the database
   """,
    'category': '',
    'website': '',
    'images' : ['static/canada.png'],
    'depends' : ['base_setup', 'product', 'analytic', 'portal', 'digest'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '_account_post_init',
    'assets': {},
    'license': 'LGPL-3',
}
