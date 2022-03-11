
from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    company_group_id = fields.Many2one(string="Grupo compañía",
        related="partner_id.company_group_id", store=True
    )
