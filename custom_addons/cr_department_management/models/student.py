from odoo import fields,models,api

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

    department_id = fields.Many2one(
        'department.department',
        string='Department'
    )

    type = fields.Selection([
        ('internal', 'Internal'),
        ('external', 'External')
    ], string='Type', default='internal')
    
    notes = fields.Html(string='Notes',sanitize=True)
    remarks = fields.Text(string='Remarks', translate=True)
    is_cr = fields.Boolean(string='is CR',default=True)
    cr_start_date = fields.Date(string='CR Start Date')
    cr_end_date = fields.Date(string='CR end Date')

    no_of_votes = fields.Integer(string='Number of Votes')
    active = fields.Boolean(string='Is Active',default=True)

    @api.onchange('mobile')
    def _onchange_mobile(self):
        self.barcode = self.mobile

    # search ORM
    def search_student(self):
        students = self.env['student.student'].search([])

        print("========== STUDENTS ==========")
        print(students)
        for student in students:
            print("ID:", student.age)
            print("Name:", student.name)

        print("==============================")

    # search count ORM
    def student_count(self):
        students_count = self.env['student.student'].search_count([])

        print("\n======= SEARCH COUNT =======")
        print("Total Students:", students_count)
        print("============================")

    # browse ORM
    def browse_student(self):
        student = self.env['student.student'].browse(self.id)

        print("\n========== BROWSE ==========")
        print("ID:", student.id)
        print("Name:", student.name)
        print("Email:", student.email)
        print("============================")

    # create ORM
    def create_student(self):
        student = self.env['student.student'].create({
            'name': 'Orm user',
            'email': 'orm@gmail.com' ,
            'type': 'internal',
            'mobile': '12345678',
            'is_cr': False,
            'active': True,
        })

        print("\n========== CREATE ==========")
        print("Created ID:", student.id)
        print("Created Name:", student.name)
        print("============================")
    
    # write ORM
    def write_user(self):
        self.ensure_one()

        self.write({
            'name': 'orm update student write'
        })

        print("\n=========== WRITE ==========")
        print("Updated ID:", self.id)
        print("Updated Name:", self.name)
        print("============================")

    
    # unlink ORM
    def unlink_student(self):
        self.ensure_one()

        student_id = self.id 
        student_name = self.name 

        self.unlink()

        print("\n========== UNLINK ==========")
        print("Deleted ID:", student_id)
        print("Deleted Name:", student_name)
        print("============================")