# -*- coding: utf-8 -*-
from odoo import http


class TestEventlight(http.Controller):
    @http.route('/test_eventlight/test_eventlight', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/test_eventlight/test_eventlight/objects', auth='public')
    def list(self, **kw):
        return http.request.render('test_eventlight.listing', {
            'root': '/test_eventlight/test_eventlight',
            'objects': http.request.env['test_eventlight.test_eventlight'].search([]),
        })

    @http.route('/test_eventlight/test_eventlight/objects/<model("test_eventlight.test_eventlight"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('test_eventlight.object', {
            'object': obj
        })

