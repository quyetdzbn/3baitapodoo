# -*- coding: utf-8 -*-
# from odoo import http


# class Bai1(http.Controller):
#     @http.route('/bai1/bai1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bai1/bai1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bai1.listing', {
#             'root': '/bai1/bai1',
#             'objects': http.request.env['bai1.bai1'].search([]),
#         })

#     @http.route('/bai1/bai1/objects/<model("bai1.bai1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bai1.object', {
#             'object': obj
#         })
