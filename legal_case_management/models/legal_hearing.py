from odoo import models, fields

class LegalHearing(models.Model):
    _name = 'legal.hearing'
    _description = 'Legal Hearing'

    name = fields.Char(string='Hearing Name', required=True)
    case_id = fields.Many2one('legal.case', string='Case', required=True, ondelete='cascade')
    date_start = fields.Datetime(string='Start Date')
    date_end = fields.Datetime(string='End Date')
    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], default='scheduled')
    location = fields.Char(string='Location')
    notes = fields.Text(string='Notes')  # Added field here
