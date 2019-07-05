# © 2018 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

<<<<<<< HEAD
from odoo import models, _
from odoo.exceptions import UserError
from ..boleto.document import Boleto
=======
from odoo import api, fields, models
from odoo.exceptions import UserError
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2


class PaymentOrderLine(models.Model):
    _inherit = 'payment.order.line'

<<<<<<< HEAD
    def generate_payment_order_line(self, move_line):
        """Gera um objeto de payment.order ao imprimir um boleto"""
        order_name = self.env['ir.sequence'].next_by_code('payment.order')
        payment_mode = move_line.payment_mode_id
        payment_order = self.env['payment.order'].search([
            ('state', '=', 'draft'),
            ('payment_mode_id', '=', payment_mode.id)], limit=1)
        order_dict = {
            'name': u'%s' % order_name,
            'user_id': self.env.user.id,
            'payment_mode_id': move_line.payment_mode_id.id,
            'state': 'draft',
            'currency_id': move_line.company_currency_id.id,
            'company_id': payment_mode.journal_id.company_id.id,
            'journal_id': payment_mode.journal_id.id,
            'src_bank_account_id': payment_mode.journal_id.bank_account_id.id,
        }
        if not payment_order:
            payment_order = payment_order.create(order_dict)

        move = self.env['payment.order.line'].search(
            [('src_bank_account_id', '=',
              payment_mode.journal_id.bank_account_id.id),
             ('move_line_id', '=', move_line.id),
             ('state', 'not in', ('cancelled', 'rejected'))])
        if not move:
            return self.env['payment.order.line'].create({
                'move_line_id': move_line.id,
                'src_bank_account_id':
                payment_mode.journal_id.bank_account_id.id,
                'journal_id': payment_mode.journal_id.id,
                'payment_order_id': payment_order.id,
                'payment_mode_id': move_line.payment_mode_id.id,
                'date_maturity': move_line.date_maturity,
                'partner_id': move_line.partner_id.id,
                'emission_date': move_line.date,
                'amount_total': move_line.amount_residual,
                'name': "%s/%s" % (move_line.move_id.name, move_line.name),
                'nosso_numero':
                payment_mode.nosso_numero_sequence.next_by_id(),
            })
        return move
=======
    @api.multi
    @api.depends('move_line_id.reconciled')
    def _compute_state(self):
        for item in self:
            if item.move_line_id.reconciled:
                item.state = 'paid'
            if not item.state:
                item.state = 'draft'

    @api.multi
    def unlink(self):
        for item in self:
            if item.state in ('paid', 'open'):
                state = 'Confirmado'
                if item.state == 'paid':
                    state = 'Pago'
                raise UserError(
                    "Você não pode deletar a linha de cobrança {}\
                    pois ela está com status {}".format(
                        item.move_id.name, state))
        return super(PaymentOrderLine, self).unlink()

    name = fields.Char(string="Ref.", size=20)
    payment_order_id = fields.Many2one(
        'payment.order', string="Ordem de Pagamento", ondelete="cascade")
    move_line_id = fields.Many2one(
        'account.move.line', string=u'Linhas de Cobrança')
    partner_id = fields.Many2one(
        'res.partner', related='move_line_id.partner_id',
        string="Parceiro", readonly=True)
    move_id = fields.Many2one('account.move', string=u"Lançamento de Diário",
                              related='move_line_id.move_id', readonly=True)
    nosso_numero = fields.Char(string=u"Nosso Número", size=20)
    payment_mode_id = fields.Many2one(
        'payment.mode', string="Modo de pagamento")
    date_maturity = fields.Date(string="Vencimento")
    value = fields.Float(string="Valor", digits=(18, 2))
    state = fields.Selection([("draft", "Provisório"),
                              ("open", "Confirmado"),
                              ("paid", "Pago"),
                              ("rejected", "Rejeitado"),
                              ("baixa", "Baixa")],
                             string=u"Situação",
                             compute="_compute_state",
                             readonly=False,
                             store=True)
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2

    def action_register_boleto(self, move_lines):
        for item in move_lines:
            if item.payment_mode_id.type != 'receivable':
                raise UserError(_('Modo de pagamento não é boleto!'))
            if not item.payment_mode_id.boleto:
                raise UserError(_('Modo de pagamento não é boleto!'))
        for move_line in move_lines:
            order_line = self.generate_payment_order_line(move_line)
            move_line.write({'l10n_br_order_line_id': order_line.id})
            self |= order_line
        move_lines.write({'boleto_emitido': True})
        return self

    def generate_boleto_list(self):
        if self.filtered(lambda x: x.state in ('cancelled', 'rejected')):
            raise UserError(
                _('Boletos cancelados ou rejeitados não permitem a impressão'))
        boleto_list = []
        for line in self:
            boleto = Boleto.getBoleto(line, line.nosso_numero)
            boleto_list.append(boleto.boleto)
        return boleto_list

    def action_print_boleto(self):
        for item in self:
<<<<<<< HEAD
            if item.payment_mode_id.type != 'receivable':
                raise UserError(_('Modo de pagamento não é boleto!'))
            if not item.payment_mode_id.boleto:
                raise UserError(_('Modo de pagamento não é boleto!'))
        return self.env.ref(
            'br_boleto.action_boleto_payment_order_line').report_action(self)
=======
            amount_total = 0
            for line in item.line_ids:
                amount_total += line.value
            item.amount_total = amount_total

    @api.multi
    def unlink(self):
        for item in self:
            item.line_ids.unlink()
        return super(PaymentOrder, self).unlink()

    name = fields.Char(max_length=30, string="Nome", required=True)
    user_id = fields.Many2one('res.users', string=u'Responsável',
                              required=True)
    payment_mode_id = fields.Many2one('payment.mode',
                                      string='Modo de Pagamento',
                                      required=True)
    state = fields.Selection([('draft', 'Rascunho'), ('cancel', 'Cancelado'),
                              ('open', 'Confirmado'), ('done', 'Fechado')],
                             string=u"Situação")

    line_ids = fields.One2many('payment.order.line', 'payment_order_id',
                               required=True, string=u'Linhas de Cobrança')
    currency_id = fields.Many2one('res.currency', string='Moeda')
    amount_total = fields.Float(string="Total",
                                compute='_compute_amount_total')
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2
