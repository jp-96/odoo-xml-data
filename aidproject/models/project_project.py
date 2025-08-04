from odoo import models

class Project(models.Model):
    _inherit = 'project.project'

    def name_get(self):
        result = []
        for project in self:
            customer = project.partner_id.name or ''
            display_name = f"{project.name} ({customer})" if customer else project.name
            result.append((project.id, display_name))
        return result
    