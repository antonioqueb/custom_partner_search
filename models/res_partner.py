from odoo import models, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """
        Aplica búsqueda parcial ('ilike') por 'company_registry' SOLO si el contexto
        'from_sale_order' está presente (es decir, cuando estamos en Ventas).
        En otros módulos, la búsqueda se realiza de forma nativa.
        """
        if self.env.context.get('from_sale_order') and name:
            args = args or []
            args.append(('company_registry', 'ilike', name))
            return super(ResPartner, self).name_search(name='', args=args, operator=operator, limit=limit)
        else:
            return super(ResPartner, self).name_search(name, args, operator, limit)