<<<<<<< HEAD
# © 2016 Fábio Luna <fabiocluna@hotmail.com>, Trustcode
=======
# -*- coding: utf-8 -*-
# © 2018 Trustcode
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class AccountInvoiceRefund(models.TransientModel):
    _inherit = 'account.invoice.refund'

    fiscal_position_id = fields.Many2one(
        'account.fiscal.position', string="Posição Fiscal")

<<<<<<< HEAD
    @api.multi
    def invoice_refund(self):
        res = super(AccountInvoiceRefund, self).invoice_refund()
        if type(res) is bool:
            return res
        if "domain" not in res:
            return res
=======
    def get_document_type(self, inv_id):
        if inv_id.fiscal_document_id.code == '55':
            document_type = 'nfe'
        elif inv_id.fiscal_document_id.code == '04':
            document_type = 'nfrural'
        elif inv_id.fiscal_document_id.code == '57':
            document_type = 'cte'
        elif inv_id.fiscal_document_id.code in ('2B', '2C', '2D'):
            document_type = 'cf'
        else:
            document_type = 'nf'
        return document_type

    @api.multi
    def invoice_refund(self):
        res = super(AccountInvoiceRefund, self).invoice_refund()
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2

        invoice_id = res['domain'][1][2][0]
        invoice_id = self.env['account.invoice'].search([
            ('id', '=', invoice_id)
        ])
<<<<<<< HEAD
        fiscal_pos = self.fiscal_position_id
        invoice_id.write({
            'fiscal_position_id': fiscal_pos.id,
            'product_serie_id': fiscal_pos.product_serie_id.id,
            'product_document_id': fiscal_pos.product_document_id.id,
            'service_serie_id': fiscal_pos.service_serie_id.id,
            'service_document_id': fiscal_pos.service_document_id.id,
            'fiscal_observation_ids': [(
                6, False, [x.id for x in fiscal_pos.fiscal_observation_ids]
            )]
        })
=======
        origin = self.env['account.invoice'].search([
            ('id', '=', self._context.get('active_id'))])

        invoice_id.write({
            'fiscal_position_id': self.fiscal_position_id.id,
            'fiscal_document_related_ids': [
                (0, 0, {
                    'invoice_related_id': origin.id,
                    'document_type': self.get_document_type(origin)})]
            })
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2

        if self.fiscal_position_id:
            for item in invoice_id.invoice_line_ids:
                price_unit = item.price_unit
                item._onchange_product_id()
                item._br_account_onchange_product_id()
                item.write({'price_unit': price_unit})
                item._set_extimated_taxes(price_unit)

        return res
