from odoo import api, fields, models, tools


class IrActions(models.Model):
    _inherit = 'ir.actions.actions'


    @api.model
    @tools.ormcache('frozenset(self.env.user.groups_id.ids)', 'model_name')
    def get_bindings(self, model_name):
        result = super(IrActions, self).get_bindings(model_name)

        act = result.get('action')

        if not act or self.env.user in [self.env.ref('base.user_root'), self.env.ref('base.user_admin')]:
            return result

        # 获取当前用户需要隐藏的动作id
        deny_action_ids = []

        deny_action_window_ids = self.env.user.groups_id.mapped('deny_action_window_ids.id')
        deny_action_server_ids = self.env.user.groups_id.mapped('deny_action_url_ids.id')
        deny_action_client_ids = self.env.user.groups_id.mapped('deny_action_client_ids.id')
        deny_action_url_ids = self.env.user.groups_id.mapped('deny_action_url_ids.id')
        deny_action_ids.extend(
            deny_action_ids + deny_action_server_ids + deny_action_client_ids + deny_action_window_ids + deny_action_url_ids)

        if act:
            for item in act:
                if item.get('id') in deny_action_ids:
                    act.remove(item)
            result.update({'action': act})

        return result



# a = {'action': [{'id': 345, 'name': 'Mrp：计划生产订单', 'type': 'ir.actions.server', 'sequence': 5, 'model_id': (313, '生产'),
#                  'model_name': 'mrp.production', 'code': 'records.button_plan()', 'child_ids': [],
#                  'crud_model_id': False, 'link_field_id': False, 'fields_lines': [], 'state': 'code', 'partner_ids': [],
#                  'channel_ids': [], 'template_id': False, 'activity_type_id': False, 'activity_summary': False,
#                  'activity_note': False, 'activity_date_deadline_range': 0, 'activity_date_deadline_range_type': 'days',
#                  'activity_user_type': 'specific', 'activity_user_id': False, 'activity_user_field_name': 'user_id',
#                  'usage': 'ir_actions_server', 'help': False, 'binding_model_id': (313, '生产'), 'binding_type': 'action',
#                  'create_uid': (1, 'OdooBot'), 'create_date': datetime.datetime(2019, 10, 30, 2, 5, 7, 931308),
#                  'write_uid': (1, 'OdooBot'), 'write_date': datetime.datetime(2020, 3, 13, 2, 46, 3, 311333),
#                  'crud_model_name': False, 'xml_id': 'mrp.production_order_server_action', 'display_name': 'Mrp：计划生产订单',
#                  '__last_update': datetime.datetime(2020, 3, 13, 2, 46, 3, 311333)}],
#      'report': [
#          {'id': 362, 'name': '生产单', 'type': 'ir.actions.report', 'binding_type': 'report', 'model': 'mrp.production',
#           'report_name': 'mrp.report_mrporder', 'report_file': 'mrp.report.mrp_production_templates', 'groups_id': [],
#           'multi': False, 'paperformat_id': False, 'print_report_name': "'Production Order - %s' % object.name",
#           'attachment_use': False, 'attachment': False, 'deny_user_ids': [], 'deny_group_ids': [],
#           'py3o_filetype': False,
#           'py3o_template_id': False, 'module': False, 'py3o_template_fallback': False, 'report_type': 'qweb-pdf',
#           'py3o_multi_in_one': False, 'help': False, 'binding_model_id': (313, '生产'), 'create_uid': (1, 'OdooBot'),
#           'create_date': datetime.datetime(2019, 10, 30, 2, 5, 7, 931308), 'write_uid': (1, 'OdooBot'),
#           'write_date': datetime.datetime(2020, 3, 13, 2, 46, 3, 311333), 'model_id': (313, '生产'),
#           'is_py3o_native_format': False, 'lo_bin_path': False, 'is_py3o_report_not_available': False,
#           'msg_py3o_report_not_available': False, 'xml_id': 'mrp.action_report_production_order', 'display_name': '生产单',
#           '__last_update': datetime.datetime(2020, 3, 13, 2, 46, 3, 311333)},
#          {'id': 364, 'name': 'Finished Product Label (PDF)', 'type': 'ir.actions.report', 'binding_type': 'report',
#           'model': 'mrp.production', 'report_name': 'mrp.label_production_view_pdf',
#           'report_file': 'mrp.label_production_view_pdf', 'groups_id': [], 'multi': False, 'paperformat_id': False,
#           'print_report_name': "'Finished products - %s' % object.name", 'attachment_use': False, 'attachment': False,
#           'deny_user_ids': [], 'deny_group_ids': [], 'py3o_filetype': False, 'py3o_template_id': False, 'module': False,
#           'py3o_template_fallback': False, 'report_type': 'qweb-pdf', 'py3o_multi_in_one': False, 'help': False,
#           'binding_model_id': (313, '生产'), 'create_uid': (1, 'OdooBot'),
#           'create_date': datetime.datetime(2019, 10, 30, 2, 5, 7, 931308), 'write_uid': (1, 'OdooBot'),
#           'write_date': datetime.datetime(2020, 3, 13, 2, 46, 3, 311333), 'model_id': (313, '生产'),
#           'is_py3o_native_format': False, 'lo_bin_path': False, 'is_py3o_report_not_available': False,
#           'msg_py3o_report_not_available': False, 'xml_id': 'mrp.action_report_finished_product',
#           'display_name': 'Finished Product Label (PDF)',
#           '__last_update': datetime.datetime(2020, 3, 13, 2, 46, 3, 311333)},
#          {'id': 799, 'name': '投料单', 'type': 'ir.actions.report', 'binding_type': 'report', 'model': 'mrp.production',
#           'report_name': 'owl_mrp_ex.feed_list_report', 'report_file': False, 'groups_id': [], 'multi': False,
#           'paperformat_id': False, 'print_report_name': False, 'attachment_use': False, 'attachment': False,
#           'deny_user_ids': [], 'deny_group_ids': [], 'py3o_filetype': False, 'py3o_template_id': False, 'module': False,
#           'py3o_template_fallback': False, 'report_type': 'qweb-html', 'py3o_multi_in_one': False, 'help': False,
#           'binding_model_id': (313, '生产'), 'create_uid': (1, 'OdooBot'),
#           'create_date': datetime.datetime(2020, 3, 5, 18, 48, 45, 198853), 'write_uid': (1, 'OdooBot'),
#           'write_date': datetime.datetime(2020, 3, 22, 8, 4, 20, 301810), 'model_id': (313, '生产'),
#           'is_py3o_native_format': False, 'lo_bin_path': False, 'is_py3o_report_not_available': False,
#           'msg_py3o_report_not_available': False, 'xml_id': 'owl_mrp_ex.action_report_feed_list', 'display_name': '投料单',
#           '__last_update': datetime.datetime(2020, 3, 22, 8, 4, 20, 301810)}]}
