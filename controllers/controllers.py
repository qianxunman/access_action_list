# -*- coding: utf-8 -*-
from odoo import http

# class Odoo12-addons-hide-action-list(http.Controller):
#     @http.route('/odoo12-addons-hide-action-list/odoo12-addons-hide-action-list/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo12-addons-hide-action-list/odoo12-addons-hide-action-list/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo12-addons-hide-action-list.listing', {
#             'root': '/odoo12-addons-hide-action-list/odoo12-addons-hide-action-list',
#             'objects': http.request.env['odoo12-addons-hide-action-list.odoo12-addons-hide-action-list'].search([]),
#         })

#     @http.route('/odoo12-addons-hide-action-list/odoo12-addons-hide-action-list/objects/<model("odoo12-addons-hide-action-list.odoo12-addons-hide-action-list"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo12-addons-hide-action-list.object', {
#             'object': obj
#         })