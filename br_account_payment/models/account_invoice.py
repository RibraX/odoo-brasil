# © 2016 Alessandro Fernandes Martini, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


FIELD_STATE = {'draft': [('readonly', False)]}


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    payment_mode_id = fields.Many2one(
<<<<<<< HEAD
        'l10n_br.payment.mode', readonly=True,
        states=FIELD_STATE, string=u"Modo de pagamento")
=======
        'payment.mode', string=u"Modo de pagamento")
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2

    @api.multi
    def finalize_invoice_move_lines(self, move_lines):
        res = super(AccountInvoice, self).\
            finalize_invoice_move_lines(move_lines)

        for invoice_line in res:
            line = invoice_line[2]
            line['payment_mode_id'] = self.payment_mode_id.id
        return res
