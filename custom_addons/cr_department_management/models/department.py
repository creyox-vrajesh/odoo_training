from odoo import fields, models, api


class Department(models.Model):
    _name = "department.department"
    _description = "department description"

    name = fields.Char(string="Department Name")
    code = fields.Char(string="Code")

    no_of_employees = fields.Integer(string="Employees", 
    compute="_compute_no_of_employees")
    
    # number of internal students
    no_of_students = fields.Integer(
        compute="_compute_no_of_students", string="Internal Students"
    )

    no_of_external_students = fields.Integer(string="External Students",
    compute="_compute_no_of_external_students")

    student_capacity = fields.Integer(string="Student capacity")
    is_full = fields.Boolean(string="Is Full", compute="_compute_is_full", store=True)

    staff_ids = fields.Many2many(
        "employee.employee",
        "department_employee_rel",
        # 'employee_id',
        # 'department_id',
        string="Staff IDs",
    )

    hod_id = fields.Many2one(
        "employee.employee", string="HOD ID: ", domain=[("is_hod", "=", True)]
    )

    student_ids = fields.One2many(
        "student.student",
        "department_id",
        string="Active Students",
        domain=[("type", "=", "internal")],
    )
    external_students_ids = fields.One2many(
        'student.student',
        "department_id",
        string="External Students",
        domain = [("type", "=", "external")]
    )

    notes = fields.Html(string="Notes", sanitize=True)
    active = fields.Boolean(string="Is Active", default=True)

    @api.depends('staff_ids')
    def _compute_no_of_employees(self):
        for department in self:

            department.no_of_employees = len(department.staff_ids)

    @api.depends('external_students_ids')
    def _compute_no_of_external_students(self):
        for department in self:
            print(department)
            department.no_of_external_students = len(department.external_students_ids)

    @api.depends("student_ids")
    def _compute_no_of_students(self):
        for department in self:
            print(department)
            
            department.no_of_students = len(department.student_ids)

    
    @api.depends("no_of_students", "student_capacity")
    def _compute_is_full(self):

        for department in self:
            department.is_full = (
                department.no_of_students >= department.student_capacity
            )
