from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


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
        if not self.field_names:
            self.field_names = "name"
        for field in self.fields_id:
            #self.field_names += ","+str(field.name)+":"+str(field.ttype)
            self.field_names += "," + str(field.name)

    @api.onchange('filter_id', 'action_server_id')
    def _compute_related_model(self):
        if self.filter_id:
            #self.related_model = self.filter_id.model_id
            self.related_model = self.env['ir.model'].search([('model', '=', self.filter_id.model_id)])
        elif self.action_server_id:
            self.related_model = self.action_server_id.model_id

    @api.constrains('limit')
    def _check_limit(self):
        """Limit must be between 1 and 16."""
        for record in self:
            if record.limit <= 0:
                raise ValidationError(_("The limit must greater than 0"))


    # @api.onchange('fields_id')
    # def _check_fields_names(self):
    #     print(type(self.field_names))
    #     print(self.field_names)
    #     field_split = self.field_names.split(',')
    #     print(field_split)
    #     field_to_remove = []
    #     for field in field_split:
    #         if field not in self.field_names:
    #             field_to_remove.append(field)
    #             # self.field_names.remove(field)
    #     for f in field_to_remove:
    #         field_split.remove(f)
    #     self.field_names = " "
    #     for f in field_split:
    #         self.field_names += f+","


