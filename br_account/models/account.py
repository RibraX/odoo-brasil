# © 2016 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountAccountTemplate(models.Model):
    _inherit = 'account.account.template'

    account_type = fields.Selection(
        [('tax', 'Imposto'), ('income', 'Receita'), ('expense', 'Despesa')],
        string="Tipo de conta")


class AccountAccount(models.Model):
    _inherit = 'account.account'

    account_type = fields.Selection(
        [('tax', 'Imposto'), ('income', 'Receita'), ('expense', 'Despesa')],
        string="Tipo de conta")


class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    indPag = fields.Selection(
        [('0', u'Pagamento à Vista'), ('1', u'Pagamento à Prazo')],
<<<<<<< HEAD
        'Indicador de Pagamento', default='0')
=======
        default='0')
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2
