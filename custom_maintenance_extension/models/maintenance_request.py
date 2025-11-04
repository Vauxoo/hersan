from odoo import models, fields

class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    maintenance_type = fields.Selection(
        selection_add=[('Programados', 'Programados')],
        ondelete={'predictive': 'set default'}
    )
