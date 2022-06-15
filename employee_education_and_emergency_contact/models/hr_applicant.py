from odoo import fields, models


class HrApplicantInherit(models.Model):
    _inherit = 'hr.applicant'

    emergency_contact_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Emergency Contacts',
        relation='rel_applicant_emergency_contact'
    )

    education_ids = fields.Many2many(
        comodel_name='hr.employee.education.line',
        string='Education',
        relation='rel_applicant_education'
    )

    manager_id = fields.Many2one('hr.employee', string='Manager', required=True, domain=[('parent_id', '=', False)])

    def create_employee_from_applicant(self):
        res = super(HrApplicantInherit, self).create_employee_from_applicant()
        res['context']['emergency_contact_ids'] = self.emergency_contact_ids.ids
        return res
