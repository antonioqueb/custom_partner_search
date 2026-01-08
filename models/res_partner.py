from odoo import models, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """
        Aplica búsqueda por 'company_registry' O por 'name' cuando el contexto
        'from_sale_order' está presente.
        """
        if self.env.context.get('from_sale_order') and name:
            args = args or []
            # Buscar por company_registry O por name
            args = ['|', ('company_registry', 'ilike', name), ('name', 'ilike', name)] + args
            return super(ResPartner, self).name_search(name='', args=args, operator=operator, limit=limit)
        else:
            return super(ResPartner, self).name_search(name, args, operator, limit)