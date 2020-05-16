# -*- coding: utf-8 -*-
{
    'name': "access to action list",

    'summary': """
 Manage your access of action list by setting groups """,

    'description': """
You can get detail info from README.md
    """,

    'author': "qianxunman",
    'website': "https://www.cnblogs.com/qianxunman/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'security',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
    ],

}
