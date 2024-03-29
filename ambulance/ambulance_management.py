import odoo.addons
from odoo import fields, models, api


class AmbulanceRegistration(models.Model):
    _name = 'ambulance.registration'
    _rec_name = 'vehicle_name'

    vehicle_id = fields.Char("Vehicle ID", readonly=True)
    vehicle_type = fields.Char("Vehicle Type")
    vehicle_number = fields.Char("Vehicle Number")
    vehicle_name = fields.Char("Vehicle Name")
    state = fields.Selection([
        ('in-service', 'In Service')
        , ('warn-out', 'Warn Out')
        , ('dispose', 'Dispose'), ],
        "Status", default='in-service')

    @api.model
    def create(self, vals):
        record = super().create(vals)
        if record:
            ambulance_serial_no = 'Ambulance-0' + str(record.id)
            record.update({'vehicle_id': ambulance_serial_no})
        return record

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f"{record.vehicle_name} {'-'} {record.vehicle_id or '--'}"))
        return res

class AmbulanceBooking(models.Model):
    _name = 'ambulance.booking'
    _rec_name = 'ambulance_id'

    date = fields.Datetime("Date", default=fields.Datetime.now())
    booking_type = fields.Char("Booking Type")
    customer_name = fields.Char('Customer Name')
    patient_name = fields.Many2one('patient.info', "Patient Name")
    mobile = fields.Char("Mobile", related='patient_name.mobile')
    start_from = fields.Char('Start/Pick-up Place')
    destination = fields.Char('Destination')
    amount = fields.Float('Amount')
    advance_amount = fields.Float('Advance Amount')
    paid_amount = fields.Float('Paid Amount')
    unpaid_amount = fields.Float('Unpaid Amount')
    grace_time = fields.Float('Expected Completion Time')
    req_date = fields.Datetime('Booking/Request Date and Time')
    ambulance_id = fields.Many2one('ambulance.registration', "Vehicle Name")
    state = fields.Selection([
        ('draft', 'Pending'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled'),

    ], 'Status', readonly=True, default='draft')





class AmbulanceExpense(models.Model):
    _name = 'ambulance.expense'
    _rec_name = 'ambulance_id'

    ambulance_id = fields.Many2one('ambulance.registration', "Vehicle Name", required=True)
    expense_date = fields.Datetime(string="Expense Date")
    bill_to = fields.Char(string="Bill Submitted To")
    fuel_type = fields.Selection(string='Fuel Type.',
                                 selection=[('patrol', 'Patrol Oil'),
                                            ('disal', 'Disel Oil'),('gas', 'Gas LPG'),
                                            ('octene', 'Octene Oil'),
                                            ('mobil', 'Mobil Oil'),
                                            ('other', 'Other Oil')], default='gas')
    fuel_quantity = fields.Char('Fuel Quantity')
    fuel_cost = fields.Float('Fuel Cost')
    other_cost = fields.Float('Other Cost')
    total_cost = fields.Float('Other Cost')
    description = fields.Text('Reason')
    state = fields.Selection([
        ('draft', 'Pending'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled'),
    ], 'Status', readonly=True)
