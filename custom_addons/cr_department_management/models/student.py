from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError


class Student(models.Model):
    _name = "student.student"
    _description = "student module"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # student_id = self.id
    name = fields.Char(string="Student Name")
    image = fields.Binary(string="Upload Image", attachment=True)
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    zip = fields.Char(string="Zip Code")

    state_id = fields.Many2one("res.country.state", string="State ID")

    country_id = fields.Many2one("res.country", string="Country ID")

    birthdate = fields.Date(string="Birthdate")
    age = fields.Float(string="Age")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    barcode = fields.Char(string="Barcode")
    admission_no = fields.Char(string="Admission Number", readonly=True)

    department_id = fields.Many2one(
        "department.department",
        string="Department",
        domain=[
            ("active", "=", True),
            ("is_full", "=", False),
        ],
    )
    dept_code = fields.Char(
        string="Department Code",
        related='department_id.code',
        store=True
    )

    type = fields.Selection(
        [("internal", "Internal"), 
        ("external", "External")],
        string="Type",
        default="internal",
    )

    notes = fields.Html(string="Notes", sanitize=True)
    remarks = fields.Text(string="Remarks", translate=True)
    is_cr = fields.Boolean(string="is CR", default=False)
    cr_start_date = fields.Date(string="CR Start Date")
    cr_end_date = fields.Date(string="CR end Date")

    no_of_votes = fields.Integer(string="Number of Votes")
    active = fields.Boolean(string="Is Active", default=True)

    def action_filtered_students(self):
        students = self.env['student.student'].search([])

        filtered_students = students.filtered(
            lambda student: student.department_id.name == 'CE'
        )

        return {
            'type': 'ir.actions.act_window',
            'name': 'CE Students',
            'res_model': 'student.student',
            'view_mode': 'list,form',
            'domain':[('id', 'in', filtered_students.ids)] 
        }

    @api.onchange("mobile")
    def _onchange_mobile(self):
        self.barcode = self.mobile

    # create method override
    @api.model_create_multi
    def create(self, vals_list):

        print(vals_list)

        last_student = self.search([], order="id desc", limit=1)

        if last_student and last_student.admission_no:
            last_number = int(last_student.admission_no[-3:])

            number = last_number + 1
        else:
            number = 1

        for vals in vals_list:
            vals["admission_no"] = f"MCA-2026-{number:03d}"
            number = number + 1

            if vals.get("department_id"):
                department = self.env["department.department"].browse(
                    vals["department_id"]
                )

                if department.no_of_students >= department.student_capacity:
                    raise ValidationError("This department is full.")

        generated = super().create(vals_list)
        print(generated)
        return generated

    # unlink method override
    def unlink(self):
        for record in self:
            if record.active:
                raise UserError("You cannot delete an active student!")

        return super().unlink()

    # search method override
    @api.model
    def web_search_read(self, domain=None, specification=None, **kwargs):
        print("################################################")
        print("UI Search Domain:", domain)
        print("UI Search Domain:", specification)
        print("################################################")

        return super().web_search_read(domain=domain, specification=specification, **kwargs)
    
    # write method override
    @api.model
    def write(self, vals):

        print(vals)
        if vals.get('type') == "external":
            vals['is_cr'] = False
            vals['cr_start_date'] = 0
            vals['cr_end_date'] = 0
            vals['no_of_votes'] = 0


        updated = super().write(vals)
        print("thats it", updated)
        return updated 

    # search ORM
    def search_student(self):
        students = self.env["student.student"].search([])

        print("========== STUDENTS ==========")
        print(students)
        for student in students:
            print("ID:", student.age)
            print("Name:", student.name)

        print("==============================")

    # search count ORM
    def student_count(self):
        students_count = self.env["student.student"].search_count([])

        print("\n======= SEARCH COUNT =======")
        print("Total Students:", students_count)
        print("============================")

    # browse ORM
    def browse_student(self):
        student = self.env["student.student"].browse(self.id)

        print("\n========== BROWSE ==========")
        print("ID:", student.id)
        print("Name:", student.name)
        print("Email:", student.email)
        print("============================")

    # create ORM
    def create_student(self):
        student = self.env["student.student"].create(
            {
                "name": "Orm user",
                "email": "orm@gmail.com",
                "type": "internal",
                "mobile": "12345678",
                "is_cr": False,
                "active": True,
            }
        )

        print("\n========== CREATE ==========")
        print("Created ID:", student.id)
        print("Created Name:", student.name)
        print("============================")

    # write ORM
    def write_user(self):
        self.ensure_one()

        self.write({"name": "orm update student write"})

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
