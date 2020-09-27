# -*- coding: utf-8 -*-
from odoo import http

# class ReportStockInOut(http.Controller):
#     @http.route('/report_stock_in_out/report_stock_in_out/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_stock_in_out/report_stock_in_out/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_stock_in_out.listing', {
#             'root': '/report_stock_in_out/report_stock_in_out',
#             'objects': http.request.env['report_stock_in_out.report_stock_in_out'].search([]),
#         })

#     @http.route('/report_stock_in_out/report_stock_in_out/objects/<model("report_stock_in_out.report_stock_in_out"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_stock_in_out.object', {
#             'object': obj
#         })