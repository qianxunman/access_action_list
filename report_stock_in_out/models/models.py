# -*- coding: utf-8 -*-

from odoo import api, fields, models
# import serial

class ViewInOutInventory(models.Model):
    _name = 'view.in.out.inventory'
    _description = '每月进销存统计'

    _auto = False

    SELECTION_TYPE = [
        ('1incoming', '当月入库'),
        ('2outgoing', '当月出库'),
        ('3inventory', '当月结存')
    ]

    product_id = fields.Many2one(comodel_name='product.product', string='产品')
    location_id = fields.Many2one(comodel_name='stock.location', string='位置')
    lot_id = fields.Many2one(comodel_name='stock.production.lot', string='批号')
    date_month = fields.Date(string='日期月份')
    format_month = fields.Char(string='月份')
    product_uom_id = fields.Many2one(comodel_name='uom.uom', string='单位')
    qty_done = fields.Float(string='数量')
    type = fields.Selection(string='数据类型', selection=SELECTION_TYPE)
