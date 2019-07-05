<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2
# © 2018 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class PaymentMode(models.Model):
<<<<<<< HEAD
    _inherit = "l10n_br.payment.mode"

    tipo_pagamento = fields.Selection(
        [('01', 'Dinheiro'),
         ('02', 'Cheque'),
         ('03', 'Cartão de Crédito'),
         ('04', 'Cartão de Débito'),
         ('05', 'Crédito Loja'),
         ('10', 'Vale Alimentação'),
         ('11', 'Vale Refeição'),
         ('12', 'Vale Presente'),
         ('13', 'Vale Combustível'),
         ('15', 'Boleto Bancário'),
         ('90', 'Sem pagamento'),
         ('99', 'Outros')],
        string="Forma de Pagamento", default="01")
=======
    _inherit = "payment.mode"

    tipo_pagamento = fields.Selection(
        [('01', u'Dinheiro'),
         ('02', u'Cheque'),
         ('03', u'Catão de Crédito'),
         ('04', u'Cartão de Débito'),
         ('05', u'Crédito Loja'),
         ('10', u'Vale Alimentação'),
         ('11', u'Vale Refeição'),
         ('12', u'Vale Presente'),
         ('13', u'Vale Combustível'),
         ('14', u'Duplicata Mercantil'),
         ('90', u'Sem pagamento'),
         ('99', u'Outros')],
        string=u"Forma de Pagamento", default="14")
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2
