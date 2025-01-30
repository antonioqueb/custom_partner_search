# models/res_partner.py
from odoo import models, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """Filtra por 'company_registry' solo si el contexto 'from_sale_order' está presente."""
        if self.env.context.get('from_sale_order') and name:
            args = args or []
            args += [('company_registry', 'ilike', name)]
            # Llama al método base con name='' para ignorar búsqueda por nombre
            return super().name_search(name='', args=args, operator=operator, limit=limit)
        else:
            return super().name_search(name, args, operator, limit)