from odoo import models,fields 

class Teachers(models.Model):
    _name = 'school.teachers'
    _description = 'teachers'

    name = fields.Char(string='Name')
    subject = fields.Char(string='Subject')
    department = fields.Char(string='Department')
    student_ids = fields.One2many(
        'school.student',
        'teacher_id',
        string = 'Students' 
    )