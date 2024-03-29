# from .admission import pending_admission_form
# from .admission import admission_reverse_model
# # from .admission.report import all_admission_report
# from .admission.release_note import release_note
# from .admission import admission_report_wizard
# from .appointment.report import details_appointment

from .ambulance import ambulance_management

# from .appointment import appointment_booking
# from .appointment import appointment_paid
# from .appointment import appointment_payment
# from .appointment import investigation_payment
# from .appointment import create_appointment


# from .bill_payment import bill_payment_form
from .bill_payment import payment_type
from .bill_payment import advance_cash

from .money_receipt import money_receipt, all_patient_report
from .money_receipt.journal import journal_receipt
from .money_receipt import wizard_money_receipt

# from .blood_bank import blood_bank
#
# from .cash_collection import cash_collection
# from .cash_collection import cc_collection_reprot_wizard
#
# from .diagnosis import diagnosis_info
#
# from .commission_configure import commission_configure
# from .commission_configure import commission_payment
# from .custom_inherit_model import res_config_settings
#
# from .discount import pending_discount, discount_category, discount_configuration, corporate_discount_configuration


from .emergency_admission import emergency_admission_form



# from .investigation import bill_model
# from .investigation import investigation_reverse_model
#
#
#
# from .inventory import ipe_inventory
# from .inventory import inventory_requisition
#
# from .laundry_linen import linen_entry


from .opd import opd_ticket, opd_ticket_item


# from .optic_sale import optic_sales, optic_lens

from .profile.broker import broker_profile
from .profile.doctor import doctors_profile
from .profile.patient import patient_form
from .profile.patient import all_patient_report
from .profile.patient import patient_report_wizard
from .profile.gaurantor import guarantor_profile
# from .profile.patient.report import barcode_generator

# # from .pharmacy_item import pharmacy_item_entry
#
#
# # from .configure import res_partner
#
#
# from .insurrance import hospital_insurance
# from .insurrance import hospital_insurance_plan
#
# from .prescription import hospital_prescription_order
# from .prescription import hospital_prescription_line



# from .labrotary import hospital_lab
# # from .labrotary import hospital_physician
# from .labrotary import hospital_test_type
# from .labrotary import hospital_test_critearea
# from .labrotary import hospital_lab_test_units
# from .labrotary import hospital_patient_lab_test
# from .labrotary .wizard import hospital_lab_test_invoice_wizard


# from .medication import hospital_medication_dosage, hospital_medicament, hospital_vaccitation, hospital_patient_medication
# from .hospital_drug import hospital_drug_route, hospital_dose_unit


from .configure import prescriptions, department, item_entry, package_info, hospital_patient_disease, hospital_pathology, hospital_pathology_category
# from .configure import res_partner

from .ward_management import ward_management,bed_cabin_management