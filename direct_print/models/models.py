# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project(models.Model):
#     _name = '/users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project./users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project'
#     _description = '/users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project./users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
