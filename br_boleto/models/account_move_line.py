# © 2016 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    boleto_emitido = fields.Boolean(string=u"Emitido")
    nosso_numero = fields.Char(string=u"Nosso Número", size=30)

    @api.multi
    def unlink(self):
        for item in self:
            line_ids = self.env['payment.order.line'].search(
                [('move_line_id', '=', item.id),
                 ('state', '=', 'draft')])
            line_ids.sudo().unlink()
        return super(AccountMoveLine, self).unlink()

    @api.multi
    def _update_check(self):
        for item in self:
            total = self.env['payment.order.line'].search_count(
                [('move_line_id', '=', item.id),
                 ('type', '=', 'receivable'),
                 ('state', 'not in', ('draft', 'cancelled', 'rejected'))])
            if total > 0:
                raise UserError(_('Existem boletos emitidos para esta fatura!\
                                  Cancele estes boletos primeiro'))
        return super(AccountMoveLine, self)._update_check()

    @api.multi
<<<<<<< HEAD
    def action_print_boleto(self):
        if self.move_id.state in ('draft', 'cancel'):
            raise UserError(
                _('Fatura provisória ou cancelada não permite emitir boleto'))
        self = self.with_context({'origin_model': 'account.invoice'})
        return self.env.ref(
            'br_boleto.action_boleto_account_invoice').report_action(self)
=======
    def action_register_boleto(self):
        boleto_list = []
        for move in self:
            if not move.payment_mode_id:
                raise UserError(u'A fatura ' + move.move_id.name + u' - ' +
                                move.partner_id.name +
                                u' não está configurada com boleto')
            if not move.payment_mode_id.nosso_numero_sequence.id:
                raise UserError(u'Cadastre a sequência do nosso número no modo \
                                de pagamento na fatura: ' + move.move_id.name +
                                u' - ' + move.partner_id.name)
            if not move.boleto_emitido:
                vencimento = fields.Date.from_string(move.date_maturity)
                if vencimento < datetime.today().date() and not\
                        move.reconciled:
                    raise UserError(u'A data de vencimento deve ser maior que a \
                                    data atual na fatura: ' +
                                    move.move_id.name +
                                    u' - ' + move.partner_id.name +
                                    u'.\n Altere a data de vencimento!')
                move.boleto_emitido = True
                move.nosso_numero = \
                    move.payment_mode_id.nosso_numero_sequence.next_by_id()

            boleto = Boleto.getBoleto(move, move.nosso_numero)
            boleto_list.append(boleto.boleto)
            move.gerar_payment_order()
        return boleto_list
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2

    @api.multi
    def open_wizard_print_boleto(self):
        return({
            'name': 'Alterar / Reimprimir Boleto',
            'type': 'ir.actions.act_window',
            'res_model': 'br.boleto.wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'origin_model': 'account.move.line',
                'default_move_line_id': self.id,
            }
        })

    @api.multi
    def unlink(self):
        order_lines = self.env['payment.order.line'].search([(
            'move_line_id', 'in', self.ids)])
        order_lines.unlink()
        return super(AccountMoveLine, self).unlink()


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.multi
    def unlink(self):
        order_lines = self.env['payment.order.line'].search([(
            'move_id', 'in', self.ids)])
        order_lines.unlink()
        return super(AccountMove, self).unlink()
