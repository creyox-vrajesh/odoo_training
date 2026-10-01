from odoo import models,fields,api
from datetime import date

class Employee(models.Model):
    _name = 'employee.employee'
    _description = 'employee description'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Employee Name')
    
    
    department_ids = fields.Many2many(
        'department.department',
        'department_employee_rel',  
        # 'employee_id',              
        # 'department_id',            
        string="Departments"
    )

    image = fields.Binary(string='Upload Image', attachment=True)
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    zip = fields.Char(string="Zip Code")
 
    state_id = fields.Many2one('res.country.state',string='State')
    country_id = fields.Many2one('res.country',string='Country')
	
    birthdate = fields.Date(string='Birthdate')
    age = fields.Float(
        string='Age',
        compute='_compute_age', 
        store=True
    )

    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    barcode = fields.Char(string='Barcode')

    job_time = fields.Selection([
        ('full_time','Full Time'),
        ('part_time','Part Time')
    ],string='Job Time',default='full_time')

    notes = fields.Html(string='Notes',sanitize=True)
    remarks = fields.Text(string='Remarks', translate=True)
    is_hod = fields.Boolean(string='Is HOD',default=True)
    active = fields.Boolean(string='Is Active',default=True)

    @api.depends('birthdate')
    def _compute_age(self):
        today= date.today()

        for record in self:
        
            if record.birthdate:
                birth = record.birthdate
                record.age = today.year - birth.year - ((today.month,today.day) < (birth.month,birth.day))
            else:
                record.age = 0

    @api.onchange('mobile')
    def _onchange_mobile(self):
        self.barcode = self.mobile