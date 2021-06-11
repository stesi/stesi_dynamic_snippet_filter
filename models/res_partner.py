from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    show_in_website = fields.Boolean("Show in website?")
    selected_partners_ids = fields.One2many('stesi.res.partner', 'partner_id')
