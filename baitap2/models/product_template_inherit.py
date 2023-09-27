# -*- coding: utf-8 -*-


from odoo import models, fields, api
from datetime import datetime


class InheritProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'extend product template'

    product_warranty = fields.Char(compute='compute_product_warranty')
    date_to = fields.Datetime(compute='compute_product_warranty')
    date_from = fields.Datetime(compute='compute_product_warranty')
    sale_order_discount_estimated = fields.Char()
    discount_code = fields.Char()
    check = fields.Boolean(store=True)

    def compute_product_warranty(self):
        for rec in self:
            if rec.discount_code:
                rec.date_to = datetime.strptime(rec.discount_code.split('/')[1], '%d%m%y')
                rec.date_from = datetime.strptime(rec.discount_code.split('/')[2], '%d%m%y')
                diff = int((rec.date_from - rec.date_to).total_seconds()) / 86400
                if diff > 365:
                    rec.product_warranty = str(int(diff / 365)) + ' năm'
                elif diff > 30 and diff < 365:
                    rec.product_warranty = str(int(diff / 30)) + ' tháng'
                elif diff < 30:
                    rec.product_warranty = str(diff) + ' ngày'
            else:
                rec.date_to = 0
                rec.date_from = 0
                rec.product_warranty = 0

    @api.constrains('discount_code')
    def check_product_warranty(self):
        # for rec in self:
        self.check = False
        if self.discount_code:
            diff = (self.date_from - datetime.now()).total_seconds()
            if diff > 0:
                self.check = True
            else:
                self.check = False

    def open_product_warranty_update_wizard(self):
        view = self.env.ref('module_name.product_price_update_wizard_form_view')
        return {
            'name': 'Update Prices',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'back.update.wizard',
            'views': [(view.id, 'form')],
            'target': 'new',
        }
