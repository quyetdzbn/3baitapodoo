from odoo import models, fields, api
from odoo.exceptions import UserError


class CustomField(models.Model):
    _name = 'customer'
    _description ='giam gia'

    # _inherit = 'res.partner'
    discount_code = fields.Char(String='giam gia')
    Sale_order_discount_estimated = fields.Char(String='tong chiet khau uoc tinh')
    name = fields.Char(String='ten',require=True)

    @api.model
    def create(self, values):
        if not self.user_has_groups('bai1.advance_sale'):
            if 'discount_code' in values:
                raise UserError(
                    'You are not allowed to modify '
                    'manager_remarks')
        return super(CustomField, self).create(values)

    def write(self, values):
        if not self.user_has_groups('bai1.advance_sale'):
            if 'discount_code' in values:
                raise UserError(
                    'You are not allowed to modify '
                    'manager_remarks')
        return super(CustomField, self).write(values)
