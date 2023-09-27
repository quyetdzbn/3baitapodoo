from odoo import api, fields, models, tools, _


class BackUpdateWizard(models.TransientModel):
    _name = "back.update.wizard"
    _description = "back update "
    # _inherit = 'res.partner'

    discount_code = fields.Char(String='mã sản phẩm')
    product_ids = fields.Many2many('product.template')

    def update_wizard(self):
        for rec in self.product_ids:
            rec.write({'discount_code': self.discount_code})
