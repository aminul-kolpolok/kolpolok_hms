from odoo import fields, models, api


class AllPatientReportInfo(models.AbstractModel):
    _name = 'report.kolpolok_hms.patient_details_report_template'
    _description = 'Patient Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # print("Hellow Data! Testing----------------")
        domain = []
        gender = data.get('form_data').get('gender')
        age = data.get('form_data').get('age')
        if gender:
            domain += [('gender', '=', gender)]

        if age != 0:
            domain += [('age', '=', age)]
        docs = self.env['patient.info'].search(domain)
        return {
            'docs': docs,
        }
