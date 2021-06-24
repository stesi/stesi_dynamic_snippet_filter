from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    description = fields.Html()
    website_image = fields.Binary("Website Image")
    web_image = fields.Binary("Web Image", compute="_compute_web_image")

    def _compute_web_image(self):
        for partner in self:
            if partner.website_image:
                partner.web_image = partner.website_image
            elif partner.image_1920:
                partner.web_image = partner.image_1920
            else:
                partner.web_image = False
