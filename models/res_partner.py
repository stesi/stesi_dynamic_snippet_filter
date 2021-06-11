from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    show_in_website = fields.Boolean("Show in website?")
    selected_partner_id = fields.Many2one('stesi.res.partner', string="Partner on Website")
