# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2015, CRS4
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from hl7apy.utils import iteritems

DATATYPES = {
    'AD_1': ['leaf', None, 'ST', 'STREET_ADDRESS', None, -1],
    'AD_2': ['leaf', None, 'ST', 'OTHER_DESIGNATION', None, -1],
    'AD_3': ['leaf', None, 'ST', 'CITY', None, -1],
    'AD_4': ['leaf', None, 'ST', 'STATE_OR_PROVINCE', None, -1],
    'AD_5': ['leaf', None, 'ID', 'ZIP_OR_POSTAL_CODE', None, -1],
    'AD_6': ['leaf', None, 'ID', 'COUNTRY', None, -1],
    'AD_7': ['leaf', None, 'ID', 'TYPE', None, -1],
    'AD_8': ['leaf', None, 'ST', 'OTHER_GEOGRAPHIC_DESIGNATION', None, -1],
    'CE_1': ['leaf', None, 'ID', 'IDENTIFIER', None, -1],
    'CE_2': ['leaf', None, 'ST', 'TEXT', None, -1],
    'CE_3': ['leaf', None, 'ST', 'NAME_OF_CODING_SYSTEM', None, -1],
    'CE_4': ['leaf', None, 'ST', 'ALTERNATE_IDENTIFIER', None, -1],
    'CE_5': ['leaf', None, 'ST', 'ALTERNATE_TEXT', None, -1],
    'CE_6': ['leaf', None, 'ST', 'NAME_OF_ALTERNATE_CODING_SYSTEM', None, -1],
    'CK_1': ['leaf', None, 'NM', 'ID_NUMBER', None, -1],
    'CK_2': ['leaf', None, 'NM', 'CHECK_DIGIT', None, -1],
    'CK_3': ['leaf', None, 'ID', 'CHECK_DIGIT_SCHEME', 'HL70061', -1],
    'CK_4': ['leaf', None, 'ST', 'ASSIGNING_FACILITY_ID', None, -1],
    'CK_ACCOUNT_NO_1': ['leaf', None, 'NM', 'ACCOUNT_NUMBER', None, -1],
    'CK_ACCOUNT_NO_2': ['leaf', None, 'NM', 'CHECK_DIGIT', None, -1],
    'CK_ACCOUNT_NO_3': ['leaf', None, 'ID', 'CHECK_DIGIT_SCHEME', None, -1],
    'CK_ACCOUNT_NO_4': ['leaf', None, 'ID', 'FACILITY_ID', None, -1],
    'CM_ABS_RANGE_1': ['sequence', None, 'CM_RANGE', 'RANGE', None, -1],
    'CM_ABS_RANGE_2': ['leaf', None, 'NM', 'NUMERIC_CHANGE', None, -1],
    'CM_ABS_RANGE_3': ['leaf', None, 'NM', 'PERCENT_PER_CHANGE', None, -1],
    'CM_ABS_RANGE_4': ['leaf', None, 'NM', 'DAYS', None, -1],
    'CM_AUI_1': ['leaf', None, 'ST', 'AUTHORIZATION_NUMBER', None, -1],
    'CM_AUI_2': ['leaf', None, 'DT', 'DATE', None, -1],
    'CM_AUI_3': ['leaf', None, 'ST', 'SOURCE', None, -1],
    'CM_BATCH_TOTAL_1': ['leaf', None, 'NM', 'CM_BATCH_TOTAL_1', None, -1],
    'CM_BATCH_TOTAL_2': ['leaf', None, 'NM', 'CM_BATCH_TOTAL_2', None, -1],
    'CM_CCD_1': ['leaf', None, 'ID', 'WHEN_TO_CHARGE', None, -1],
    'CM_CCD_2': ['sequence', None, 'TS', 'DATE_TIME', None, -1],
    'CM_DDI_1': ['leaf', None, 'ST', 'DELAY_DAYS', None, -1],
    'CM_DDI_2': ['leaf', None, 'NM', 'AMOUNT', None, -1],
    'CM_DDI_3': ['leaf', None, 'NM', 'NUMBER_OF_DAYS', None, -1],
    'CM_DIN_1': ['sequence', None, 'TS', 'DATE', None, -1],
    'CM_DIN_2': ['sequence', None, 'CE', 'INSTITUTION_NAME', None, -1],
    'CM_DLD_1': ['leaf', None, 'ID', 'DISCHARGE_LOCATION', None, -1],
    'CM_DLD_2': ['sequence', None, 'TS', 'EFFECTIVE_DATE', None, -1],
    'CM_DLT_1': ['sequence', None, 'CM_RANGE', 'RANGE', None, -1],
    'CM_DLT_2': ['leaf', None, 'NM', 'NUMERIC_THRESHOLD', None, -1],
    'CM_DLT_3': ['leaf', None, 'ST', 'CHANGE', None, -1],
    'CM_DLT_4': ['leaf', None, 'NM', 'LENGTH_OF_TIME_DAYS', None, -1],
    'CM_DTN_1': ['leaf', None, 'ID', 'DAY_TYPE', None, -1],
    'CM_DTN_2': ['leaf', None, 'NM', 'NUMBER_OF_DAYS', None, -1],
    'CM_EIP_1': ['leaf', None, 'ST', 'PARENT_S_PLACER_ORDER_NUMBER', None, -1],
    'CM_EIP_2': ['leaf', None, 'ST', 'PARENT_S_FILLER_ORDER_NUMBER', None, -1],
    'CM_ELD_1': ['leaf', None, 'ST', 'SEGMENT_ID', None, -1],
    'CM_ELD_2': ['leaf', None, 'NM', 'SEQUENCE', None, -1],
    'CM_ELD_3': ['leaf', None, 'NM', 'FIELD_POSITION', None, -1],
    'CM_ELD_4': ['sequence', None, 'CE', 'CODE_IDENTIFYING_ERROR', None, -1],
    'CM_FILLER_1': ['leaf', None, 'ID', 'UNIQUE_FILLER_ID', None, -1],
    'CM_FILLER_2': ['leaf', None, 'ID', 'FILLER_APPLICATION_ID', None, -1],
    'CM_FINANCE_1': ['leaf', None, 'ID', 'FINANCIAL_CLASS_ID', None, -1],
    'CM_FINANCE_2': ['sequence', None, 'TS', 'EFFECTIVE_DATE', None, -1],
    'CM_GROUP_ID_1': ['leaf', None, 'ID', 'UNIQUE_GROUP_ID', None, -1],
    'CM_GROUP_ID_2': ['leaf', None, 'ID', 'PLACER_APPLICATION_ID', None, -1],
    'CM_INTERNAL_LOCATION_1': ['leaf', None, 'ID', 'NURSE_UNIT_STATION', None, -1],
    'CM_INTERNAL_LOCATION_2': ['leaf', None, 'ID', 'ROOM', None, -1],
    'CM_INTERNAL_LOCATION_3': ['leaf', None, 'ID', 'BED', None, -1],
    'CM_INTERNAL_LOCATION_4': ['leaf', None, 'ID', 'FACILITY_ID', None, -1],
    'CM_INTERNAL_LOCATION_5': ['leaf', None, 'ID', 'BED_STATUS', None, -1],
    'CM_INTERNAL_LOCATION_6': ['leaf', None, 'ID', 'ETAGE', None, -1],
    'CM_INTERNAL_LOCATION_7': ['leaf', None, 'ID', 'KLINIK', None, -1],
    'CM_INTERNAL_LOCATION_8': ['leaf', None, 'ID', 'ZENTRUM', None, -1],
    'CM_JOB_CODE_1': ['leaf', None, 'ID', 'JOB_CODE', None, -1],
    'CM_JOB_CODE_2': ['leaf', None, 'ID', 'EMPLOYEE_CLASSIFICATION', None, -1],
    'CM_LA1_1': ['sequence', None, 'CM_INTERNAL_LOCATION', 'DISPENSE_DELIVER_TO_LOCATION', None, -1],
    'CM_LA1_2': ['sequence', None, 'AD', 'LOCATION', None, -1],
    'CM_LICENSE_NO_1': ['leaf', None, 'ST', 'LICENSE_NUMBER', None, -1],
    'CM_LICENSE_NO_2': ['leaf', None, 'ST', 'ISSUING_STATE_PROVINCE_COUNTRY', None, -1],
    'CM_MOC_1': ['leaf', None, 'ST', 'DOLLAR_AMOUNT', None, -1],
    'CM_MOC_2': ['leaf', None, 'ST', 'CHARGE_CODE', None, -1],
    'CM_MSG_1': ['leaf', None, 'ID', 'MESSAGE_TYPE', None, -1],
    'CM_MSG_2': ['leaf', None, 'ID', 'TRIGGER_EVENT', None, -1],
    'CM_NDL_1': ['sequence', None, 'CN', 'INTERPRETER_TECHNICIAN', None, -1],
    'CM_NDL_2': ['sequence', None, 'TS', 'START_DATE_TIME', None, -1],
    'CM_NDL_3': ['sequence', None, 'TS', 'END_DATE_TIME', None, -1],
    'CM_NDL_4': ['sequence', None, 'CM_INTERNAL_LOCATION', 'LOCATION', None, -1],
    'CM_OCD_1': ['leaf', None, 'ID', 'OCCURRENCE_CODE', None, -1],
    'CM_OCD_2': ['leaf', None, 'DT', 'OCCURRENCE_DATE', None, -1],
    'CM_OSP_1': ['leaf', None, 'ID', 'OCCURRENCE_SPAN_CODE', None, -1],
    'CM_OSP_2': ['leaf', None, 'DT', 'OCCURRENCE_SPAN_START_DATE', None, -1],
    'CM_OSP_3': ['leaf', None, 'DT', 'OCCURRENCE_SPAN_STOP_DATE', None, -1],
    'CM_PARENT_RESULT_1': ['sequence', None, 'CE', 'OBSERVATION_IDENTIFIER_OBX_3_OF_PARENT_RESULT', None, -1],
    'CM_PARENT_RESULT_2': ['leaf', None, 'ST', 'SUB_ID_OBX_4_OF_PARENT_RESULT', None, -1],
    'CM_PARENT_RESULT_3': ['sequence', None, 'CE', 'RESULT_OBX_5_OF_PARENT_RESULT', None, -1],
    'CM_PAT_ID_1': ['leaf', None, 'ST', 'PATIENT_ID', None, -1],
    'CM_PAT_ID_2': ['leaf', None, 'NM', 'CHECK_DIGIT', None, -1],
    'CM_PAT_ID_3': ['leaf', None, 'ID', 'CHECK_DIGIT_SCHEME', None, -1],
    'CM_PAT_ID_4': ['leaf', None, 'ID', 'FACILITY_ID', None, -1],
    'CM_PAT_ID_5': ['leaf', None, 'ID', 'TYPE', None, -1],
    'CM_PAT_ID_0192_1': ['leaf', None, 'ST', 'PATIENT_ID', None, -1],
    'CM_PAT_ID_0192_2': ['leaf', None, 'NM', 'CHECK_DIGIT', None, -1],
    'CM_PAT_ID_0192_3': ['leaf', None, 'ID', 'CHECK_DIGIT_SCHEME', None, -1],
    'CM_PAT_ID_0192_4': ['leaf', None, 'ID', 'FACILITY_ID', None, -1],
    'CM_PAT_ID_0192_5': ['leaf', None, 'ID', 'TYPE', 'HL70192', -1],
    'CM_PCF_1': ['leaf', None, 'ID', 'PRE_CERTIFICATION_PATIENT_TYPE', None, -1],
    'CM_PCF_2': ['leaf', None, 'ID', 'PRE_CERTICATION_REQUIRED', None, -1],
    'CM_PCF_3': ['sequence', None, 'TS', 'PRE_CERTIFICATION_WINDOW', None, -1],
    'CM_PEN_1': ['leaf', None, 'ID', 'PENALTY_ID', None, -1],
    'CM_PEN_2': ['leaf', None, 'NM', 'PENALTY_AMOUNT', None, -1],
    'CM_PIP_1': ['sequence', None, 'CE', 'PRIVILEGE', None, -1],
    'CM_PIP_2': ['sequence', None, 'CE', 'PRIVILEGE_CLASS', None, -1],
    'CM_PIP_3': ['leaf', None, 'DT', 'EXPIRATION_DATE', None, -1],
    'CM_PIP_4': ['leaf', None, 'DT', 'ACTIVATION_DATE', None, -1],
    'CM_PLACER_1': ['leaf', None, 'ID', 'UNIQUE_PLACER_ID', None, -1],
    'CM_PLACER_2': ['leaf', None, 'ID', 'PLACER_APPLICATION', None, -1],
    'CM_PLN_1': ['leaf', None, 'ST', 'ID_NUMBER', None, -1],
    'CM_PLN_2': ['leaf', None, 'ID', 'TYPE_OF_ID_NUMBER_ID', None, -1],
    'CM_PLN_3': ['leaf', None, 'ST', 'STATE_OTHER_QUALIFIYING_INFO', None, -1],
    'CM_POSITION_1': ['leaf', None, 'ST', 'SAAL', None, -1],
    'CM_POSITION_2': ['leaf', None, 'ST', 'TISCH', None, -1],
    'CM_POSITION_3': ['leaf', None, 'ST', 'STUHL', None, -1],
    'CM_PRACTITIONER_1': ['sequence', None, 'CN', 'PROCEDURE_PRACTITIONER_ID', None, -1],
    'CM_PRACTITIONER_2': ['leaf', None, 'ID', 'PROCEDURE_PRACTITIONER_TYPE', None, -1],
    'CM_PTA_1': ['leaf', None, 'ID', 'POLICY_TYPE', 'HL70147', -1],
    'CM_PTA_2': ['leaf', None, 'ID', 'AMOUNT_CLASS', 'HL70193', -1],
    'CM_PTA_3': ['leaf', None, 'NM', 'AMOUNT', None, -1],
    'CM_RANGE_1': ['sequence', None, 'CE', 'LOW_VALUE', None, -1],
    'CM_RANGE_2': ['sequence', None, 'CE', 'HIGH_VALUE', None, -1],
    'CM_RFR_1': ['sequence', None, 'CE', 'REFERENCE_RANGE', None, -1],
    'CM_RFR_2': ['leaf', None, 'ID', 'SEX', None, -1],
    'CM_RFR_3': ['sequence', None, 'CE', 'AGE_RANGE', None, -1],
    'CM_RFR_4': ['sequence', None, 'CE', 'GESTATIONAL_AGE_RANGE', None, -1],
    'CM_RFR_5': ['leaf', None, 'ST', 'SPECIES', None, -1],
    'CM_RFR_6': ['leaf', None, 'ID', 'RACE_SUBSPECIES', None, -1],
    'CM_RFR_7': ['leaf', None, 'ST', 'TEXT_CONDITION', None, -1],
    'CM_RMC_1': ['leaf', None, 'ID', 'ROOM_TYPE', None, -1],
    'CM_RMC_2': ['leaf', None, 'ID', 'AMOUNT_TYPE', None, -1],
    'CM_RMC_3': ['leaf', None, 'NM', 'COVERAGE_AMOUNT', None, -1],
    'CM_SPD_1': ['leaf', None, 'ST', 'SPECIALTY_NAME', None, -1],
    'CM_SPD_2': ['leaf', None, 'ST', 'GOVERNING_BOARD', None, -1],
    'CM_SPD_3': ['leaf', None, 'ID', 'ELIGIBLE_OR_CERTIFIED', None, -1],
    'CM_SPD_4': ['leaf', None, 'DT', 'DATE_OF_CERTIFICATION', None, -1],
    'CM_SPS_1': ['sequence', None, 'CE', 'SPECIMEN_SOURCE_NAME_OR_CODE', None, -1],
    'CM_SPS_2': ['leaf', None, 'TX', 'ADDITIVES', None, -1],
    'CM_SPS_3': ['leaf', None, 'TX', 'FREETEXT', None, -1],
    'CM_SPS_4': ['sequence', None, 'CE', 'BODY_SITE', None, -1],
    'CM_SPS_5': ['sequence', None, 'CE', 'SITE_MODIFIER', None, -1],
    'CM_UVC_1': ['leaf', None, 'ID', 'VALUE_CODE', None, -1],
    'CM_UVC_2': ['leaf', None, 'NM', 'VALUE_AMOUNT', None, -1],
    'CM_VR_1': ['leaf', None, 'ST', 'FIRST_DATA_CODE_VALUE', None, -1],
    'CM_VR_2': ['leaf', None, 'ST', 'LAST_DATA_CODE_CALUE', None, -1],
    'CN_1': ['leaf', None, 'ID', 'ID_NUMBER', None, -1],
    'CN_2': ['leaf', None, 'ST', 'FAMILIY_NAME', None, -1],
    'CN_3': ['leaf', None, 'ST', 'GIVEN_NAME', None, -1],
    'CN_4': ['leaf', None, 'ST', 'MIDDLE_INITIAL_OR_NAME', None, -1],
    'CN_5': ['leaf', None, 'ST', 'SUFFIX_E_G_JR_OR_III', None, -1],
    'CN_6': ['leaf', None, 'ST', 'PREFIX_E_G_DR', None, -1],
    'CN_7': ['leaf', None, 'ST', 'DEGREE_E_G_MD', None, -1],
    'CN_8': ['leaf', None, 'ID', 'SOURCE_TABLE_ID', None, -1],
    'CQ_1': ['leaf', None, 'ST', 'QUANTITY', None, -1],
    'CQ_2': ['leaf', None, 'ST', 'UNITS', None, -1],
    'PN_1': ['leaf', None, 'ST', 'FAMILIY_NAME', None, -1],
    'PN_2': ['leaf', None, 'ST', 'GIVEN_NAME', None, -1],
    'PN_3': ['leaf', None, 'ST', 'MIDDLE_INITIAL_OR_NAME', None, -1],
    'PN_4': ['leaf', None, 'ST', 'SUFFIX_E_G_JR_OR_III', None, -1],
    'PN_5': ['leaf', None, 'ST', 'PREFIX_E_G_DR', None, -1],
    'PN_6': ['leaf', None, 'ST', 'DEGREE_E_G_MD', None, -1],
    'RI_1': ['leaf', None, 'ST', 'REPEAT_PATTERN', None, -1],
    'RI_2': ['leaf', None, 'ST', 'EXPLICIT_TIME_INTEVALL', None, -1],
    'TQ_1': ['sequence', None, 'CQ', 'QUANTITY', None, -1],
    'TQ_2': ['sequence', None, 'RI', 'INTERVAL', None, -1],
    'TQ_3': ['leaf', None, 'ST', 'DURATION', None, -1],
    'TQ_4': ['sequence', None, 'TS', 'START_DATE_TIME', None, -1],
    'TQ_5': ['sequence', None, 'TS', 'END_DATE_TIME', None, -1],
    'TQ_6': ['leaf', None, 'ID', 'PRIORITY', None, -1],
    'TQ_7': ['leaf', None, 'ST', 'CONDITION', None, -1],
    'TQ_8': ['leaf', None, 'TX', 'TEXT_TX', None, -1],
    'TQ_9': ['leaf', None, 'ID', 'CONJUNCTION', None, -1],
    'TQ_10': ['leaf', None, 'ST', 'ORDER_SEQUENCING', None, -1],
    'TS_1': ['leaf', None, 'ST', 'TIME_OF_AN_EVENT', None, -1],
    'TS_2': ['leaf', None, 'ST', 'DEGREE_OF_PRECISION', None, -1],
}


DATATYPES_STRUCTS = {
    'AD': (
           ('AD_1', DATATYPES['AD_1'], (0, 1), 'CMP'),
           ('AD_2', DATATYPES['AD_2'], (0, 1), 'CMP'),
           ('AD_3', DATATYPES['AD_3'], (0, 1), 'CMP'),
           ('AD_4', DATATYPES['AD_4'], (0, 1), 'CMP'),
           ('AD_5', DATATYPES['AD_5'], (0, 1), 'CMP'),
           ('AD_6', DATATYPES['AD_6'], (0, 1), 'CMP'),
           ('AD_7', DATATYPES['AD_7'], (0, 1), 'CMP'),
           ('AD_8', DATATYPES['AD_8'], (0, 1), 'CMP'),),
    'CE': (
           ('CE_1', DATATYPES['CE_1'], (0, 1), 'CMP'),
           ('CE_2', DATATYPES['CE_2'], (0, 1), 'CMP'),
           ('CE_3', DATATYPES['CE_3'], (0, 1), 'CMP'),
           ('CE_4', DATATYPES['CE_4'], (0, 1), 'CMP'),
           ('CE_5', DATATYPES['CE_5'], (0, 1), 'CMP'),
           ('CE_6', DATATYPES['CE_6'], (0, 1), 'CMP'),),
    'CK': (
           ('CK_1', DATATYPES['CK_1'], (0, 1), 'CMP'),
           ('CK_2', DATATYPES['CK_2'], (0, 1), 'CMP'),
           ('CK_3', DATATYPES['CK_3'], (0, 1), 'CMP'),
           ('CK_4', DATATYPES['CK_4'], (0, 1), 'CMP'),),
    'CK_ACCOUNT_NO': (
           ('CK_ACCOUNT_NO_1', DATATYPES['CK_ACCOUNT_NO_1'], (0, 1), 'CMP'),
           ('CK_ACCOUNT_NO_2', DATATYPES['CK_ACCOUNT_NO_2'], (0, 1), 'CMP'),
           ('CK_ACCOUNT_NO_3', DATATYPES['CK_ACCOUNT_NO_3'], (0, 1), 'CMP'),
           ('CK_ACCOUNT_NO_4', DATATYPES['CK_ACCOUNT_NO_4'], (0, 1), 'CMP'),),
    'CM_ABS_RANGE': (
           ('CM_ABS_RANGE_1', DATATYPES['CM_ABS_RANGE_1'], (0, 1), 'CMP'),
           ('CM_ABS_RANGE_2', DATATYPES['CM_ABS_RANGE_2'], (0, 1), 'CMP'),
           ('CM_ABS_RANGE_3', DATATYPES['CM_ABS_RANGE_3'], (0, 1), 'CMP'),
           ('CM_ABS_RANGE_4', DATATYPES['CM_ABS_RANGE_4'], (0, 1), 'CMP'),),
    'CM_AUI': (
           ('CM_AUI_1', DATATYPES['CM_AUI_1'], (0, 1), 'CMP'),
           ('CM_AUI_2', DATATYPES['CM_AUI_2'], (0, 1), 'CMP'),
           ('CM_AUI_3', DATATYPES['CM_AUI_3'], (0, 1), 'CMP'),),
    'CM_BATCH_TOTAL': (
           ('CM_BATCH_TOTAL_1', DATATYPES['CM_BATCH_TOTAL_1'], (0, 1), 'CMP'),
           ('CM_BATCH_TOTAL_2', DATATYPES['CM_BATCH_TOTAL_2'], (0, 1), 'CMP'),),
    'CM_CCD': (
           ('CM_CCD_1', DATATYPES['CM_CCD_1'], (0, 1), 'CMP'),
           ('CM_CCD_2', DATATYPES['CM_CCD_2'], (0, 1), 'CMP'),),
    'CM_DDI': (
           ('CM_DDI_1', DATATYPES['CM_DDI_1'], (0, 1), 'CMP'),
           ('CM_DDI_2', DATATYPES['CM_DDI_2'], (0, 1), 'CMP'),
           ('CM_DDI_3', DATATYPES['CM_DDI_3'], (0, 1), 'CMP'),),
    'CM_DIN': (
           ('CM_DIN_1', DATATYPES['CM_DIN_1'], (0, 1), 'CMP'),
           ('CM_DIN_2', DATATYPES['CM_DIN_2'], (0, 1), 'CMP'),),
    'CM_DLD': (
           ('CM_DLD_1', DATATYPES['CM_DLD_1'], (0, 1), 'CMP'),
           ('CM_DLD_2', DATATYPES['CM_DLD_2'], (0, 1), 'CMP'),),
    'CM_DLT': (
           ('CM_DLT_1', DATATYPES['CM_DLT_1'], (0, 1), 'CMP'),
           ('CM_DLT_2', DATATYPES['CM_DLT_2'], (0, 1), 'CMP'),
           ('CM_DLT_3', DATATYPES['CM_DLT_3'], (0, 1), 'CMP'),
           ('CM_DLT_4', DATATYPES['CM_DLT_4'], (0, 1), 'CMP'),),
    'CM_DTN': (
           ('CM_DTN_1', DATATYPES['CM_DTN_1'], (0, 1), 'CMP'),
           ('CM_DTN_2', DATATYPES['CM_DTN_2'], (0, 1), 'CMP'),),
    'CM_EIP': (
           ('CM_EIP_1', DATATYPES['CM_EIP_1'], (0, 1), 'CMP'),
           ('CM_EIP_2', DATATYPES['CM_EIP_2'], (0, 1), 'CMP'),),
    'CM_ELD': (
           ('CM_ELD_1', DATATYPES['CM_ELD_1'], (0, 1), 'CMP'),
           ('CM_ELD_2', DATATYPES['CM_ELD_2'], (0, 1), 'CMP'),
           ('CM_ELD_3', DATATYPES['CM_ELD_3'], (0, 1), 'CMP'),
           ('CM_ELD_4', DATATYPES['CM_ELD_4'], (0, 1), 'CMP'),),
    'CM_FILLER': (
           ('CM_FILLER_1', DATATYPES['CM_FILLER_1'], (0, 1), 'CMP'),
           ('CM_FILLER_2', DATATYPES['CM_FILLER_2'], (0, 1), 'CMP'),),
    'CM_FINANCE': (
           ('CM_FINANCE_1', DATATYPES['CM_FINANCE_1'], (0, 1), 'CMP'),
           ('CM_FINANCE_2', DATATYPES['CM_FINANCE_2'], (0, 1), 'CMP'),),
    'CM_GROUP_ID': (
           ('CM_GROUP_ID_1', DATATYPES['CM_GROUP_ID_1'], (0, 1), 'CMP'),
           ('CM_GROUP_ID_2', DATATYPES['CM_GROUP_ID_2'], (0, 1), 'CMP'),),
    'CM_INTERNAL_LOCATION': (
           ('CM_INTERNAL_LOCATION_1', DATATYPES['CM_INTERNAL_LOCATION_1'], (0, 1), 'CMP'),
           ('CM_INTERNAL_LOCATION_2', DATATYPES['CM_INTERNAL_LOCATION_2'], (0, 1), 'CMP'),
           ('CM_INTERNAL_LOCATION_3', DATATYPES['CM_INTERNAL_LOCATION_3'], (0, 1), 'CMP'),
           ('CM_INTERNAL_LOCATION_4', DATATYPES['CM_INTERNAL_LOCATION_4'], (0, 1), 'CMP'),
           ('CM_INTERNAL_LOCATION_5', DATATYPES['CM_INTERNAL_LOCATION_5'], (0, 1), 'CMP'),
           ('CM_INTERNAL_LOCATION_6', DATATYPES['CM_INTERNAL_LOCATION_6'], (0, 1), 'CMP'),
           ('CM_INTERNAL_LOCATION_7', DATATYPES['CM_INTERNAL_LOCATION_7'], (0, 1), 'CMP'),
           ('CM_INTERNAL_LOCATION_8', DATATYPES['CM_INTERNAL_LOCATION_8'], (0, 1), 'CMP'),),
    'CM_JOB_CODE': (
           ('CM_JOB_CODE_1', DATATYPES['CM_JOB_CODE_1'], (0, 1), 'CMP'),
           ('CM_JOB_CODE_2', DATATYPES['CM_JOB_CODE_2'], (0, 1), 'CMP'),),
    'CM_LA1': (
           ('CM_LA1_1', DATATYPES['CM_LA1_1'], (0, 1), 'CMP'),
           ('CM_LA1_2', DATATYPES['CM_LA1_2'], (0, 1), 'CMP'),),
    'CM_LICENSE_NO': (
           ('CM_LICENSE_NO_1', DATATYPES['CM_LICENSE_NO_1'], (0, 1), 'CMP'),
           ('CM_LICENSE_NO_2', DATATYPES['CM_LICENSE_NO_2'], (0, 1), 'CMP'),),
    'CM_MOC': (
           ('CM_MOC_1', DATATYPES['CM_MOC_1'], (0, 1), 'CMP'),
           ('CM_MOC_2', DATATYPES['CM_MOC_2'], (0, 1), 'CMP'),),
    'CM_MSG': (
           ('CM_MSG_1', DATATYPES['CM_MSG_1'], (0, 1), 'CMP'),
           ('CM_MSG_2', DATATYPES['CM_MSG_2'], (0, 1), 'CMP'),),
    'CM_NDL': (
           ('CM_NDL_1', DATATYPES['CM_NDL_1'], (0, 1), 'CMP'),
           ('CM_NDL_2', DATATYPES['CM_NDL_2'], (0, 1), 'CMP'),
           ('CM_NDL_3', DATATYPES['CM_NDL_3'], (0, 1), 'CMP'),
           ('CM_NDL_4', DATATYPES['CM_NDL_4'], (0, 1), 'CMP'),),
    'CM_OCD': (
           ('CM_OCD_1', DATATYPES['CM_OCD_1'], (0, 1), 'CMP'),
           ('CM_OCD_2', DATATYPES['CM_OCD_2'], (0, 1), 'CMP'),),
    'CM_OSP': (
           ('CM_OSP_1', DATATYPES['CM_OSP_1'], (0, 1), 'CMP'),
           ('CM_OSP_2', DATATYPES['CM_OSP_2'], (0, 1), 'CMP'),
           ('CM_OSP_3', DATATYPES['CM_OSP_3'], (0, 1), 'CMP'),),
    'CM_PARENT_RESULT': (
           ('CM_PARENT_RESULT_1', DATATYPES['CM_PARENT_RESULT_1'], (0, 1), 'CMP'),
           ('CM_PARENT_RESULT_2', DATATYPES['CM_PARENT_RESULT_2'], (0, 1), 'CMP'),
           ('CM_PARENT_RESULT_3', DATATYPES['CM_PARENT_RESULT_3'], (0, 1), 'CMP'),),
    'CM_PAT_ID': (
           ('CM_PAT_ID_1', DATATYPES['CM_PAT_ID_1'], (0, 1), 'CMP'),
           ('CM_PAT_ID_2', DATATYPES['CM_PAT_ID_2'], (0, 1), 'CMP'),
           ('CM_PAT_ID_3', DATATYPES['CM_PAT_ID_3'], (0, 1), 'CMP'),
           ('CM_PAT_ID_4', DATATYPES['CM_PAT_ID_4'], (0, 1), 'CMP'),
           ('CM_PAT_ID_5', DATATYPES['CM_PAT_ID_5'], (0, 1), 'CMP'),),
    'CM_PAT_ID_0192': (
           ('CM_PAT_ID_0192_1', DATATYPES['CM_PAT_ID_0192_1'], (0, 1), 'CMP'),
           ('CM_PAT_ID_0192_2', DATATYPES['CM_PAT_ID_0192_2'], (0, 1), 'CMP'),
           ('CM_PAT_ID_0192_3', DATATYPES['CM_PAT_ID_0192_3'], (0, 1), 'CMP'),
           ('CM_PAT_ID_0192_4', DATATYPES['CM_PAT_ID_0192_4'], (0, 1), 'CMP'),
           ('CM_PAT_ID_0192_5', DATATYPES['CM_PAT_ID_0192_5'], (0, 1), 'CMP'),),
    'CM_PCF': (
           ('CM_PCF_1', DATATYPES['CM_PCF_1'], (0, 1), 'CMP'),
           ('CM_PCF_2', DATATYPES['CM_PCF_2'], (0, 1), 'CMP'),
           ('CM_PCF_3', DATATYPES['CM_PCF_3'], (0, 1), 'CMP'),),
    'CM_PEN': (
           ('CM_PEN_1', DATATYPES['CM_PEN_1'], (0, 1), 'CMP'),
           ('CM_PEN_2', DATATYPES['CM_PEN_2'], (0, 1), 'CMP'),),
    'CM_PIP': (
           ('CM_PIP_1', DATATYPES['CM_PIP_1'], (0, 1), 'CMP'),
           ('CM_PIP_2', DATATYPES['CM_PIP_2'], (0, 1), 'CMP'),
           ('CM_PIP_3', DATATYPES['CM_PIP_3'], (0, 1), 'CMP'),
           ('CM_PIP_4', DATATYPES['CM_PIP_4'], (0, 1), 'CMP'),),
    'CM_PLACER': (
           ('CM_PLACER_1', DATATYPES['CM_PLACER_1'], (0, 1), 'CMP'),
           ('CM_PLACER_2', DATATYPES['CM_PLACER_2'], (0, 1), 'CMP'),),
    'CM_PLN': (
           ('CM_PLN_1', DATATYPES['CM_PLN_1'], (0, 1), 'CMP'),
           ('CM_PLN_2', DATATYPES['CM_PLN_2'], (0, 1), 'CMP'),
           ('CM_PLN_3', DATATYPES['CM_PLN_3'], (0, 1), 'CMP'),),
    'CM_POSITION': (
           ('CM_POSITION_1', DATATYPES['CM_POSITION_1'], (0, 1), 'CMP'),
           ('CM_POSITION_2', DATATYPES['CM_POSITION_2'], (0, 1), 'CMP'),
           ('CM_POSITION_3', DATATYPES['CM_POSITION_3'], (0, 1), 'CMP'),),
    'CM_PRACTITIONER': (
           ('CM_PRACTITIONER_1', DATATYPES['CM_PRACTITIONER_1'], (0, 1), 'CMP'),
           ('CM_PRACTITIONER_2', DATATYPES['CM_PRACTITIONER_2'], (0, 1), 'CMP'),),
    'CM_PTA': (
           ('CM_PTA_1', DATATYPES['CM_PTA_1'], (0, 1), 'CMP'),
           ('CM_PTA_2', DATATYPES['CM_PTA_2'], (0, 1), 'CMP'),
           ('CM_PTA_3', DATATYPES['CM_PTA_3'], (0, 1), 'CMP'),),
    'CM_RANGE': (
           ('CM_RANGE_1', DATATYPES['CM_RANGE_1'], (0, 1), 'CMP'),
           ('CM_RANGE_2', DATATYPES['CM_RANGE_2'], (0, 1), 'CMP'),),
    'CM_RFR': (
           ('CM_RFR_1', DATATYPES['CM_RFR_1'], (0, 1), 'CMP'),
           ('CM_RFR_2', DATATYPES['CM_RFR_2'], (0, 1), 'CMP'),
           ('CM_RFR_3', DATATYPES['CM_RFR_3'], (0, 1), 'CMP'),
           ('CM_RFR_4', DATATYPES['CM_RFR_4'], (0, 1), 'CMP'),
           ('CM_RFR_5', DATATYPES['CM_RFR_5'], (0, 1), 'CMP'),
           ('CM_RFR_6', DATATYPES['CM_RFR_6'], (0, 1), 'CMP'),
           ('CM_RFR_7', DATATYPES['CM_RFR_7'], (0, 1), 'CMP'),),
    'CM_RMC': (
           ('CM_RMC_1', DATATYPES['CM_RMC_1'], (0, 1), 'CMP'),
           ('CM_RMC_2', DATATYPES['CM_RMC_2'], (0, 1), 'CMP'),
           ('CM_RMC_3', DATATYPES['CM_RMC_3'], (0, 1), 'CMP'),),
    'CM_SPD': (
           ('CM_SPD_1', DATATYPES['CM_SPD_1'], (0, 1), 'CMP'),
           ('CM_SPD_2', DATATYPES['CM_SPD_2'], (0, 1), 'CMP'),
           ('CM_SPD_3', DATATYPES['CM_SPD_3'], (0, 1), 'CMP'),
           ('CM_SPD_4', DATATYPES['CM_SPD_4'], (0, 1), 'CMP'),),
    'CM_SPS': (
           ('CM_SPS_1', DATATYPES['CM_SPS_1'], (0, 1), 'CMP'),
           ('CM_SPS_2', DATATYPES['CM_SPS_2'], (0, 1), 'CMP'),
           ('CM_SPS_3', DATATYPES['CM_SPS_3'], (0, 1), 'CMP'),
           ('CM_SPS_4', DATATYPES['CM_SPS_4'], (0, 1), 'CMP'),
           ('CM_SPS_5', DATATYPES['CM_SPS_5'], (0, 1), 'CMP'),),
    'CM_UVC': (
           ('CM_UVC_1', DATATYPES['CM_UVC_1'], (0, 1), 'CMP'),
           ('CM_UVC_2', DATATYPES['CM_UVC_2'], (0, 1), 'CMP'),),
    'CM_VR': (
           ('CM_VR_1', DATATYPES['CM_VR_1'], (0, 1), 'CMP'),
           ('CM_VR_2', DATATYPES['CM_VR_2'], (0, 1), 'CMP'),),
    'CQ': (
           ('CQ_1', DATATYPES['CQ_1'], (0, 1), 'CMP'),
           ('CQ_2', DATATYPES['CQ_2'], (0, 1), 'CMP'),),
    'CN': (
           ('CN_1', DATATYPES['CN_1'], (0, 1), 'CMP'),
           ('CN_2', DATATYPES['CN_2'], (0, 1), 'CMP'),
           ('CN_3', DATATYPES['CN_3'], (0, 1), 'CMP'),
           ('CN_4', DATATYPES['CN_4'], (0, 1), 'CMP'),
           ('CN_5', DATATYPES['CN_5'], (0, 1), 'CMP'),
           ('CN_6', DATATYPES['CN_6'], (0, 1), 'CMP'),
           ('CN_7', DATATYPES['CN_7'], (0, 1), 'CMP'),
           ('CN_8', DATATYPES['CN_8'], (0, 1), 'CMP'),),
    'PN': (
           ('PN_1', DATATYPES['PN_1'], (0, 1), 'CMP'),
           ('PN_2', DATATYPES['PN_2'], (0, 1), 'CMP'),
           ('PN_3', DATATYPES['PN_3'], (0, 1), 'CMP'),
           ('PN_4', DATATYPES['PN_4'], (0, 1), 'CMP'),
           ('PN_5', DATATYPES['PN_5'], (0, 1), 'CMP'),
           ('PN_6', DATATYPES['PN_6'], (0, 1), 'CMP'),),
    'RI': (
           ('RI_1', DATATYPES['RI_1'], (0, 1), 'CMP'),
           ('RI_2', DATATYPES['RI_2'], (0, 1), 'CMP'),),
    'TQ': (
           ('TQ_1', DATATYPES['TQ_1'], (0, 1), 'CMP'),
           ('TQ_2', DATATYPES['TQ_2'], (0, 1), 'CMP'),
           ('TQ_3', DATATYPES['TQ_3'], (0, 1), 'CMP'),
           ('TQ_4', DATATYPES['TQ_4'], (0, 1), 'CMP'),
           ('TQ_5', DATATYPES['TQ_5'], (0, 1), 'CMP'),
           ('TQ_6', DATATYPES['TQ_6'], (0, 1), 'CMP'),
           ('TQ_7', DATATYPES['TQ_7'], (0, 1), 'CMP'),
           ('TQ_8', DATATYPES['TQ_8'], (0, 1), 'CMP'),
           ('TQ_9', DATATYPES['TQ_9'], (0, 1), 'CMP'),
           ('TQ_10', DATATYPES['TQ_10'], (0, 1), 'CMP'),),
    'TS': (
           ('TS_1', DATATYPES['TS_1'], (0, 1), 'CMP'),
           ('TS_2', DATATYPES['TS_2'], (0, 1), 'CMP'),),
}

for k, v in iteritems(DATATYPES):
    if v[0] == 'sequence':
        v[1] = DATATYPES_STRUCTS[v[2]]