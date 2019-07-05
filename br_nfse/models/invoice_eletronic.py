# © 2016 Danimar Ribeiro <danimaribeiro@gmail.com>, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models
<<<<<<< HEAD
=======
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DTFT

_logger = logging.getLogger(__name__)

try:
    from pytrustnfe.nfse.paulistana import envio_lote_rps
    from pytrustnfe.nfse.paulistana import teste_envio_lote_rps
    from pytrustnfe.nfse.paulistana import cancelamento_nfe
    from pytrustnfe.certificado import Certificado
except ImportError:
    _logger.warning('Cannot import pytrustnfe', exc_info=1)
>>>>>>> f1111b8ab4e9b0f064d267d2c8ccaab9409617c2


STATE = {'edit': [('readonly', False)]}


class InvoiceEletronic(models.Model):
    _inherit = 'invoice.eletronic'

    nfse_eletronic = fields.Boolean('Emite NFS-e?', readonly=True)
    verify_code = fields.Char(
        string=u'Código Autorização', size=20, readonly=True, states=STATE)
    numero_nfse = fields.Char(
        string=u"Número NFSe", size=50, readonly=True, states=STATE)

    @api.multi
    def _hook_validation(self):
        errors = super(InvoiceEletronic, self)._hook_validation()
        if self.nfse_eletronic:
            if not self.company_id.inscr_mun:
                errors.append(u'Inscrição municipal obrigatória')
        return errors
