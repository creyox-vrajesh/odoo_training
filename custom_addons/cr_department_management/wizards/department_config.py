from odoo import models,fields

class Department_config(models.TransientModel):
    _name = "department.conf"
    _description = "department configuration file"

    type = fields.Selection([
        ('create', 'Create'),
        ('write','Write')
    ],string="Create or Write")

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

    department_id = fields.Many2one(
        'department.department',
        string="Departments"
    )


    def action_process(self):
        return 

    def action_cancel(self):
        return {
            'type':'ir.actions.act_window_close'
        }