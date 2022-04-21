# -*- coding: utf-8 -*-
#from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx
import base64
import io
from odoo import fields
import datetime
from time import gmtime, strftime
from odoo import _
from odoo.tools.safe_eval import safe_eval
from io import BytesIO

from odoo import models

import logging

_logger = logging.getLogger(__name__)

class DeliverySlipReportXls(models.AbstractModel):
    
    _name = 'report.xt_delivery_splip.deliveryslip_report_xls.xlsx'
    _inherit = 'report.report_xlsx.abstract'      
          

    def generate_xlsx_report(self, workbook, data, obj):
        #objs = self._get_objs_for_report(docids, data)
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_ids', []))
        used_context = {
            'lang': self.env.context['lang'],
        }        
        
        header_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bold': True, 'size': 12})
        format = workbook.add_format({'align': 'left', 'valign': 'top'})
        bold = workbook.add_format({'align': 'left', 'bold': True})
        bold_extra = workbook.add_format({'align': 'left', 'bold': True, 'size': 14})
        nro_format = workbook.add_format({'num_format': '#,###0.000'})
        date_format = workbook.add_format({'num_format': 'dd/mm/yy hh:mm'})
                                
        for o in obj:
            _logger.info('order: %s'%o)
            worksheet = workbook.add_worksheet('%s'%o.name)
            
            company_id = self.env.user.company_id
            binaryData = company_id.logo
            imgdata = base64.b64decode(binaryData)
            image = io.BytesIO(imgdata)
            
            #worksheet.set_header('&L&G', {'image_left': logo})
            worksheet.merge_range('A1:A2','')
            worksheet.merge_range('B1:D2', self.env.user.company_id.name + ': Delivery'  , header_format)
            
            worksheet.insert_image('A1', 'logo.png', {'image_data': image, 'x_scale': 0.30, 'y_scale': 0.30})
                
            worksheet.set_column('A:A', 25)
            worksheet.set_column('B:B', 30)
            worksheet.set_column('C:C', 20)
            worksheet.set_column('D:D', 20)
            #worksheet.set_column('E:E', 20)
            #worksheet.set_column('F:F', 15)            
            worksheet.write('A5', company_id.name, bold)
            default_address = company_id.partner_id.with_context(show_address_only=True)._get_name()
            _logger.info('default_address: %s'%default_address)
            worksheet.write('A6', default_address)            
            
                                    
            worksheet.write('D7', o.partner_id.name, bold)
            default_address = o.partner_id.with_context(show_address_only=True)._get_name()
            _logger.info('default_address: %s'%default_address)
            worksheet.write('D8', default_address)
            
            worksheet.write('A9', o.name, bold_extra)
            worksheet.write('A10', 'Date', bold)
            worksheet.write('A11', o.scheduled_date, date_format)
            
            row, col = 12, 0
            worksheet.write(row, col, 'Code', header_format)
            worksheet.write(row, col + 1, 'Product', header_format)
            worksheet.write(row, col + 2, 'Quantity', header_format)
            
            row += 1            
            
            for move in o.move_lines.filtered(lambda x: x.product_uom_qty):
                worksheet.write(row, col, move.product_id.default_code)
                worksheet.write(row, col + 1, move.product_id.name)
                worksheet.write(row, col + 2, move.product_uom_qty)
                
                row += 1  
                
            # Seccion para seriales
            has_serial_number = o.move_line_ids.mapped('lot_id')     
                     
            if o.move_line_ids:                
                
                row += 1      
                worksheet.write(row, col, 'Product', header_format)
                worksheet.write(row, col + 1, 'Description', header_format)
                if self.env.user.has_group('stock.group_lot_on_delivery_slip'):
                    worksheet.write(row, col + 2, 'Lot/Serial Number', header_format)
                worksheet.write(row, col + 3, 'Quantity', header_format)
                
                row += 1                   
                for move_line in o.move_line_ids:
                    worksheet.write(row, col, move_line.product_id.default_code)
                    worksheet.write(row, col + 1, move_line.product_id.name)
                    if self.env.user.has_group('stock.group_lot_on_delivery_slip'):
                        if has_serial_number and move_line.lot_name:  #groups="stock.group_lot_on_delivery_slip">                        
                            worksheet.write(row, col + 2, move_line.lot_name or '')
                        else:                        
                            worksheet.write(row, col + 2, move_line.lot_id.name or '')
                    worksheet.write(row, col + 3, move_line.qty_done)   
                    
                    row += 1              

