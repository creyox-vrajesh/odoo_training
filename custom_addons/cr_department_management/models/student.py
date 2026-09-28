from odoo import fields,models

class Student(models.Model):
    _name = 'student.student'
    _description = 'student module'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # student_id = self.id
    name = fields.Char(string='Student Name')
    image = fields.Binary(string='Upload Image', attachment=True)
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    zip = fields.Char(string="Zip Code")


    state_id = fields.Many2one('res.country.state', string='State ID')
    
    country_id = fields.Many2one('res.country',string='Country ID')

    birthdate = fields.Date(string='Birthdate')
    age = fields.Float(string='Age')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    barcode = fields.Char(string='Barcode')

    department_id = fields.Many2one('department.department',string='Department ID')

    type = fields.Selection([
        ('internal', 'Internal'),
        ('external', 'External')
    ], string='Type', default='internal')
    
    notes = fields.Html(string='Notes',sanitize=True)
    remarks = fields.Text(string='Remarks', translate=True)
    is_cr = fields.Boolean(string='is CR',default=True)
    cr_start_date = fields.Date(string='CR ~Start Date')
    cr_end_date = fields.Date(string='CR end Date')

    no_of_votes = fields.Integer(string='Number of Votes')
    active = fields.Boolean(string='Is Active',default=True)

    # class create_student(self):
    #     student = self.env['student.student'].create({
    #         'name' : 'akshay kumar',
    #         'email' : 'akshay@07gmail.com' 
    #     })
    #     print(student)
  