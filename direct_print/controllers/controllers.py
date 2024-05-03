# -*- coding: utf-8 -*-
# from odoo import http


# class /users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project(http.Controller):
#     @http.route('//users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project//users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project//users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project.listing', {
#             'root': '//users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project//users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project',
#             'objects': http.request.env['/users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project./users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project'].search([]),
#         })

#     @http.route('//users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project//users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project/objects/<model("/users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project./users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/users/shendy.juniantotunasgroup.com/kerja/surigiwa/side-project.object', {
#             'object': obj
#         })
