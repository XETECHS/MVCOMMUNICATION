# © 2016 Camptocamp SA (Matthieu Dietrich)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"
    
    price_retail_list_id = fields.Many2one('product.pricelist',
                                        string='Retail Price Rate', readonly=False)    

class AccountConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    price_retail_list_id = fields.Many2one(related="company_id.price_retail_list_id",
                                        string='Retail Price Rate', readonly=False)

    @api.onchange('price_retail_list_id')
    def save_price_retail_list_id(self):
        if self.price_retail_list_id:
            self.company_id.price_retail_list_id = self.price_retail_list_id
