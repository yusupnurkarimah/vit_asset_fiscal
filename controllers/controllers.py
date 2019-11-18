# -*- coding: utf-8 -*-
from odoo import http

# class VitAssetFiscal(http.Controller):
#     @http.route('/vit_asset_fiscal/vit_asset_fiscal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_asset_fiscal/vit_asset_fiscal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_asset_fiscal.listing', {
#             'root': '/vit_asset_fiscal/vit_asset_fiscal',
#             'objects': http.request.env['vit_asset_fiscal.vit_asset_fiscal'].search([]),
#         })

#     @http.route('/vit_asset_fiscal/vit_asset_fiscal/objects/<model("vit_asset_fiscal.vit_asset_fiscal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_asset_fiscal.object', {
#             'object': obj
#         })