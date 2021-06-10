from odoo import fields, models, api


class StesiResPartner(models.Model):
    _name = 'stesi.res.partner'
    _description = 'Selected Partners'

    partner_id = fields.Many2one('res.partner')
    name = fields.Char(related='partner_id.name')
    image = fields.Binary(related='partner_id.image_512')
    description = fields.Html()
