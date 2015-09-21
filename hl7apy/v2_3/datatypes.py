
DATATYPES = {
    'ABSRANGE_1': ['sequence', None, 'RANGE', 'RANGE', None, -1],
    'ABSRANGE_2': ['leaf', None, 'NM', 'NUMERIC_CHANGE', None, -1],
    'ABSRANGE_3': ['leaf', None, 'NM', 'PERCENT_PER_CHANGE', None, -1],
    'ABSRANGE_4': ['leaf', None, 'NM', 'DAYS', None, -1],
    'AD_1': ['leaf', None, 'ST', 'STREET_ADDRESS', None, -1],
    'AD_2': ['leaf', None, 'ST', 'OTHER_DESIGNATION', None, -1],
    'AD_3': ['leaf', None, 'ST', 'CITY', None, -1],
    'AD_4': ['leaf', None, 'ST', 'STATE_OR_PROVINCE', None, -1],
    'AD_5': ['leaf', None, 'ST', 'ZIP_OR_POSTAL_CODE', None, -1],
    'AD_6': ['leaf', None, 'ID', 'COUNTRY', None, -1],
    'AD_7': ['leaf', None, 'ID', 'ADDRESS_TYPE', None, -1],
    'AD_8': ['leaf', None, 'ST', 'OTHER_GEOGRAPHIC_DESIGNATION', None, -1],
    'AUI_1': ['leaf', None, 'ST', 'AUTHORIZATION_NUMBER', None, -1],
    'AUI_2': ['sequence', None, 'TS', 'DATE', None, -1],
    'AUI_3': ['leaf', None, 'ST', 'SOURCE', None, -1],
    'CCD_1': ['leaf', None, 'ID', 'WHEN_TO_CHARGE_CODE', None, -1],
    'CCD_2': ['sequence', None, 'TS', 'DATE_TIME', None, -1],
    'CD_1': ['sequence', None, 'WVI', 'CHANNEL_IDENTIFIER', None, -1],
    'CD_2': ['sequence', None, 'CM', 'ELECTRODE_NAMES', None, -1],
    'CD_3': ['sequence', None, 'CM', 'CHANNEL_SENSITIVITY_UNITS', None, -1],
    'CD_4': ['sequence', None, 'CM', 'CALIBRATION_PARAMETERS', None, -1],
    'CD_5': ['leaf', None, 'NM', 'SAMPLING_FREQUENCY', None, -1],
    'CD_6': ['sequence', None, 'CM', 'MINIMUM_MAXIMUM_DATA_VALUES', None, -1],
    'CE_1': ['leaf', None, 'ID', 'IDENTIFIER', None, -1],
    'CE_2': ['leaf', None, 'ST', 'TEXT', None, -1],
    'CE_3': ['leaf', None, 'ST', 'NAME_OF_CODING_SYSTEM', None, -1],
    'CE_4': ['leaf', None, 'ID', 'ALTERNATE_IDENTIFIER', None, -1],
    'CE_5': ['leaf', None, 'ST', 'ALTERNATE_TEXT', None, -1],
    'CE_6': ['leaf', None, 'ST', 'NAME_OF_ALTERNATE_CODING_SYSTEM', None, -1],
    'CF_1': ['leaf', None, 'ID', 'IDENTIFIER', None, -1],
    'CF_2': ['leaf', None, 'FT', 'FORMATTED_TEXT', None, -1],
    'CF_3': ['leaf', None, 'ST', 'NAME_OF_CODING_SYSTEM', None, -1],
    'CF_4': ['leaf', None, 'ID', 'ALTERNATE_IDENTIFIER', None, -1],
    'CF_5': ['leaf', None, 'FT', 'ALTERNATE_FORMATTED_TEXT', None, -1],
    'CF_6': ['leaf', None, 'ST', 'NAME_OF_ALTERNATE_CODING_SYSTEM', None, -1],
    'CK_1': ['leaf', None, 'NM', 'ID_NUMBER_NM', None, -1],
    'CK_2': ['leaf', None, 'ST', 'CHECK_DIGIT', None, -1],
    'CK_3': ['leaf', None, 'ID', 'CODE_IDENTIFYING_THE_CHECK_DIGIT_SCHEME_EMPLOYED', None, -1],
    'CK_4': ['sequence', None, 'HD', 'ASSIGNING_AUTHORITY', None, -1],
    'CN_1': ['leaf', None, 'ST', 'ID_NUMBER_ST', None, -1],
    'CN_2': ['leaf', None, 'ST', 'FAMILY_NAME', None, -1],
    'CN_3': ['leaf', None, 'ST', 'GIVEN_NAME', None, -1],
    'CN_4': ['leaf', None, 'ST', 'MIDDLE_INITIAL_OR_NAME', None, -1],
    'CN_5': ['leaf', None, 'ST', 'SUFFIX_E_G_JR_OR_III', None, -1],
    'CN_6': ['leaf', None, 'ST', 'PREFIX_E_G_DR', None, -1],
    'CN_7': ['leaf', None, 'ST', 'DEGREE_E_G_MD', None, -1],
    'CN_8': ['leaf', None, 'ID', 'SOURCE_TABLE', None, -1],
    'CN_9': ['sequence', None, 'HD', 'ASSIGNING_AUTHORITY', None, -1],
    'CP_1': ['sequence', None, 'MO', 'PRICE', None, -1],
    'CP_2': ['leaf', None, 'ID', 'PRICE_TYPE', None, -1],
    'CP_3': ['leaf', None, 'NM', 'FROM_VALUE', None, -1],
    'CP_4': ['leaf', None, 'NM', 'TO_VALUE', None, -1],
    'CP_5': ['sequence', None, 'CE', 'RANGE_UNITS', None, -1],
    'CP_6': ['leaf', None, 'ID', 'RANGE_TYPE', None, -1],
    'CQ_1': ['leaf', None, 'NM', 'QUANTITY', None, -1],
    'CQ_2': ['sequence', None, 'CE', 'UNITS', None, -1],
    'CX_1': ['leaf', None, 'ST', 'ID', None, -1],
    'CX_2': ['leaf', None, 'ST', 'CHECK_DIGIT', None, -1],
    'CX_3': ['leaf', None, 'ID', 'CODE_IDENTIFYING_THE_CHECK_DIGIT_SCHEME_EMPLOYED', None, -1],
    'CX_4': ['sequence', None, 'HD', 'ASSIGNING_AUTHORITY', None, -1],
    'CX_5': ['leaf', None, 'IS', 'IDENTIFIER_TYPE_CODE', 'HL70203', -1],
    'CX_6': ['sequence', None, 'HD', 'ASSIGNING_FACILITY', None, -1],
    'DDI_1': ['leaf', None, 'NM', 'DELAY_DAYS', None, -1],
    'DDI_2': ['leaf', None, 'NM', 'AMOUNT', None, -1],
    'DDI_3': ['leaf', None, 'NM', 'NUMBER_OF_DAYS', None, -1],
    'DIN_1': ['sequence', None, 'TS', 'DATE', None, -1],
    'DIN_2': ['sequence', None, 'CE', 'INSTITUTION_NAME', None, -1],
    'DLD_1': ['leaf', None, 'ID', 'DISCHARGE_LOCATION', None, -1],
    'DLD_2': ['sequence', None, 'TS', 'EFFECTIVE_DATE', None, -1],
    'DLN_1': ['leaf', None, 'ST', 'DRIVER_S_LICENSE_NUMBER', None, -1],
    'DLN_2': ['leaf', None, 'IS', 'ISSUING_STATE_PROVINCE_COUNTRY', None, -1],
    'DLN_3': ['leaf', None, 'DT', 'EXPIRATION_DATE', None, -1],
    'DLT_1': ['sequence', None, 'RANGE', 'RANGE', None, -1],
    'DLT_2': ['leaf', None, 'NM', 'NUMERIC_THRESHOLD', None, -1],
    'DLT_3': ['leaf', None, 'ST', 'CHANGE', None, -1],
    'DLT_4': ['leaf', None, 'NM', 'LENGTH_OF_TIME_DAYS', None, -1],
    'DR_1': ['sequence', None, 'TS', 'RANGE_START_DATE_TIME', None, -1],
    'DR_2': ['sequence', None, 'TS', 'RANGE_END_DATE_TIME', None, -1],
    'DTN_1': ['leaf', None, 'IS', 'DAY_TYPE', None, -1],
    'DTN_2': ['leaf', None, 'NM', 'NUMBER_OF_DAYS', None, -1],
    'ED_1': ['sequence', None, 'HD', 'SOURCE_APPLICATION', None, -1],
    'ED_2': ['leaf', None, 'ID', 'TYPE_OF_DATA', None, -1],
    'ED_3': ['leaf', None, 'ID', 'DATA', None, -1],
    'ED_4': ['leaf', None, 'ID', 'ENCODING', None, -1],
    'ED_5': ['leaf', None, 'ST', 'DATA', None, -1],
    'EI_1': ['leaf', None, 'ST', 'ENTITY_IDENTIFIER', None, -1],
    'EI_2': ['leaf', None, 'IS', 'NAMESPACE_ID', None, -1],
    'EI_3': ['leaf', None, 'ST', 'UNIVERSAL_ID', None, -1],
    'EI_4': ['leaf', None, 'ID', 'UNIVERSAL_ID_TYPE', None, -1],
    'EIP_1': ['sequence', None, 'EI', 'PARENT_S_PLACER_ORDER_NUMBER', None, -1],
    'EIP_2': ['sequence', None, 'EI', 'PARENT_S_FILLER_ORDER_NUMBER', None, -1],
    'ELD_1': ['leaf', None, 'ST', 'SEGMENT_ID', None, -1],
    'ELD_2': ['leaf', None, 'NM', 'SEQUENCE', None, -1],
    'ELD_3': ['leaf', None, 'NM', 'FIELD_POSITION', None, -1],
    'ELD_4': ['sequence', None, 'CE', 'CODE_IDENTIFYING_ERROR', None, -1],
    'FC_1': ['leaf', None, 'IS', 'FINANCIAL_CLASS', None, -1],
    'FC_2': ['sequence', None, 'TS', 'EFFECTIVE_DATE', None, -1],
    'HD_1': ['leaf', None, 'IS', 'NAMESPACE_ID', None, -1],
    'HD_2': ['leaf', None, 'ST', 'UNIVERSAL_ID', None, -1],
    'HD_3': ['leaf', None, 'ID', 'UNIVERSAL_ID_TYPE', None, -1],
    'JCC_1': ['leaf', None, 'IS', 'JOB_CODE', None, -1],
    'JCC_2': ['leaf', None, 'IS', 'JOB_CLASS', None, -1],
    'LA1_1': ['leaf', None, 'ST', 'POINT_OF_CARE_ST', None, -1],
    'LA1_2': ['leaf', None, 'IS', 'ROOM', None, -1],
    'LA1_3': ['leaf', None, 'IS', 'BED', None, -1],
    'LA1_4': ['sequence', None, 'HD', 'FACILITY_HD', None, -1],
    'LA1_5': ['leaf', None, 'IS', 'LOCATION_STATUS', None, -1],
    'LA1_6': ['leaf', None, 'IS', 'PERSON_LOCATION_TYPE', None, -1],
    'LA1_7': ['leaf', None, 'IS', 'BUILDING', None, -1],
    'LA1_8': ['leaf', None, 'ST', 'FLOOR', None, -1],
    'LA1_9': ['leaf', None, 'ST', 'STREET_ADDRESS', None, -1],
    'LA1_10': ['leaf', None, 'ST', 'OTHER_DESIGNATION', None, -1],
    'LA1_11': ['leaf', None, 'ST', 'CITY', None, -1],
    'LA1_12': ['leaf', None, 'ST', 'STATE_OR_PROVINCE', None, -1],
    'LA1_13': ['leaf', None, 'ST', 'ZIP_OR_POSTAL_CODE', None, -1],
    'LA1_14': ['leaf', None, 'ID', 'COUNTRY', None, -1],
    'LA1_15': ['leaf', None, 'ID', 'ADDRESS_TYPE', None, -1],
    'LA1_16': ['leaf', None, 'ST', 'OTHER_GEOGRAPHIC_DESIGNATION', None, -1],
    'MA_1': ['leaf', None, 'NM', 'SAMPLE_1_FROM_CHANNEL_1', None, -1],
    'MA_2': ['leaf', None, 'NM', 'SAMPLE_1_FROM_CHANNEL_2', None, -1],
    'MA_3': ['leaf', None, 'NM', 'SAMPLE_1_FROM_CHANNEL_3', None, -1],
    'MA_4': ['leaf', None, 'NM', 'SAMPLE_2_FROM_CHANNEL_1', None, -1],
    'MA_5': ['leaf', None, 'NM', 'SAMPLE_2_FROM_CHANNEL_2', None, -1],
    'MA_6': ['leaf', None, 'NM', 'SAMPLE_2_FROM_CHANNEL_3', None, -1],
    'MO_1': ['leaf', None, 'NM', 'QUANTITY', None, -1],
    'MO_2': ['leaf', None, 'ID', 'DENOMINATION', None, -1],
    'MOC_1': ['sequence', None, 'MO', 'DOLLAR_AMOUNT', None, -1],
    'MOC_2': ['sequence', None, 'CE', 'CHARGE_CODE', None, -1],
    'MSG_1': ['leaf', None, 'ID', 'MESSAGE_TYPE', None, -1],
    'MSG_2': ['leaf', None, 'ID', 'TRIGGER_EVENT', None, -1],
    'NA_1': ['leaf', None, 'NM', 'VALUE1', None, -1],
    'NA_2': ['leaf', None, 'NM', 'VALUE2', None, -1],
    'NA_3': ['leaf', None, 'NM', 'VALUE3', None, -1],
    'NA_4': ['leaf', None, 'NM', 'VALUE4', None, -1],
    'NDL_1': ['sequence', None, 'CN', 'NAME', None, -1],
    'NDL_2': ['sequence', None, 'TS', 'START_DATE_TIME', None, -1],
    'NDL_3': ['sequence', None, 'TS', 'END_DATE_TIME', None, -1],
    'NDL_4': ['leaf', None, 'IS', 'POINT_OF_CARE_IS', None, -1],
    'NDL_5': ['leaf', None, 'IS', 'ROOM', None, -1],
    'NDL_6': ['leaf', None, 'IS', 'BED', None, -1],
    'NDL_7': ['sequence', None, 'HD', 'FACILITY_HD', None, -1],
    'NDL_8': ['leaf', None, 'IS', 'LOCATION_STATUS', None, -1],
    'NDL_9': ['leaf', None, 'IS', 'PERSON_LOCATION_TYPE', None, -1],
    'NDL_10': ['leaf', None, 'IS', 'BUILDING', None, -1],
    'NDL_11': ['leaf', None, 'ST', 'FLOOR', None, -1],
    'OCD_1': ['sequence', None, 'CE', 'OCCURRENCE_CODE', None, -1],
    'OCD_2': ['leaf', None, 'DT', 'OCCURRENCE_DATE', None, -1],
    'OSP_1': ['sequence', None, 'CE', 'OCCURRENCE_SPAN_CODE', None, -1],
    'OSP_2': ['leaf', None, 'DT', 'OCCURRENCE_SPAN_START_DATE', None, -1],
    'OSP_3': ['leaf', None, 'DT', 'OCCURRENCE_SPAN_STOP_DATE', None, -1],
    'PCF_1': ['leaf', None, 'IS', 'PRE_CERTIFICATION_PATIENT_TYPE', None, -1],
    'PCF_2': ['leaf', None, 'ID', 'PRE_CERTIFICATION_REQUIRED', None, -1],
    'PCF_3': ['sequence', None, 'TS', 'PRE_CERTIFICATION_WINDWOW', None, -1],
    'PEN_1': ['leaf', None, 'IS', 'PENALTY_TYPE', None, -1],
    'PEN_2': ['leaf', None, 'NM', 'PENALTY_AMOUNT', None, -1],
    'PI_1': ['leaf', None, 'ST', 'ID_NUMBER_ST', None, -1],
    'PI_2': ['leaf', None, 'IS', 'TYPE_OF_ID_NUMBER_IS', None, -1],
    'PI_3': ['leaf', None, 'ST', 'OTHER_QUALIFYING_INFO', None, -1],
    'PIP_1': ['sequence', None, 'CE', 'PRIVILEGE', None, -1],
    'PIP_2': ['sequence', None, 'CE', 'PRIVILEGE_CLASS', None, -1],
    'PIP_3': ['leaf', None, 'DT', 'EXPIRATION_DATE', None, -1],
    'PIP_4': ['leaf', None, 'DT', 'ACTIVATION_DATE', None, -1],
    'PL_1': ['leaf', None, 'ID', 'POINT_OF_CARE_ID', None, -1],
    'PL_2': ['leaf', None, 'IS', 'ROOM', None, -1],
    'PL_3': ['leaf', None, 'IS', 'BED', None, -1],
    'PL_4': ['sequence', None, 'HD', 'FACILITY_HD', None, -1],
    'PL_5': ['leaf', None, 'IS', 'LOCATION_STATUS', None, -1],
    'PL_6': ['leaf', None, 'IS', 'PERSON_LOCATION_TYPE', None, -1],
    'PL_7': ['leaf', None, 'IS', 'BUILDING', None, -1],
    'PL_8': ['leaf', None, 'ST', 'FLOOR', None, -1],
    'PL_9': ['leaf', None, 'ST', 'LOCATION_TYPE', None, -1],
    'PLN_1': ['leaf', None, 'ST', 'ID_NUMBER', None, -1],
    'PLN_2': ['leaf', None, 'IS', 'TYPE_OF_ID_NUMBER_IS', None, -1],
    'PLN_3': ['leaf', None, 'ST', 'STATE_OTHER_QUALIFYING_INFO', None, -1],
    'PLN_4': ['leaf', None, 'DT', 'EXPIRATION_DATE', None, -1],
    'PPN_1': ['leaf', None, 'ST', 'ID_NUMBER', None, -1],
    'PPN_2': ['leaf', None, 'ST', 'FAMILY_NAME', None, -1],
    'PPN_3': ['leaf', None, 'ST', 'GIVEN_NAME', None, -1],
    'PPN_4': ['leaf', None, 'ST', 'MIDDLE_INITIAL_OR_NAME', None, -1],
    'PPN_5': ['leaf', None, 'ST', 'SUFFIX_E_G_JR_OR_III', None, -1],
    'PPN_6': ['leaf', None, 'ST', 'PREFIX_E_G_DR', None, -1],
    'PPN_7': ['leaf', None, 'ST', 'DEGREE_E_G_MD', None, -1],
    'PPN_8': ['leaf', None, 'ID', 'SOURCE_TABLE', None, -1],
    'PPN_9': ['sequence', None, 'HD', 'ASSIGNING_AUTHORITY', None, -1],
    'PPN_10': ['leaf', None, 'ID', 'NAME_TYPE_CODE', None, -1],
    'PPN_11': ['leaf', None, 'ST', 'IDENTIFIER_CHECK_DIGIT', None, -1],
    'PPN_12': ['leaf', None, 'ID', 'CODE_IDENTIFYING_THE_CHECK_DIGIT_SCHEME_EMPLOYED', None, -1],
    'PPN_13': ['leaf', None, 'IS', 'IDENTIFIER_TYPE_CODE', None, -1],
    'PPN_14': ['sequence', None, 'HD', 'ASSIGNING_FACILITY', None, -1],
    'PPN_15': ['sequence', None, 'TS', 'DATE_TIME_ACTION_PERFORMED', None, -1],
    'PRL_1': ['sequence', None, 'CE', 'OBX_3_OBSERVATION_IDENTIFIER_OF_PARENT_RESULT', None, -1],
    'PRL_2': ['leaf', None, 'ST', 'OBX_4_SUB_ID_OF_PARENT_RESULT', None, -1],
    'PRL_3': ['leaf', None, 'TX', 'PART_OF_OBX_5_OBSERVATION_RESULT_FROM_PARENT', None, -1],
    'PT_1': ['leaf', None, 'ST', 'PROCESSING_ID', None, -1],
    'PT_2': ['leaf', None, 'ST', 'PROCESSING_MODE', None, -1],
    'PTA_1': ['leaf', None, 'IS', 'POLICY_TYPE', 'HL70147', -1],
    'PTA_2': ['leaf', None, 'IS', 'AMOUNT_CLASS', 'HL70193', -1],
    'PTA_3': ['leaf', None, 'NM', 'AMOUNT', None, -1],
    'QIP_1': ['leaf', None, 'ST', 'FIELD_NAME', None, -1],
    'QIP_2': ['leaf', None, 'ST', 'VALUE1_VALUE2_VALUE3', None, -1],
    'QSC_1': ['leaf', None, 'ST', 'NAME_OF_FIELD', None, -1],
    'QSC_2': ['leaf', None, 'ID', 'RELATIONAL_OPERATOR', None, -1],
    'QSC_3': ['leaf', None, 'ST', 'VALUE', None, -1],
    'QSC_4': ['leaf', None, 'ID', 'RELATIONAL_CONJUNCTION', None, -1],
    'RANGE_1': ['sequence', None, 'CE', 'LOW_VALUE', None, -1],
    'RANGE_2': ['sequence', None, 'CE', 'HIGH_VALUE', None, -1],
    'RCD_1': ['leaf', None, 'ST', 'HL7_ITEM_NUMBER', None, -1],
    'RCD_2': ['leaf', None, 'ST', 'HL7_DATE_TYPE', None, -1],
    'RCD_3': ['leaf', None, 'NM', 'MAXIMUM_COLUMN_WIDTH', None, -1],
    'RFR_1': ['sequence', None, 'RANGE', 'REFERENCE_RANGE', None, -1],
    'RFR_2': ['leaf', None, 'IS', 'SEX', None, -1],
    'RFR_3': ['sequence', None, 'RANGE', 'AGE_RANGE', None, -1],
    'RFR_4': ['sequence', None, 'RANGE', 'AGE_GESTATION', None, -1],
    'RFR_5': ['leaf', None, 'TX', 'SPECIES', None, -1],
    'RFR_6': ['leaf', None, 'ST', 'RACE_SUBSPECIES', None, -1],
    'RFR_7': ['leaf', None, 'TX', 'CONDITIONS', None, -1],
    'RI_1': ['leaf', None, 'IS', 'REPEAT_PATTERN', None, -1],
    'RI_2': ['leaf', None, 'ST', 'EXPLICIT_TIME_INTERVAL', None, -1],
    'RMC_1': ['leaf', None, 'IS', 'ROOM_TYPE', 'HL70145', -1],
    'RMC_2': ['leaf', None, 'IS', 'AMOUNT_TYPE', None, -1],
    'RMC_3': ['leaf', None, 'NM', 'COVERAGE_AMOUNT', 'HL70193', -1],
    'RP_1': ['leaf', None, 'ST', 'POINTER', None, -1],
    'RP_2': ['sequence', None, 'HD', 'APPLICATION_ID', None, -1],
    'RP_3': ['leaf', None, 'ID', 'TYPE_OF_DATA', None, -1],
    'RP_4': ['leaf', None, 'ID', 'SUBTYPE', None, -1],
    'SCV_1': ['leaf', None, 'IS', 'PARAMETER_CLASS', None, -1],
    'SCV_2': ['leaf', None, 'ST', 'PARAMETER_VALUE', None, -1],
    'SN_1': ['leaf', None, 'ST', 'COMPARATOR', None, -1],
    'SN_2': ['leaf', None, 'NM', 'NUM1', None, -1],
    'SN_3': ['leaf', None, 'ST', 'SEPARATOR_OR_SUFFIX', None, -1],
    'SN_4': ['leaf', None, 'NM', 'NUM2', None, -1],
    'SPD_1': ['leaf', None, 'ST', 'SPECIALTY_NAME', None, -1],
    'SPD_2': ['leaf', None, 'ST', 'GOVERNING_BOARD', None, -1],
    'SPD_3': ['leaf', None, 'ID', 'ELIGIBLE_OR_CERTIFIED', None, -1],
    'SPD_4': ['leaf', None, 'DT', 'DATE_OF_CERTIFICATION', None, -1],
    'SPS_1': ['sequence', None, 'CE', 'SPECIMEN_SOURCE_NAME_OR_CODE', None, -1],
    'SPS_2': ['leaf', None, 'TX', 'ADDITIVES', None, -1],
    'SPS_3': ['leaf', None, 'TX', 'FREETEXT', None, -1],
    'SPS_4': ['sequence', None, 'CE', 'BODY_SITE', None, -1],
    'SPS_5': ['sequence', None, 'CE', 'SITE_MODIFIER', None, -1],
    'SPS_6': ['sequence', None, 'CE', 'COLLECTION_MODIFIER_METHOD_CODE', None, -1],
    'TQ_1': ['sequence', None, 'CQ', 'QUANTITY', None, -1],
    'TQ_2': ['sequence', None, 'RI', 'INTERVAL', None, -1],
    'TQ_3': ['leaf', None, 'ST', 'DURATION', None, -1],
    'TQ_4': ['sequence', None, 'TS', 'START_DATE_TIME', None, -1],
    'TQ_5': ['sequence', None, 'TS', 'END_DATE_TIME', None, -1],
    'TQ_6': ['leaf', None, 'ST', 'PRIORITY', None, -1],
    'TQ_7': ['leaf', None, 'ST', 'CONDITION', None, -1],
    'TQ_8': ['leaf', None, 'TX', 'TEXT_TX', None, -1],
    'TQ_9': ['leaf', None, 'ST', 'CONJUNCTION', None, -1],
    'TQ_10': ['sequence', None, 'CM', 'ORDER_SEQUENCING', None, -1],
    'TS_1': ['leaf', None, 'ST', 'TIME_OF_AN_EVENT', None, -1],
    'TS_2': ['leaf', None, 'ST', 'DEGREE_OF_PRECISION', None, -1],
    'UVC_1': ['leaf', None, 'IS', 'VALUE_CODE', None, -1],
    'UVC_2': ['leaf', None, 'NM', 'VALUE_AMOUNT', None, -1],
    'VH_1': ['leaf', None, 'ID', 'START_DAY_RANGE', None, -1],
    'VH_2': ['leaf', None, 'ID', 'END_DAY_RANGE', None, -1],
    'VH_3': ['leaf', None, 'TM', 'START_HOUR_RANGE', None, -1],
    'VH_4': ['leaf', None, 'TM', 'END_HOUR_RANGE', None, -1],
    'VR_1': ['leaf', None, 'ST', 'FIRST_DATA_CODE_VALUE', None, -1],
    'VR_2': ['leaf', None, 'ST', 'LAST_DATA_CODE_CALUE', None, -1],
    'WVI_1': ['leaf', None, 'NM', 'CHANNEL_NUMBER', None, -1],
    'WVI_2': ['leaf', None, 'ST', 'CHANNEL_NAME', None, -1],
    'XAD_1': ['leaf', None, 'ST', 'STREET_ADDRESS', None, -1],
    'XAD_2': ['leaf', None, 'ST', 'OTHER_DESIGNATION', None, -1],
    'XAD_3': ['leaf', None, 'ST', 'CITY', None, -1],
    'XAD_4': ['leaf', None, 'ST', 'STATE_OR_PROVINCE', None, -1],
    'XAD_5': ['leaf', None, 'ST', 'ZIP_OR_POSTAL_CODE', None, -1],
    'XAD_6': ['leaf', None, 'ID', 'COUNTRY', None, -1],
    'XAD_7': ['leaf', None, 'ID', 'ADDRESS_TYPE', None, -1],
    'XAD_8': ['leaf', None, 'ST', 'OTHER_GEOGRAPHIC_DESIGNATION', None, -1],
    'XAD_9': ['leaf', None, 'IS', 'COUNTY_PARISH_CODE', None, -1],
    'XAD_10': ['leaf', None, 'IS', 'CENSUS_TRACT', None, -1],
    'XCN_1': ['leaf', None, 'ST', 'ID_NUMBER_ST', None, -1],
    'XCN_2': ['leaf', None, 'ST', 'FAMILY_NAME', None, -1],
    'XCN_3': ['leaf', None, 'ST', 'GIVEN_NAME', None, -1],
    'XCN_4': ['leaf', None, 'ST', 'MIDDLE_INITIAL_OR_NAME', None, -1],
    'XCN_5': ['leaf', None, 'ST', 'SUFFIX_E_G_JR_OR_III', None, -1],
    'XCN_6': ['leaf', None, 'ST', 'PREFIX_E_G_DR', None, -1],
    'XCN_7': ['leaf', None, 'ST', 'DEGREE_E_G_MD', None, -1],
    'XCN_8': ['leaf', None, 'ID', 'SOURCE_TABLE', None, -1],
    'XCN_9': ['sequence', None, 'HD', 'ASSIGNING_AUTHORITY', None, -1],
    'XCN_10': ['leaf', None, 'ID', 'NAME_TYPE', None, -1],
    'XCN_11': ['leaf', None, 'ST', 'IDENTIFIER_CHECK_DIGIT', None, -1],
    'XCN_12': ['leaf', None, 'ID', 'CODE_IDENTIFYING_THE_CHECK_DIGIT_SCHEME_EMPLOYED', None, -1],
    'XCN_13': ['leaf', None, 'IS', 'IDENTIFIER_TYPE_CODE', None, -1],
    'XCN_14': ['sequence', None, 'HD', 'ASSIGNING_FACILITY_ID', None, -1],
    'XON_1': ['leaf', None, 'ST', 'ORGANIZATION_NAME', None, -1],
    'XON_2': ['leaf', None, 'IS', 'ORGANIZATION_NAME_TYPE_CODE', None, -1],
    'XON_3': ['leaf', None, 'NM', 'ID_NUMBER_NM', None, -1],
    'XON_4': ['leaf', None, 'ST', 'CHECK_DIGIT', None, -1],
    'XON_5': ['leaf', None, 'ID', 'CODE_IDENTIFYING_THE_CHECK_DIGIT_SCHEME_EMPLOYED', None, -1],
    'XON_6': ['sequence', None, 'HD', 'ASSIGNING_AUTHORITY', None, -1],
    'XON_7': ['leaf', None, 'IS', 'IDENTIFIER_TYPE_CODE', None, -1],
    'XON_8': ['sequence', None, 'HD', 'ASSIGNING_FACILITY_ID', None, -1],
    'XPN_1': ['leaf', None, 'ST', 'FAMILY_NAME', None, -1],
    'XPN_2': ['leaf', None, 'ST', 'GIVEN_NAME', None, -1],
    'XPN_3': ['leaf', None, 'ST', 'MIDDLE_INITIAL_OR_NAME', None, -1],
    'XPN_4': ['leaf', None, 'ST', 'SUFFIX_E_G_JR_OR_III', None, -1],
    'XPN_5': ['leaf', None, 'ST', 'PREFIX_E_G_DR', None, -1],
    'XPN_6': ['leaf', None, 'ST', 'DEGREE_E_G_MD', None, -1],
    'XPN_7': ['leaf', None, 'ID', 'NAME_TYPE_CODE', None, -1],
    'XPN_8': ['leaf', None, 'ID', 'NAME_REPRESENTATION_CODE', None, -1],
    'XTN_1': ['leaf', None, 'TN', '999_999_9999_X99999_C_ANY_TEXT', None, -1],
    'XTN_2': ['leaf', None, 'ID', 'TELECOMMUNICATION_USE_CODE', None, -1],
    'XTN_3': ['leaf', None, 'ID', 'TELECOMMUNICATION_EQUIPMENT_TYPE_ID', None, -1],
    'XTN_4': ['leaf', None, 'ST', 'EMAIL_ADDRESS', None, -1],
    'XTN_5': ['leaf', None, 'NM', 'COUNTRY_CODE', None, -1],
    'XTN_6': ['leaf', None, 'NM', 'AREA_CITY_CODE', None, -1],
    'XTN_7': ['leaf', None, 'NM', 'PHONE_NUMBER', None, -1],
    'XTN_8': ['leaf', None, 'NM', 'EXTENSION', None, -1],
    'XTN_9': ['leaf', None, 'ST', 'ANY_TEXT', None, -1],
}


DATATYPES_STRUCTS = {
    'ABSRANGE': (
           ('ABSRANGE_1', DATATYPES['ABSRANGE_1'], (0, 1), 'CMP'),
           ('ABSRANGE_2', DATATYPES['ABSRANGE_2'], (0, 1), 'CMP'),
           ('ABSRANGE_3', DATATYPES['ABSRANGE_3'], (0, 1), 'CMP'),
           ('ABSRANGE_4', DATATYPES['ABSRANGE_4'], (0, 1), 'CMP'),),
    'AD': (
           ('AD_1', DATATYPES['AD_1'], (0, 1), 'CMP'),
           ('AD_2', DATATYPES['AD_2'], (0, 1), 'CMP'),
           ('AD_3', DATATYPES['AD_3'], (0, 1), 'CMP'),
           ('AD_4', DATATYPES['AD_4'], (0, 1), 'CMP'),
           ('AD_5', DATATYPES['AD_5'], (0, 1), 'CMP'),
           ('AD_6', DATATYPES['AD_6'], (0, 1), 'CMP'),
           ('AD_7', DATATYPES['AD_7'], (0, 1), 'CMP'),
           ('AD_8', DATATYPES['AD_8'], (0, 1), 'CMP'),),
    'AUI': (
           ('AUI_1', DATATYPES['AUI_1'], (0, 1), 'CMP'),
           ('AUI_2', DATATYPES['AUI_2'], (0, 1), 'CMP'),
           ('AUI_3', DATATYPES['AUI_3'], (0, 1), 'CMP'),),
    'CCD': (
           ('CCD_1', DATATYPES['CCD_1'], (0, 1), 'CMP'),
           ('CCD_2', DATATYPES['CCD_2'], (0, 1), 'CMP'),),
    'CD': (
           ('CD_1', DATATYPES['CD_1'], (0, 1), 'CMP'),
           ('CD_2', DATATYPES['CD_2'], (0, 1), 'CMP'),
           ('CD_3', DATATYPES['CD_3'], (0, 1), 'CMP'),
           ('CD_4', DATATYPES['CD_4'], (0, 1), 'CMP'),
           ('CD_5', DATATYPES['CD_5'], (0, 1), 'CMP'),
           ('CD_6', DATATYPES['CD_6'], (0, 1), 'CMP'),),
    'CE': (
           ('CE_1', DATATYPES['CE_1'], (0, 1), 'CMP'),
           ('CE_2', DATATYPES['CE_2'], (0, 1), 'CMP'),
           ('CE_3', DATATYPES['CE_3'], (0, 1), 'CMP'),
           ('CE_4', DATATYPES['CE_4'], (0, 1), 'CMP'),
           ('CE_5', DATATYPES['CE_5'], (0, 1), 'CMP'),
           ('CE_6', DATATYPES['CE_6'], (0, 1), 'CMP'),),
    'CF': (
           ('CF_1', DATATYPES['CF_1'], (0, 1), 'CMP'),
           ('CF_2', DATATYPES['CF_2'], (0, 1), 'CMP'),
           ('CF_3', DATATYPES['CF_3'], (0, 1), 'CMP'),
           ('CF_4', DATATYPES['CF_4'], (0, 1), 'CMP'),
           ('CF_5', DATATYPES['CF_5'], (0, 1), 'CMP'),
           ('CF_6', DATATYPES['CF_6'], (0, 1), 'CMP'),),
    'CK': (
           ('CK_1', DATATYPES['CK_1'], (0, 1), 'CMP'),
           ('CK_2', DATATYPES['CK_2'], (0, 1), 'CMP'),
           ('CK_3', DATATYPES['CK_3'], (0, 1), 'CMP'),
           ('CK_4', DATATYPES['CK_4'], (0, 1), 'CMP'),),
    'CN': (
           ('CN_1', DATATYPES['CN_1'], (0, 1), 'CMP'),
           ('CN_2', DATATYPES['CN_2'], (0, 1), 'CMP'),
           ('CN_3', DATATYPES['CN_3'], (0, 1), 'CMP'),
           ('CN_4', DATATYPES['CN_4'], (0, 1), 'CMP'),
           ('CN_5', DATATYPES['CN_5'], (0, 1), 'CMP'),
           ('CN_6', DATATYPES['CN_6'], (0, 1), 'CMP'),
           ('CN_7', DATATYPES['CN_7'], (0, 1), 'CMP'),
           ('CN_8', DATATYPES['CN_8'], (0, 1), 'CMP'),
           ('CN_9', DATATYPES['CN_9'], (0, 1), 'CMP'),),
    'CP': (
           ('CP_1', DATATYPES['CP_1'], (0, 1), 'CMP'),
           ('CP_2', DATATYPES['CP_2'], (0, 1), 'CMP'),
           ('CP_3', DATATYPES['CP_3'], (0, 1), 'CMP'),
           ('CP_4', DATATYPES['CP_4'], (0, 1), 'CMP'),
           ('CP_5', DATATYPES['CP_5'], (0, 1), 'CMP'),
           ('CP_6', DATATYPES['CP_6'], (0, 1), 'CMP'),),
    'CQ': (
           ('CQ_1', DATATYPES['CQ_1'], (0, 1), 'CMP'),
           ('CQ_2', DATATYPES['CQ_2'], (0, 1), 'CMP'),),
    'CX': (
           ('CX_1', DATATYPES['CX_1'], (0, 1), 'CMP'),
           ('CX_2', DATATYPES['CX_2'], (0, 1), 'CMP'),
           ('CX_3', DATATYPES['CX_3'], (0, 1), 'CMP'),
           ('CX_4', DATATYPES['CX_4'], (0, 1), 'CMP'),
           ('CX_5', DATATYPES['CX_5'], (0, 1), 'CMP'),
           ('CX_6', DATATYPES['CX_6'], (0, 1), 'CMP'),),
    'DDI': (
           ('DDI_1', DATATYPES['DDI_1'], (0, 1), 'CMP'),
           ('DDI_2', DATATYPES['DDI_2'], (0, 1), 'CMP'),
           ('DDI_3', DATATYPES['DDI_3'], (0, 1), 'CMP'),),
    'DIN': (
           ('DIN_1', DATATYPES['DIN_1'], (0, 1), 'CMP'),
           ('DIN_2', DATATYPES['DIN_2'], (0, 1), 'CMP'),),
    'DLD': (
           ('DLD_1', DATATYPES['DLD_1'], (0, 1), 'CMP'),
           ('DLD_2', DATATYPES['DLD_2'], (0, 1), 'CMP'),),
    'DLN': (
           ('DLN_1', DATATYPES['DLN_1'], (0, 1), 'CMP'),
           ('DLN_2', DATATYPES['DLN_2'], (0, 1), 'CMP'),
           ('DLN_3', DATATYPES['DLN_3'], (0, 1), 'CMP'),),
    'DLT': (
           ('DLT_1', DATATYPES['DLT_1'], (0, 1), 'CMP'),
           ('DLT_2', DATATYPES['DLT_2'], (0, 1), 'CMP'),
           ('DLT_3', DATATYPES['DLT_3'], (0, 1), 'CMP'),
           ('DLT_4', DATATYPES['DLT_4'], (0, 1), 'CMP'),),
    'DR': (
           ('DR_1', DATATYPES['DR_1'], (0, 1), 'CMP'),
           ('DR_2', DATATYPES['DR_2'], (0, 1), 'CMP'),),
    'DTN': (
           ('DTN_1', DATATYPES['DTN_1'], (0, 1), 'CMP'),
           ('DTN_2', DATATYPES['DTN_2'], (0, 1), 'CMP'),),
    'ED': (
           ('ED_1', DATATYPES['ED_1'], (0, 1), 'CMP'),
           ('ED_2', DATATYPES['ED_2'], (0, 1), 'CMP'),
           ('ED_3', DATATYPES['ED_3'], (0, 1), 'CMP'),
           ('ED_4', DATATYPES['ED_4'], (0, 1), 'CMP'),
           ('ED_5', DATATYPES['ED_5'], (0, 1), 'CMP'),),
    'EI': (
           ('EI_1', DATATYPES['EI_1'], (0, 1), 'CMP'),
           ('EI_2', DATATYPES['EI_2'], (0, 1), 'CMP'),
           ('EI_3', DATATYPES['EI_3'], (0, 1), 'CMP'),
           ('EI_4', DATATYPES['EI_4'], (0, 1), 'CMP'),),
    'EIP': (
           ('EIP_1', DATATYPES['EIP_1'], (0, 1), 'CMP'),
           ('EIP_2', DATATYPES['EIP_2'], (0, 1), 'CMP'),),
    'ELD': (
           ('ELD_1', DATATYPES['ELD_1'], (0, 1), 'CMP'),
           ('ELD_2', DATATYPES['ELD_2'], (0, 1), 'CMP'),
           ('ELD_3', DATATYPES['ELD_3'], (0, 1), 'CMP'),
           ('ELD_4', DATATYPES['ELD_4'], (0, 1), 'CMP'),),
    'FC': (
           ('FC_1', DATATYPES['FC_1'], (0, 1), 'CMP'),
           ('FC_2', DATATYPES['FC_2'], (0, 1), 'CMP'),),
    'HD': (
           ('HD_1', DATATYPES['HD_1'], (0, 1), 'CMP'),
           ('HD_2', DATATYPES['HD_2'], (0, 1), 'CMP'),
           ('HD_3', DATATYPES['HD_3'], (0, 1), 'CMP'),),
    'JCC': (
           ('JCC_1', DATATYPES['JCC_1'], (0, 1), 'CMP'),
           ('JCC_2', DATATYPES['JCC_2'], (0, 1), 'CMP'),),
    'LA1': (
           ('LA1_1', DATATYPES['LA1_1'], (0, 1), 'CMP'),
           ('LA1_2', DATATYPES['LA1_2'], (0, 1), 'CMP'),
           ('LA1_3', DATATYPES['LA1_3'], (0, 1), 'CMP'),
           ('LA1_4', DATATYPES['LA1_4'], (0, 1), 'CMP'),
           ('LA1_5', DATATYPES['LA1_5'], (0, 1), 'CMP'),
           ('LA1_6', DATATYPES['LA1_6'], (0, 1), 'CMP'),
           ('LA1_7', DATATYPES['LA1_7'], (0, 1), 'CMP'),
           ('LA1_8', DATATYPES['LA1_8'], (0, 1), 'CMP'),
           ('LA1_9', DATATYPES['LA1_9'], (0, 1), 'CMP'),
           ('LA1_10', DATATYPES['LA1_10'], (0, 1), 'CMP'),
           ('LA1_11', DATATYPES['LA1_11'], (0, 1), 'CMP'),
           ('LA1_12', DATATYPES['LA1_12'], (0, 1), 'CMP'),
           ('LA1_13', DATATYPES['LA1_13'], (0, 1), 'CMP'),
           ('LA1_14', DATATYPES['LA1_14'], (0, 1), 'CMP'),
           ('LA1_15', DATATYPES['LA1_15'], (0, 1), 'CMP'),
           ('LA1_16', DATATYPES['LA1_16'], (0, 1), 'CMP'),),
    'MA': (
           ('MA_1', DATATYPES['MA_1'], (0, 1), 'CMP'),
           ('MA_2', DATATYPES['MA_2'], (0, 1), 'CMP'),
           ('MA_3', DATATYPES['MA_3'], (0, 1), 'CMP'),
           ('MA_4', DATATYPES['MA_4'], (0, 1), 'CMP'),
           ('MA_5', DATATYPES['MA_5'], (0, 1), 'CMP'),
           ('MA_6', DATATYPES['MA_6'], (0, 1), 'CMP'),),
    'MO': (
           ('MO_1', DATATYPES['MO_1'], (0, 1), 'CMP'),
           ('MO_2', DATATYPES['MO_2'], (0, 1), 'CMP'),),
    'MOC': (
           ('MOC_1', DATATYPES['MOC_1'], (0, 1), 'CMP'),
           ('MOC_2', DATATYPES['MOC_2'], (0, 1), 'CMP'),),
    'MSG': (
           ('MSG_1', DATATYPES['MSG_1'], (0, 1), 'CMP'),
           ('MSG_2', DATATYPES['MSG_2'], (0, 1), 'CMP'),),
    'NA': (
           ('NA_1', DATATYPES['NA_1'], (0, 1), 'CMP'),
           ('NA_2', DATATYPES['NA_2'], (0, 1), 'CMP'),
           ('NA_3', DATATYPES['NA_3'], (0, 1), 'CMP'),
           ('NA_4', DATATYPES['NA_4'], (0, 1), 'CMP'),),
    'NDL': (
           ('NDL_1', DATATYPES['NDL_1'], (0, 1), 'CMP'),
           ('NDL_2', DATATYPES['NDL_2'], (0, 1), 'CMP'),
           ('NDL_3', DATATYPES['NDL_3'], (0, 1), 'CMP'),
           ('NDL_4', DATATYPES['NDL_4'], (0, 1), 'CMP'),
           ('NDL_5', DATATYPES['NDL_5'], (0, 1), 'CMP'),
           ('NDL_6', DATATYPES['NDL_6'], (0, 1), 'CMP'),
           ('NDL_7', DATATYPES['NDL_7'], (0, 1), 'CMP'),
           ('NDL_8', DATATYPES['NDL_8'], (0, 1), 'CMP'),
           ('NDL_9', DATATYPES['NDL_9'], (0, 1), 'CMP'),
           ('NDL_10', DATATYPES['NDL_10'], (0, 1), 'CMP'),
           ('NDL_11', DATATYPES['NDL_11'], (0, 1), 'CMP'),),
    'OCD': (
           ('OCD_1', DATATYPES['OCD_1'], (0, 1), 'CMP'),
           ('OCD_2', DATATYPES['OCD_2'], (0, 1), 'CMP'),),
    'OSP': (
           ('OSP_1', DATATYPES['OSP_1'], (0, 1), 'CMP'),
           ('OSP_2', DATATYPES['OSP_2'], (0, 1), 'CMP'),
           ('OSP_3', DATATYPES['OSP_3'], (0, 1), 'CMP'),),
    'PCF': (
           ('PCF_1', DATATYPES['PCF_1'], (0, 1), 'CMP'),
           ('PCF_2', DATATYPES['PCF_2'], (0, 1), 'CMP'),
           ('PCF_3', DATATYPES['PCF_3'], (0, 1), 'CMP'),),
    'PEN': (
           ('PEN_1', DATATYPES['PEN_1'], (0, 1), 'CMP'),
           ('PEN_2', DATATYPES['PEN_2'], (0, 1), 'CMP'),),
    'PI': (
           ('PI_1', DATATYPES['PI_1'], (0, 1), 'CMP'),
           ('PI_2', DATATYPES['PI_2'], (0, 1), 'CMP'),
           ('PI_3', DATATYPES['PI_3'], (0, 1), 'CMP'),),
    'PIP': (
           ('PIP_1', DATATYPES['PIP_1'], (0, 1), 'CMP'),
           ('PIP_2', DATATYPES['PIP_2'], (0, 1), 'CMP'),
           ('PIP_3', DATATYPES['PIP_3'], (0, 1), 'CMP'),
           ('PIP_4', DATATYPES['PIP_4'], (0, 1), 'CMP'),),
    'PL': (
           ('PL_1', DATATYPES['PL_1'], (0, 1), 'CMP'),
           ('PL_2', DATATYPES['PL_2'], (0, 1), 'CMP'),
           ('PL_3', DATATYPES['PL_3'], (0, 1), 'CMP'),
           ('PL_4', DATATYPES['PL_4'], (0, 1), 'CMP'),
           ('PL_5', DATATYPES['PL_5'], (0, 1), 'CMP'),
           ('PL_6', DATATYPES['PL_6'], (0, 1), 'CMP'),
           ('PL_7', DATATYPES['PL_7'], (0, 1), 'CMP'),
           ('PL_8', DATATYPES['PL_8'], (0, 1), 'CMP'),
           ('PL_9', DATATYPES['PL_9'], (0, 1), 'CMP'),),
    'PLN': (
           ('PLN_1', DATATYPES['PLN_1'], (0, 1), 'CMP'),
           ('PLN_2', DATATYPES['PLN_2'], (0, 1), 'CMP'),
           ('PLN_3', DATATYPES['PLN_3'], (0, 1), 'CMP'),
           ('PLN_4', DATATYPES['PLN_4'], (0, 1), 'CMP'),),
    'PPN': (
           ('PPN_1', DATATYPES['PPN_1'], (0, 1), 'CMP'),
           ('PPN_2', DATATYPES['PPN_2'], (0, 1), 'CMP'),
           ('PPN_3', DATATYPES['PPN_3'], (0, 1), 'CMP'),
           ('PPN_4', DATATYPES['PPN_4'], (0, 1), 'CMP'),
           ('PPN_5', DATATYPES['PPN_5'], (0, 1), 'CMP'),
           ('PPN_6', DATATYPES['PPN_6'], (0, 1), 'CMP'),
           ('PPN_7', DATATYPES['PPN_7'], (0, 1), 'CMP'),
           ('PPN_8', DATATYPES['PPN_8'], (0, 1), 'CMP'),
           ('PPN_9', DATATYPES['PPN_9'], (0, 1), 'CMP'),
           ('PPN_10', DATATYPES['PPN_10'], (0, 1), 'CMP'),
           ('PPN_11', DATATYPES['PPN_11'], (0, 1), 'CMP'),
           ('PPN_12', DATATYPES['PPN_12'], (0, 1), 'CMP'),
           ('PPN_13', DATATYPES['PPN_13'], (0, 1), 'CMP'),
           ('PPN_14', DATATYPES['PPN_14'], (0, 1), 'CMP'),
           ('PPN_15', DATATYPES['PPN_15'], (0, 1), 'CMP'),),
    'PRL': (
           ('PRL_1', DATATYPES['PRL_1'], (0, 1), 'CMP'),
           ('PRL_2', DATATYPES['PRL_2'], (0, 1), 'CMP'),
           ('PRL_3', DATATYPES['PRL_3'], (0, 1), 'CMP'),),
    'PT': (
           ('PT_1', DATATYPES['PT_1'], (0, 1), 'CMP'),
           ('PT_2', DATATYPES['PT_2'], (0, 1), 'CMP'),),
    'PTA': (
           ('PTA_1', DATATYPES['PTA_1'], (0, 1), 'CMP'),
           ('PTA_2', DATATYPES['PTA_2'], (0, 1), 'CMP'),
           ('PTA_3', DATATYPES['PTA_3'], (0, 1), 'CMP'),),
    'QIP': (
           ('QIP_1', DATATYPES['QIP_1'], (0, 1), 'CMP'),
           ('QIP_2', DATATYPES['QIP_2'], (0, 1), 'CMP'),),
    'QSC': (
           ('QSC_1', DATATYPES['QSC_1'], (0, 1), 'CMP'),
           ('QSC_2', DATATYPES['QSC_2'], (0, 1), 'CMP'),
           ('QSC_3', DATATYPES['QSC_3'], (0, 1), 'CMP'),
           ('QSC_4', DATATYPES['QSC_4'], (0, 1), 'CMP'),),
    'RANGE': (
           ('RANGE_1', DATATYPES['RANGE_1'], (0, 1), 'CMP'),
           ('RANGE_2', DATATYPES['RANGE_2'], (0, 1), 'CMP'),),
    'RCD': (
           ('RCD_1', DATATYPES['RCD_1'], (0, 1), 'CMP'),
           ('RCD_2', DATATYPES['RCD_2'], (0, 1), 'CMP'),
           ('RCD_3', DATATYPES['RCD_3'], (0, 1), 'CMP'),),
    'RFR': (
           ('RFR_1', DATATYPES['RFR_1'], (0, 1), 'CMP'),
           ('RFR_2', DATATYPES['RFR_2'], (0, 1), 'CMP'),
           ('RFR_3', DATATYPES['RFR_3'], (0, 1), 'CMP'),
           ('RFR_4', DATATYPES['RFR_4'], (0, 1), 'CMP'),
           ('RFR_5', DATATYPES['RFR_5'], (0, 1), 'CMP'),
           ('RFR_6', DATATYPES['RFR_6'], (0, 1), 'CMP'),
           ('RFR_7', DATATYPES['RFR_7'], (0, 1), 'CMP'),),
    'RI': (
           ('RI_1', DATATYPES['RI_1'], (0, 1), 'CMP'),
           ('RI_2', DATATYPES['RI_2'], (0, 1), 'CMP'),),
    'RMC': (
           ('RMC_1', DATATYPES['RMC_1'], (0, 1), 'CMP'),
           ('RMC_2', DATATYPES['RMC_2'], (0, 1), 'CMP'),
           ('RMC_3', DATATYPES['RMC_3'], (0, 1), 'CMP'),),
    'RP': (
           ('RP_1', DATATYPES['RP_1'], (0, 1), 'CMP'),
           ('RP_2', DATATYPES['RP_2'], (0, 1), 'CMP'),
           ('RP_3', DATATYPES['RP_3'], (0, 1), 'CMP'),
           ('RP_4', DATATYPES['RP_4'], (0, 1), 'CMP'),),
    'SCV': (
           ('SCV_1', DATATYPES['SCV_1'], (0, 1), 'CMP'),
           ('SCV_2', DATATYPES['SCV_2'], (0, 1), 'CMP'),),
    'SN': (
           ('SN_1', DATATYPES['SN_1'], (0, 1), 'CMP'),
           ('SN_2', DATATYPES['SN_2'], (0, 1), 'CMP'),
           ('SN_3', DATATYPES['SN_3'], (0, 1), 'CMP'),
           ('SN_4', DATATYPES['SN_4'], (0, 1), 'CMP'),),
    'SPD': (
           ('SPD_1', DATATYPES['SPD_1'], (0, 1), 'CMP'),
           ('SPD_2', DATATYPES['SPD_2'], (0, 1), 'CMP'),
           ('SPD_3', DATATYPES['SPD_3'], (0, 1), 'CMP'),
           ('SPD_4', DATATYPES['SPD_4'], (0, 1), 'CMP'),),
    'SPS': (
           ('SPS_1', DATATYPES['SPS_1'], (0, 1), 'CMP'),
           ('SPS_2', DATATYPES['SPS_2'], (0, 1), 'CMP'),
           ('SPS_3', DATATYPES['SPS_3'], (0, 1), 'CMP'),
           ('SPS_4', DATATYPES['SPS_4'], (0, 1), 'CMP'),
           ('SPS_5', DATATYPES['SPS_5'], (0, 1), 'CMP'),
           ('SPS_6', DATATYPES['SPS_6'], (0, 1), 'CMP'),),
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
    'UVC': (
           ('UVC_1', DATATYPES['UVC_1'], (0, 1), 'CMP'),
           ('UVC_2', DATATYPES['UVC_2'], (0, 1), 'CMP'),),
    'VH': (
           ('VH_1', DATATYPES['VH_1'], (0, 1), 'CMP'),
           ('VH_2', DATATYPES['VH_2'], (0, 1), 'CMP'),
           ('VH_3', DATATYPES['VH_3'], (0, 1), 'CMP'),
           ('VH_4', DATATYPES['VH_4'], (0, 1), 'CMP'),),
    'VR': (
           ('VR_1', DATATYPES['VR_1'], (0, 1), 'CMP'),
           ('VR_2', DATATYPES['VR_2'], (0, 1), 'CMP'),),
    'WVI': (
           ('WVI_1', DATATYPES['WVI_1'], (0, 1), 'CMP'),
           ('WVI_2', DATATYPES['WVI_2'], (0, 1), 'CMP'),),
    'XAD': (
           ('XAD_1', DATATYPES['XAD_1'], (0, 1), 'CMP'),
           ('XAD_2', DATATYPES['XAD_2'], (0, 1), 'CMP'),
           ('XAD_3', DATATYPES['XAD_3'], (0, 1), 'CMP'),
           ('XAD_4', DATATYPES['XAD_4'], (0, 1), 'CMP'),
           ('XAD_5', DATATYPES['XAD_5'], (0, 1), 'CMP'),
           ('XAD_6', DATATYPES['XAD_6'], (0, 1), 'CMP'),
           ('XAD_7', DATATYPES['XAD_7'], (0, 1), 'CMP'),
           ('XAD_8', DATATYPES['XAD_8'], (0, 1), 'CMP'),
           ('XAD_9', DATATYPES['XAD_9'], (0, 1), 'CMP'),
           ('XAD_10', DATATYPES['XAD_10'], (0, 1), 'CMP'),),
    'XCN': (
           ('XCN_1', DATATYPES['XCN_1'], (0, 1), 'CMP'),
           ('XCN_2', DATATYPES['XCN_2'], (0, 1), 'CMP'),
           ('XCN_3', DATATYPES['XCN_3'], (0, 1), 'CMP'),
           ('XCN_4', DATATYPES['XCN_4'], (0, 1), 'CMP'),
           ('XCN_5', DATATYPES['XCN_5'], (0, 1), 'CMP'),
           ('XCN_6', DATATYPES['XCN_6'], (0, 1), 'CMP'),
           ('XCN_7', DATATYPES['XCN_7'], (0, 1), 'CMP'),
           ('XCN_8', DATATYPES['XCN_8'], (0, 1), 'CMP'),
           ('XCN_9', DATATYPES['XCN_9'], (0, 1), 'CMP'),
           ('XCN_10', DATATYPES['XCN_10'], (0, 1), 'CMP'),
           ('XCN_11', DATATYPES['XCN_11'], (0, 1), 'CMP'),
           ('XCN_12', DATATYPES['XCN_12'], (0, 1), 'CMP'),
           ('XCN_13', DATATYPES['XCN_13'], (0, 1), 'CMP'),
           ('XCN_14', DATATYPES['XCN_14'], (0, 1), 'CMP'),),
    'XON': (
           ('XON_1', DATATYPES['XON_1'], (0, 1), 'CMP'),
           ('XON_2', DATATYPES['XON_2'], (0, 1), 'CMP'),
           ('XON_3', DATATYPES['XON_3'], (0, 1), 'CMP'),
           ('XON_4', DATATYPES['XON_4'], (0, 1), 'CMP'),
           ('XON_5', DATATYPES['XON_5'], (0, 1), 'CMP'),
           ('XON_6', DATATYPES['XON_6'], (0, 1), 'CMP'),
           ('XON_7', DATATYPES['XON_7'], (0, 1), 'CMP'),
           ('XON_8', DATATYPES['XON_8'], (0, 1), 'CMP'),),
    'XPN': (
           ('XPN_1', DATATYPES['XPN_1'], (0, 1), 'CMP'),
           ('XPN_2', DATATYPES['XPN_2'], (0, 1), 'CMP'),
           ('XPN_3', DATATYPES['XPN_3'], (0, 1), 'CMP'),
           ('XPN_4', DATATYPES['XPN_4'], (0, 1), 'CMP'),
           ('XPN_5', DATATYPES['XPN_5'], (0, 1), 'CMP'),
           ('XPN_6', DATATYPES['XPN_6'], (0, 1), 'CMP'),
           ('XPN_7', DATATYPES['XPN_7'], (0, 1), 'CMP'),
           ('XPN_8', DATATYPES['XPN_8'], (0, 1), 'CMP'),),
    'XTN': (
           ('XTN_1', DATATYPES['XTN_1'], (0, 1), 'CMP'),
           ('XTN_2', DATATYPES['XTN_2'], (0, 1), 'CMP'),
           ('XTN_3', DATATYPES['XTN_3'], (0, 1), 'CMP'),
           ('XTN_4', DATATYPES['XTN_4'], (0, 1), 'CMP'),
           ('XTN_5', DATATYPES['XTN_5'], (0, 1), 'CMP'),
           ('XTN_6', DATATYPES['XTN_6'], (0, 1), 'CMP'),
           ('XTN_7', DATATYPES['XTN_7'], (0, 1), 'CMP'),
           ('XTN_8', DATATYPES['XTN_8'], (0, 1), 'CMP'),
           ('XTN_9', DATATYPES['XTN_9'], (0, 1), 'CMP'),),
}

for k, v in DATATYPES.iteritems():
    if v[0] == 'sequence':
        v[1] = DATATYPES_STRUCTS[v[2]]