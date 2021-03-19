from odoo import models, fields, api
from odoo.exceptions import UserError


class WebsiteSnippetFilter(models.Model):
    _inherit = 'website.snippet.filter'

    # def _get_fields_domain(self):
    #     if self.filter_id != False:
    #         domain = [('model_id.name', '=', self.filter_id.model_id)]
    #     elif self.action_server_id != False:
    #         domain = [('model_id', '=', self.action_server_id.model_id)]
    #     return domain

    fields_id = fields.Many2many('ir.model.fields')

    related_model = fields.Many2one('ir.model', compute='_compute_related_model')

    @api.onchange('fields_id')
    def change_field_names(self):
        for field in self.fields_id:
            #self.field_names += ","+str(field.name)+":"+str(field.ttype)
            self.field_names += "," + str(field.name)

    def _compute_related_model(self):
        if self.filter_id:
            #self.related_model = self.filter_id.model_id
            self.related_model = self.env['ir.model'].search([('model', '=', self.filter_id.model_id)])
        elif self.action_server_id:
            self.related_model = self.action_server_id.model_id



