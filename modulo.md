## ./__init__.py
```py
from . import models```

## ./__manifest__.py
```py
{
    'name': 'Custom Partner Search in Sales',
    'summary': 'Restringe la búsqueda de contactos en cotizaciones por el campo company_registry.',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'author': 'Alphaqueb Consulting',
    'website': 'https://alphaqueb.com',
    'depends': ['sale_management'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
```

## ./models/__init__.py
```py
from . import res_partner```

## ./models/res_partner.py
```py
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
        # Solo filtra si estamos en contexto de Ventas Y el usuario teclea algo
        if self.env.context.get('from_sale_order') and name:
            args = args or []
            # Búsqueda PARCIAL por company_registry
            args.append(('company_registry', 'ilike', name))
            # Pasamos name='' para ignorar coincidencia por nombre y forzar la búsqueda anterior
            return super(ResPartner, self).name_search(name='', args=args, operator=operator, limit=limit)
        else:
            # En cualquier otro módulo (Compras, Contabilidad, etc.), búsqueda nativa
            return super(ResPartner, self).name_search(name, args, operator, limit)
```

## ./views/sale_order_view.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="view_order_form_inherit_partner_domain" model="ir.ui.view">
        <field name="name">sale.order.form.inherit.partner.domain</field>
        <field name="model">sale.order</field>
        <field name="inherit_id" ref="sale.view_order_form"/>
        <field name="arch" type="xml">
            <xpath expr="//field[@name='partner_id']" position="attributes">
                <attribute name="domain">[('company_registry', '!=', False)]</attribute>
                <attribute name="context">{'from_sale_order': True}</attribute>
            </xpath>
        </field>
    </record>
</odoo>
```

