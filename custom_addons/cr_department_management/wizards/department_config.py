from odoo import models,fields
from odoo.exceptions import UserError

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
        self.ensure_one()

        if self.type == "create":
            self.env['department.department'].create({
                "name": self.name,
                "code": self.code
            })
        
        if self.type == "write":
            if not self.department_id:
                raise UserError("Please select a department to update.")

            vals={}
            if self.name:
                vals["name"] = self.name

            if self.code:
                vals["code"] = self.code

            if vals:
                self.department_id.write(vals)
    
        return {
            'type':'ir.actions.act_window_close'
        } 

    def action_cancel(self):
        return {
            'type':'ir.actions.act_window_close'
        }