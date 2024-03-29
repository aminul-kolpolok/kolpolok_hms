from odoo import fields, models, api
from odoo import exceptions


class MoneyReceipt(models.Model):
    _name = 'money.receipt'
    _rec_name = 'name'
    _order = 'name desc'

    name = fields.Char("Mr ID")
    date = fields.Datetime("Date", default=fields.Datetime.now())
    # bill_id = fields.Many2one("bill.register", "BIll ID")
    # optic_sale_id = fields.Many2one("optics.sale", "Optics Sale ID")
    opd_id = fields.Many2one('opd.info', 'OPD ID')
    # admission_id = fields.Many2one("admission.info", "Admission ID")

    refund_amount = fields.Float("Refund Amount", default=0.0)
    total = fields.Float(string='Grand Total', digits='Discount')
    paid = fields.Float("Paid Amount")
    adv = fields.Float(string='Advance')
    due_amount = fields.Float("Due Amount", default=0.0)
    doctors_payment = fields.Integer("Doctors Payment")
    broker_payment = fields.Integer("Broker Payment")
    already_collected = fields.Boolean("Already collected")
    user_id = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user.id)
    payment_type = fields.Selection([
        ('due_pay', 'Due Payment'),
        ('adv', 'Advance'),
        ('cash', 'Cash'),
        ('refund', 'Refund'),
        ('card', 'Card')], 'Payment Type', default='cash')


    ac_no = fields.Char(string="Card A/C No.")
    psn = fields.Char(string="MFS Payment A/C")
    mcash_mobile_no_payment = fields.Char(string="M-Cash Mobile")
    card_paid = fields.Float("Card Amount")
    card_amount = fields.Float("Card Amount")
    mfs_paid = fields.Float("MFS Amount")
    mfs_amount = fields.Float("MFS Amount")
    cash_paid = fields.Float("Cash Amount")
    cash_amount = fields.Float("Cash Amount")
    card_no_payment = fields.Char(string="Card No.")
    payment_process_type = fields.Selection([('cash', 'Cash'),
                                             ('card', 'Card'),
                                             ('m_cash', 'MFS'),
                                             ('card_cash', 'Cash & Card'),
                                             ('m_cash_cash', 'Cash & MFS'),
                                             ('m_cash_card', 'MFS & Card'),
                                             ('card_cash_mcash', 'Cash, Card & MFS')], default='cash')
    # payment_line_ids = fields.One2many('bill.paymentline.info', 'money_receipt_id', string='Bill Payment Receipt')
    # optics_payment_line_ids = fields.One2many('optics.sale.payment.line', 'money_receipt_id', string='Optics Payment Receipt')
    # admission_payment_line_ids = fields.One2many('hospital_admission.payment.line', 'money_receipt_id', string='Admission Payment Receipt')
    # Cancel Field --------------
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='confirmed', track_visibility='onchange')


    def customer_cancel(self):
        pass

    def create(self, vals, context=None):
        if context is None:
            context = {}
        res = super(MoneyReceipt, self).create(vals, context)
        return res

    #
    def btn_print_receipt(self):
        return self.env.ref('kolpolok_hms.report_money_receipt_action_form').report_action(self)

    @api.model
    def create(self, vals):
        # Create the record using super()
        record = super(MoneyReceipt, self).create(vals)

        # Check if the record was created successfully
        if record:
            # Generate the MR name text
            mr_name_text = 'MR-0100' + str(record.id)

            # Update the name field of the created record
            record.write({'name': mr_name_text})

        return record