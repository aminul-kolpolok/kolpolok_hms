# -*- coding: utf-8 -*-
{
    'name': "Kolpolok Hospital Management",
    'summary': "This Hospital Management is adde Patient profie with report, Doctor profile, Broker profile, Patient Gaurranter profile, Emergency Module, "
               "Ward management, Payment Management, OPD ticket Management, Item Configuration, Ambulance Services, item configuration and other ........",
    'description': "Kolpolok General Hospital",
    'sequence': '-010',
    'author': "This is demo Hospital Management of Kolpolok, if need full Hospital Management system, Please contact: info@kolpolok.com",
    'version': '0.16',
    'depends': ['base','mail','product','stock','sale_management', 'account', 'hr'],
    'assets': {'web.asset_backend':['lions_Hospital_v_03/static/src/css/custom.css',],'web.asset_fronted':['kolpolok_hms/static/src/css/custom.css',],},

    'data': [
        'security/ir.model.access.csv',

        'profile/patient/patient_report_wizard.xml',
        'ambulance/ambulance_view.xml',
        'ambulance/ambulance_booking_view.xml',
        'ambulance/ambulance_expense_view.xml',


        'money_receipt/report/report_view.xml',
        'money_receipt/report/money_receipt_form_print.xml',
        'money_receipt/report/money_receipt_report_print_format.xml',
        #

        # 'admission/report/details_admission_report_print.xml',
        # 'admission/report/admission_form_print.xml',
        #
        # 'diagnosis/diagnosis_form_view.xml',


        # 'admission/report/release_print_view.xml',
        # 'appointment/report/appointment_print_view.xml',
        # 'appointment/report/details_appointment_view.xml',
        # 'appointment/appointment_booking_view.xml',
        # 'appointment/appointment_paid_view.xml',
        # 'appointment/appointment_payment_view.xml',
        # 'appointment/investigation_payment_view.xml',
        # 'appointment/create_appointment_view.xml',

        # 'bill_payment/bill_payment_form.xml',
        'bill_payment/payment_type.xml',
        'bill_payment/advance_cash_view.xml',
        'money_receipt/money_receipt_view.xml',

        # 'blood_bank/blood_donor_view.xml',
        # 'blood_bank/blood_receiver_view.xml',

        # 'cash_collection/cash_collection_view.xml',
        # 'cash_collection/cc_collection_report_wizard.xml',
        # 'cash_collection/report/cc_collection_report_print_view.xml',
        # 'cash_collection/report/cc_collection_wizard_report_format_download.xml',
        #
        # 'commission_configure/commission_configure_view.xml',
        # 'commission_configure/commission_payment_view.xml',

        'configure/prescriptions.xml',
        'configure/department_config.xml',
        'configure/item_entry_view.xml',
        'configure/package_view.xml',
        'configure/hospital_patient_disease.xml',
        'configure/hospital_pathology_category.xml',
        'configure/hospital_pathology.xml',

        'emergency_admission/emergency_admission_form_view.xml',


        'money_receipt/journal/journal_receipt_view.xml',

        'opd/report/report_view.xml',
        'opd/report/opd_form_print.xml',

        'opd/opd_ticket_item_view.xml',
        'opd/opd_ticket_form_view.xml',

        'profile/patient/patient_view.xml',
        'profile/patient/report/patient_card.xml',
        'profile/broker/broker_view.xml',
        'profile/doctor/doctors_view.xml',
        'profile/gaurantor/guarantor_form_view.xml',

        'profile/patient/report/patient_report_print_format.xml',
        'profile/patient/report/patient_diseases_document_report.xml',
        'profile/patient/report/patient_medications_document_report.xml',
        'profile/patient/report/patient_vaccinations_document_report.xml',




        'report/mail_template.xml',
        'report/mail_template_appointment.xml',
        # 'report/custom_header_footer.xml',
        'report/report_view.xml',


    ],
    'installable': True,
    'auto_install': False
}
