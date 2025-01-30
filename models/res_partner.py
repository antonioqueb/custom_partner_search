from odoo import models, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """Aplica la restricción solo cuando la búsqueda proviene de una cotización u orden de venta."""
        args = args or []
        context_model = self.env.context.get('model')

        # Solo aplicar la restricción en ventas (sale.order)
        if context_model == 'sale.order' and name:
            args.append(('company_registry', 'ilike', name))
        
        return super(ResPartner, self).name_search(name, args, operator, limit)
