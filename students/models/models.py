# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date
from dateutil.relativedelta import relativedelta

class Students(models.Model):
    _name = 'wb.students'
    _description = 'this is student profile'

    student_ref = fields.Char('student id', default=lambda self: _('New'))
    name = fields.Char("name")
    user_id = fields.Many2one('res.users', 'User')
    address = fields.Char("address")
    classe = fields.Char("classe")
    category = fields.Char("category")
    age = fields.Integer("age", compute="_compute_age")
    date_of_birth = fields.Date("date_of_birth")




    @api.onchange('age')
    def onchange_age(self):
        if self.age < 18:
            self.category = "Minor"
        else:
            self.category = "Adult"


    @api.depends("date_of_birth")
    def _compute_age(self):
        self.age = False
        for rec in self:
            rec.age = relativedelta(date.today(),rec.date_of_birth).years

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'student_ref' not in vals['student_ref'] == _('New'):
                vals['student_ref'] = self.env['ir.sequence'].next_by_code('wb.students.sequence')
        return super().create(vals_list)




class students1(models.Model):
    _inherit = 'wb.students'
    _description = 'this is teacher profile'
    specialization = fields.Char("stage")
    teaching_experience = fields.Char("sujet")

# class teachers(models.Model):
#     _name = "wb.teachers"
#     _inherits = {'wb.students': 'student_ref'}
#     _description = 'this is teacher profile'
#     specialization = fields.Char("specialization")
#     teaching_experience = fields.Char("teaching_experience")




