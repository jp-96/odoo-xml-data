# -*- coding: utf-8 -*-
# from odoo import http


# class Aidproject(http.Controller):
#     @http.route('/aidproject/aidproject', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aidproject/aidproject/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aidproject.listing', {
#             'root': '/aidproject/aidproject',
#             'objects': http.request.env['aidproject.aidproject'].search([]),
#         })

#     @http.route('/aidproject/aidproject/objects/<model("aidproject.aidproject"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aidproject.object', {
#             'object': obj
#         })
