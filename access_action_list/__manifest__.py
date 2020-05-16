# -*- coding: utf-8 -*-
{
    'name': "Access For Action List",

    'summary': """
 Manage your action list access rights by setting groups """,

    'description': """
You can manage your action list access rights by setting groups.
The setting will not work on user Administrator and Odoobot.
    """,

    'author': "Qianxunman",
    'website': "https://www.cnblogs.com/qianxunman/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'security',
    'version': '2.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
    ],

    'images': ['static/description/show_apps.gif'],
    'price': 10,
    'currency': 'EUR',
    'license': 'OPL-1',
    'support': 'qianxunman1@outlook.com',

}

