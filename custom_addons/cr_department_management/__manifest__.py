{
    'name':'cr department management',
    'version': '19.0.0.5',
    'sequence': 2,
    'summary' : 'Custom module development for Odoo 19',
    'category' : 'Department Management',
    'author' : 'Vrajesh Mer',
    'depends' : ['base','mail'],
    'data' : [
        'security/ir.model.access.csv',
        'views/department_management_view.xml',
        'views/department_view.xml',
        'views/employee_view.xml',
        'views/student_view.xml',
        'views/department_config_wizard.xml'
    ],
    'installable' : True,
    'application' : True,
    'license' : 'LGPL-3'
}