departments = self.env['hr.department'].sudo().search([('id', '!=', False)])
if departments:
    for department in departments:
        total = 0
        # print(department.name)
        department_id_revenue = self.env['hr.department'].search([('id', '=', department.id)])

        list_po = self.env['purchase.order'].search(
            [('department', '=', department.id),
             ('create_date', '>', date_begin),
             ('create_date', '<=', date_end)])

        for rec in list_po:
            if rec.state == 'purchase':
                total += rec.amount_total
        purchase_list.append({"department_id": department.id,
                              "actual_spending": total,
                              "diff_actual_limit": total - department_id_revenue.spending_limit_month,
                              "date_end": date_end,
                              "date_begin": date_begin
                              })
    for rec in purchase_list:
        check = self.env['report.accountant'].search(
            [('department', '=', rec['department_id']), ('date_end', '=', rec['date_end']),
             ('date_begin', '=', rec['date_begin'])])
        if check:
            continue
        else:
            self.env['report.accountant'].create(
                {"department": rec['department_id'],
                 "actual_spending": rec['actual_spending'],
                 "revenue_difference": rec['diff_actual_limit']
                 })
    purchase_list_report = []
    for rec in self.env['report.accountant'].search(
            [('create_date', '>=', date_begin), ('create_date', '<=', date_end)]):
        purchase_list_report.append(rec.id)

    self.create({"crm_report": [(6, 0, crm_list_report)],
                 "purchase_report": [(6, 0, purchase_list_report)]})
