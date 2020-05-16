from odoo import api, fields, models


class ResGroups(models.Model):
    _inherit = 'res.groups'


    deny_action_window_ids = fields.Many2many(comodel_name='ir.actions.act_window', string='window action')
    deny_action_server_ids = fields.Many2many(comodel_name='ir.actions.server', string='server actions')
    deny_action_client_ids = fields.Many2many(comodel_name='ir.actions.client', string='client action')
    deny_action_url_ids = fields.Many2many(comodel_name='ir.actions.act_url', string='url actions')


