"""Medical Records Validator Project (freeCodeCamp)

This project handles:
 - Validation of patient medical record input
 - Verification of data types and format constraints using rules and regex
 - Detection and reporting of invalid or inconsistent records with error details
"""

import re

def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    """Validate and identify invalid entries in the patient's medical record.
    Args:
        patient_id (str): Patient ID.
        age (int): Patient's age.
        gender (str): Patient's gender.
        diagnosis (str): Patient's diagnosed condition.
        medications (list): List of prescribed medications.
        last_visit_id (str): Patient's last visit ID.
    Returns:
        list: Keys of all invalid records.
    """

    # Each record must abide by the following rules:
    # patient_id (str) should start with 'p' or 'P' followed by some number
    # age (int) should be greater than or equal to 18
    # gender (str) should be either male or female
    # diagnosis (str or None)
    # each element of medications (list) should be a string
    # last_visit_id (str) should start with 'v' followed by some number
    constraints = {
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18,
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
    }
    # return the keys of all invalid records
    return [key for key, value in constraints.items() if not value]
    
def validate(data):
    """Validates a sequence of medical records.
    Args:
        data (list or tuple): A sequence of medical records for validation
    Returns:
        bool: Whether the input was valid or not
    """

    # Acquired data must be a sequence of each patient's medical record.
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple of records.")
        return False
            
    is_invalid = False
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    # Loop through each patient record with its index
    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: Expected patient record {index + 1} to be a dictionary.")
            print("Input Received: ", dictionary)
            is_invalid = True
            continue

        # Check if record has all required fields
        input_keys = set(dictionary.keys())
        if input_keys != key_set:
            print(f"Invalid format: Patient record {index + 1} has missing and/or invalid keys.")
            print(f"Unexpected keys found: {input_keys - key_set}")
            print(f"Missing fields: {key_set - input_keys}")
            is_invalid = True
            continue

        # Find invalid fields in each record
        invalid_records = find_invalid_records(**dictionary)
        for key in invalid_records:
            print(f"Unexpected format '{key}: {dictionary[key]}' in patient record {index + 1}.")
            is_invalid = True

    if is_invalid:
        return False
        
    # All records are valid
    print("All records are valid.")
    return True

def main():    
    medical_records = [
        {
            'patient_id': 'P1001',
            'age': 34,
            'gender': 'Female',
            'diagnosis': 'Hypertension',
            'medications': ['Lisinopril'],
            'last_visit_id': 'V2301',
        },
        {
            'patient_id': 'p1002',
            'age': 47,
            'gender': 'male',
            'diagnosis': 'Type 2 Diabetes',
            'medications': ['Metformin', 'Insulin'],
            'last_visit_id': 'v2302',
        },
        {
            'patient_id': 'P1003',
            'age': 29,
            'gender': 'female',
            'diagnosis': 'Asthma',
            'medications': ['Albuterol'],
            'last_visit_id': 'v2303',
        },
        {
            'patient_id': 'p1004',
            'age': 56,
            'gender': 'Male',
            'diagnosis': 'Chronic Back Pain',
            'medications': ['Ibuprofen', 'Physical Therapy'],
            'last_visit_id': 'V2304',
        }
    ]
    
    validate(medical_records)

if __name__ == "__main__":
    main()