from odoo import models, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """Modifica la búsqueda de contactos en Odoo para que solo se filtre por el campo company_registry."""
        args = args or []
        
        if name:
            args.append(('company_registry', 'ilike', name))
        
        return super(ResPartner, self).name_search(name, args, operator, limit)
