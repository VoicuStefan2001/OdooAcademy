# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Academy Lyall',
    'version' : '1.0',
    'summary': 'Lyall\'s testing module',
    'sequence': 100,
    'description': """
Testing space
====================

The primary module for working with content for the academy.
   """,
    'category': '',
    'website': '',
    'images' : ['static/canada.png'],
    'depends' : [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '_account_post_init',
    'assets': {},
    'license': 'LGPL-3',
}
