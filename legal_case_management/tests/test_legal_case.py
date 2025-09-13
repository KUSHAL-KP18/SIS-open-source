from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestLegalCaseManagement(TransactionCase):

    def setUp(self):
        super(TestLegalCaseManagement, self).setUp()
        self.lawyer = self.env['res.partner'].create({
            'name': 'Test Lawyer',
            'is_lawyer': True,
            'bar_number': 'BAR0001',
        })
        self.client = self.env['res.partner'].create({
            'name': 'Test Client',
            'is_client': True,
        })

    def test_create_case(self):
        case = self.env['legal.case'].create({
            'client_id': self.client.id,
            'responsible_lawyer_id': self.lawyer.id,
            'case_type': 'criminal',
            'stage': 'intake',
            'fixed_fee_amount': 500,
        })
        self.assertTrue(case.name.startswith('CASE/'))
        self.assertEqual(case.stage, 'intake')

    def test_close_case(self):
        case = self.env['legal.case'].create({
            'client_id': self.client.id,
            'responsible_lawyer_id': self.lawyer.id,
            'case_type': 'family',
            'stage': 'active',
            'fixed_fee_amount': 300,
        })
        case.action_close_case()
        self.assertEqual(case.stage, 'closed')
        self.assertIsNotNone(case.close_date)

    def test_invoice_creation_error(self):
        case = self.env['legal.case'].create({
            'client_id': self.client.id,
            'responsible_lawyer_id': self.lawyer.id,
            'case_type': 'civil',
            'fixed_fee_amount': 0,
        })
        with self.assertRaises(ValidationError):
            case.action_create_invoice()
