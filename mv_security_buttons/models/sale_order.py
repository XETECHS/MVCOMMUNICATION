# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################
from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

class AccountInvoice(models.Model):
    _inherit = "account.move"
