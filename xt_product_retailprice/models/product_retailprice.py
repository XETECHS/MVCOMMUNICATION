# -*- coding: utf-8 -*-

import logging
from odoo.addons import decimal_precision as dp
from odoo import models, fields, api



_logger = logging.getLogger(__name__) # Need for message in console.


class ProductTemplate(models.Model):
    #_name = 'product.template'
    _inherit = 'product.template'
        
    #For display retailprice in product.

    retail_price = fields.Float('Retail Price', default=1.0,digits=dp.get_precision('Product Price'),help="Retail Price at which the product is sold to customers.")    

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #@api.multi
    def write(self, values):
        res = super(SaleOrder, self).write(values)
        for order in self:
            if order.state not in ['draft','cancel'] and order.pricelist_id.id==order.company_id.price_retail_list_id.id:
                for line in order.order_line:
                    line.product_id.write({'retail_price':line.price_unit})
        return res

class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"
    
    base = fields.Selection(selection_add=[('retail_price','Retail Price')], ondelete={'retail_price': 'set default'})


class SaleOrderLine(models.Model):
    
    _inherit = 'sale.order.line'    
    
    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        if self.order_id.pricelist_id.id==self.order_id.company_id.price_retail_list_id.id:
            return
        return super(SaleOrderLine, self).product_uom_change()


