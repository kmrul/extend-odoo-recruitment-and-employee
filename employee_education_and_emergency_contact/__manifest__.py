# -*- coding: utf-8 -*-
# Part of Kamrul Hasan <kamrul.devcs@gmail.com>.
{
    "name": "Employee Emergency Contact and Education via Recruitment",
    "author": "Brain Station 23",
    "website": "https://brainstation-23.com/",
    "support": "kamrul.devcs@gmail.com",
    "version": "15.0.1",
    "category": "Human Resources/Recruitment",
    "summary": """ Create emergency contact and education information """,
    "description": """Create emergency contact and education information """,
    "depends": [
        'base', 'hr', 'hr_recruitment'
    ],
    "data": [
        'security/ir.model.access.csv',
        'security/hr_security.xml',
        'security/department_manager_rules.xml',
        'views/hr_employee_education_line.xml',
        'views/hr_applicant_views.xml',
        'views/hr_applicant_manager.xml',
        'views/hr_employee_views.xml',
    ],
    "images": [

    ],
    "license": "OPL-1",
    "installable": True,
    "auto_install": False,
    "application": False,
    "price": "0",
}
