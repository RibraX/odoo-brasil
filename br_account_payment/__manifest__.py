# © 2016 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Contas a Pagar e Receber',
    'summary': """Facilita a visualização de parcelas a pagar e receber
    no Odoo - Mantido por Trustcode""",
    'description': """Facilita a visualização de parcelas a pagar e receber
    no Odoo - Mantido por Trustcode""",
    'version': '12.0.1.0.0',
    'category': 'Invoicing & Payments',
    'author': 'Trustcode',
    'license': 'AGPL-3',
    'website': 'http://www.trustcode.com.br',
    'contributors': [
        'Danimar Ribeiro <danimaribeiro@gmail.com>',
        'Carlos Alberto Cipriano Korovsky <carlos.korovsky@uktech.com.br',
    ],
    'depends': [
        'br_account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_invoice.xml',
        'views/br_account_payment.xml',
        'views/payment_mode.xml',
        'views/account_payment.xml',
        'views/account_journal.xml',
        'views/account_move.xml',
<<<<<<< HEAD
        'views/payment_order.xml',
        'views/res_settings.xml',
        'views/payment_statement.xml',
        'security/account_security.xml',
        'wizard/payment_cnab_import.xml',
=======
        'security/account_security.xml',
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2
    ],
    'installable': True,
    'application': True,
}
