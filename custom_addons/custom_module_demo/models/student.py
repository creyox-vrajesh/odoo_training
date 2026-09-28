from odoo import models,fields 

class Student(models.Model):
    _name = 'school.student'
    _description = 'student'

    name = fields.Char(string='Name',required=True)
    age = fields.Integer(string='Age')
    email = fields.Char(string='Email') 
    phone = fields.Char(string='Phone',readonly=True)
    teacher_id = fields.Many2one(
        'school.teachers',
        string = 'Teacher ID'
    ) 