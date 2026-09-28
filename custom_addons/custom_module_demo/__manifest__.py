{
    'name': 'My Custom Module',
    'version' : '1.0',
    'sequence' : 1,
    'summary' : 'Custom configurations and modules for Odoo 19',
    'category' : 'Extra Tools',
    'author' : 'Vrajesh Mer',
    'depends' : ['base'],
    'data' : [
        'security/ir.model.access.csv',
        'data/student_data.xml',
        'views/student_views.xml',
        'views/teacher_view.xml'
    ],
    'installable' : True,
    'application' : True,
    'license' : 'LGPL-3'
}