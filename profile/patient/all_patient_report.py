from odoo import fields, models, api


class AllAdmissionReportInfo(models.AbstractModel):
    _name = 'report.kolpolok_hms.patient_details_report_template'
    _description = 'Patient Report'


    # This function is used for the get reprot data of patient
    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     domain = []
    #     gender = data.get('form_data').get('gender')
    #     age = data.get('form_data').get('age')
    #
    #     if gender:
    #         domain += [('gender', '=', gender)]
    #     else:
    #         # If gender is not specified, include both male and female patients
    #         domain += ['|', '|', ('gender', '=', 'male'), ('gender', '=', 'female'), ('gender', '=', 'kids')]
    #
    #     if age != 0:
    #         domain += [('age', '=', age)]
    #
    #     docs = self.env['patient.info'].search(domain)
    #     return {
    #         'docs': docs,
    #     }

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = []
        gender = data.get('form_data').get('gender')
        age = data.get('form_data').get('age')
        start_date = data.get('form_data').get('start_date')
        end_date = data.get('form_data').get('end_date')

        if gender:
            domain += [('gender', '=', gender)]
        else:
            # If gender is not specified, include both male, female, and kids patients
            domain += ['|', '|', ('gender', '=', 'male'), ('gender', '=', 'female'), ('gender', '=', 'kids')]

        if age != 0:
            domain += [('age', '=', age)]

        # Add condition for patient_create_date if start_date and end_date are provided
        if start_date and end_date:
            domain += [('create_date', '>=', start_date), ('create_date', '<=', end_date)]

        docs = self.env['patient.info'].search(domain)
        return {
            'docs': docs,
        }
