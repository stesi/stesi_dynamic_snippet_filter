from odoo import models, fields, api


class WebsiteSnippetFilter(models.Model):
    _inherit = 'website.snippet.filter'

    fields_id = fields.Many2one('ir.model.fields')

    @api.onchange('fields_id')
    def change_field_names(self):
        self.field_names += ","+str(self.fields_id.name)




