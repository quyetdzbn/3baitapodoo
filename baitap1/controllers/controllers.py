# -*- coding: utf-8 -*-
from odoo import http
import json


@odoo.http.route(['/pet'], methods=['POST'], type='json', auth="none", csrf=True)
def pet_handler(self, **kw):
    # body
    if request.httprequest.json.get("token") != "odooneverdie":
        return {"error": "Invalid Token"}

    model_name = "monthly.report"

    try:
        response = {}
        # recordset báo cáo hàng tháng
        records = request.env[model_name].sudo().search([])
        for rec in records:

            # kiểm tra xem record có khác với tháng yêu cầu
            if rec.create_date.month != request.httprequest.json.get("month"):
                return response

            crm_report = []
            purchase_report = []
            for crm in rec.crm_month_report:
                crm_report.append({
                    "sale_team_name": crm.sales_team_id.name,
                    "real_revenue": crm.actual_revenue,
                    "diff": crm.diff_actual_target
                })
            response["sales"] = crm_report

            for purchase in rec.purchase_month_report:
                purchase_report.append({
                    "department_name": purchase.department_id.name,
                    "real_cost": purchase.actual_spending,
                    "diff": purchase.diff_actual_limit
                })
            response["purchase"] = purchase_report

    except Exception as e:
        response = {
            "status": "error",
            "content": "not found"
        }
        raise e
    return response


class Baitap1(http.Controller):
    # @http.route('/mountain', auth='public',type='json')
    # def mountain_check(self):
    #     return "mountain check"

    @http.route('/mountain', auth='user', type='http')
    def mountain_check(self):
        return json.dumps({"check": "check123"})
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/baitap1/baitap1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('baitap1.listing', {
#             'root': '/baitap1/baitap1',
#             'objects': http.request.env['baitap1.baitap1'].search([]),
#         })

#     @http.route('/baitap1/baitap1/objects/<model("baitap1.baitap1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('baitap1.object', {
#             'object': obj
#         })
