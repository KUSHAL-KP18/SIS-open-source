from odoo import models, fields, api
from odoo.exceptions import UserError

class LegalCase(models.Model):
    _name = 'legal.case'
    _description = 'Legal Case'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    name = fields.Char(string='Case Reference', required=True, copy=False, readonly=True, default='New')
    client_id = fields.Many2one('res.partner', string='Client', domain=[('is_client', '=', True)], required=True)
    responsible_lawyer_id = fields.Many2one('res.partner', string='Responsible Lawyer', domain=[('is_lawyer', '=', True)])
    member_ids = fields.Many2many('res.partner', string='Members', domain=[('is_lawyer', '=', True)])
    case_type = fields.Selection([('criminal', 'Criminal'), ('civil', 'Civil')], string='Case Type')
    stage = fields.Selection([('intake', 'Intake'), ('active', 'Active'), ('closed', 'Closed')], string='Stage', default='intake')
    open_date = fields.Date(string='Open Date', default=fields.Date.context_today)
    close_date = fields.Date(string='Close Date')
    fixed_fee_amount = fields.Monetary(string='Fixed Fee Amount', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    hearing_ids = fields.One2many('legal.hearing', 'case_id', string='Hearings')

    invoice_count = fields.Integer(string='Invoice Count', compute='_compute_invoice_count')
    hearing_count = fields.Integer(string='Hearing Count', compute='_compute_hearing_count')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('legal.case') or 'New'
        return super(LegalCase, self).create(vals)

    def _compute_invoice_count(self):
        for case in self:
            invoices = self.env['account.move'].search([('legal_case_id', '=', case.id), ('move_type', '=', 'out_invoice')])
            case.invoice_count = len(invoices)

    def _compute_hearing_count(self):
        for case in self:
            case.hearing_count = len(case.hearing_ids)

    def action_close_case(self):
        for record in self:
            if record.stage not in ['active', 'intake']:
                raise UserError("Cannot close case unless stage is Active or Intake.")
            record.stage = 'closed'
            record.close_date = fields.Date.context_today(record)

    def action_create_invoice(self):
        AccountMove = self.env['account.move']
        for record in self:
            if record.stage != 'active':
                raise UserError("Invoices can only be created in Active stage.")
            invoice_vals = {
                'move_type': 'out_invoice',
                'partner_id': record.client_id.id,
                'invoice_line_ids': [(0, 0, {
                    'name': 'Legal Services',
                    'quantity': 1,
                    'price_unit': record.fixed_fee_amount,
                })],
                'legal_case_id': record.id,
            }
            invoice = AccountMove.create(invoice_vals)
            invoice.action_post()
