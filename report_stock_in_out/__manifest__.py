# -*- coding: utf-8 -*-
{
    'name': "report_stock_in_out",

    'summary': """
        仓库进销存报表""",

    'description': """
        按照仓库的维度查看每一天该仓库的入库产品数量,出库产品数量,以及出入库之后的现存量.
    """,

    'author': "qianxunman",
    'website': "http://www.cnblogs.com/qianxunman",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'reports',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        'data/func.sql',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    
    'images': ['static/description/show_apps.png'],
    'currency': 'EUR',
    'license': 'OPL-1',
    'support': 'qianxunman1@outlook.com',


}