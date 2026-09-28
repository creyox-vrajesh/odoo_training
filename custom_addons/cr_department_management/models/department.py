from odoo import fields,models,api

class Department(models.Model):
    _name = 'department.department'
    _description = 'department description'

    name = fields.Char(string='Department Name')
    code = fields.Char(string='Code')
    no_of_students = fields.Integer(
        compute='_compute_no_of_students',
        store=True,
        string='Number of Students'
    )

    staff_ids = fields.Many2many(
        'employee.employee',
        'department_employee_rel',
        # 'employee_id',
        # 'department_id',
        string="Staff IDs" 
    )

    hod_id = fields.Many2one('employee.employee', string='HOD ID: ')
    student_ids = fields.One2many('student.student', 'department_id', string='Student IDs: ')
    
    notes = fields.Html(string='Notes',sanitize=True)
    active = fields.Boolean(string='Is Active',default=True)
	

    @api.depends('student_ids')
    def _compute_no_of_students(self):
        for department in self:
            print(department)
            domain = [
                ('department_id','=',department.id),
            ] 

            department.no_of_students = self.env[
                'student.student'
            ].search_count(domain)

    print("num of students are : ",no_of_students)