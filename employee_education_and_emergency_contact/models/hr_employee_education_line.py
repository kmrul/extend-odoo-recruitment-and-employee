from odoo import fields, models


class HrEmployeeEducationLine(models.Model):
    _name = 'hr.employee.education.line'

    institute = fields.Char(string='Institute')
    degree = fields.Char(string='Degree')
    passing_year = fields.Char(string='Passing Year')
