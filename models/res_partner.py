# models/res_partner.py
from odoo import models, api

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        """
        Aplica búsqueda exacta por 'company_registry' SOLO si el contexto
        'from_sale_order' está presente (es decir, cuando estamos en Ventas).
        En otros módulos, la búsqueda se realiza de forma nativa.
        """
        # Solo filtra si estamos en contexto de Ventas Y el usuario teclea algo
        if self.env.context.get('from_sale_order') and name:
            args = args or []
            # Búsqueda EXACTA por company_registry
            args.append(('company_registry', '=', name))
            # Pasamos name='' para ignorar coincidencia por nombre y forzar la búsqueda anterior
            return super(ResPartner, self).name_search(name='', args=args, operator=operator, limit=limit)
        else:
            # En cualquier otro módulo (Compras, Contabilidad, etc.), búsqueda nativa
            return super(ResPartner, self).name_search(name, args, operator, limit)
