# -*- coding: utf-8 -*-
# Copyright 2017 LasLabs Inc.
# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class MedicalPractitioner(models.Model):
    _name = 'medical.practitioner'
    _description = 'Medical Practitioner'
    _inherit = 'medical.abstract.entity'

    _sql_constraints = [(
        'medical_practitioner_unique_code',
        'UNIQUE (code)',
        'Internal ID must be unique',
    )]

    role_ids = fields.Many2many(
        string='Roles',
        comodel_name='medical.role',
    )
    practitioner_type = fields.Selection(
        string='Entity Type',
        selection=[('internal', 'Internal Entity'),
                   ('external', 'External Entity')],
        readonly=False,
    )
    code = fields.Char(
        string='Internal ID',
        help='Unique ID for this physician',
        required=True,
        default=lambda s: s.env['ir.sequence'].next_by_code(s._name + '.code'),
    )
    specialty_ids = fields.Many2many(
        string='Specialties',
        comodel_name='medical.specialty',
    )
