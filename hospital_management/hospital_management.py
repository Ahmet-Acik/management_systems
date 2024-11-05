"""
Hospital Management System

This module uses lists, sets, tuples, and dictionaries to manage hospital data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

Data Structures:

1. Lists: To store collections of patients, doctors, and appointments.
2. Tuples: To store immutable patient and doctor details.
3. Sets: To manage unique specialties and departments.
4. Dictionaries: To map patient IDs and doctor IDs to their details and manage appointments.

List of patients with details (Patient ID, Name, Age, Gender, Medical History):
patients = [
    (1, "Alice", 30, "Female", {"Diabetes", "Hypertension"}),
    (2, "Bob", 45, "Male", {"Asthma"}),
    (3, "Charlie", 25, "Male", {"Allergy"}),
    (4, "Diana", 35, "Female", {"Thyroid"}),
    (5, "Eve", 50, "Female", {"Arthritis"})
]

List of doctors with details (Doctor ID, Name, Age, Specialty, Department):
doctors = [
    (101, "Dr. Smith", 50, "Cardiology", "Cardiology"),
    (102, "Dr. Johnson", 40, "Neurology", "Neurology"),
    (103, "Dr. Brown", 45, "Orthopedics", "Orthopedics"),
    (104, "Dr. White", 35, "Pediatrics", "Pediatrics"),
    (105, "Dr. Green", 55, "General Medicine", "General Medicine")
]

List of appointments (Appointment ID, Patient ID, Doctor ID, Date, Time):
appointments = [
    (201, 1, 101, "2023-10-01", "10:00 AM"),
    (202, 2, 102, "2023-10-02", "11:00 AM"),
    (203, 3, 103, "2023-10-03", "12:00 PM"),
    (204, 4, 104, "2023-10-04", "01:00 PM"),
    (205, 5, 105, "2023-10-05", "02:00 PM")
]

Set of unique specialties:
specialties = set()

Adding specialties from doctors:
for doctor in doctors:
    specialties.add(doctor[3])

Set of unique departments:
departments = set()

Adding departments from doctors:
for doctor in doctors:
    departments.add(doctor[4])

Dictionary to map patient IDs to their details:
patient_catalog = {patient[0]: patient for patient in patients}

Dictionary to map doctor IDs to their details:
doctor_catalog = {doctor[0]: doctor for doctor in doctors}

Dictionary to manage appointments:
appointment_schedule = {appointment[0]: appointment for appointment in appointments}

Functions:

List-Related Methods:
1. find_patient_index(patient_id): Finds the index of a patient in the list.
2. find_doctor_index(doctor_id): Finds the index of a doctor in the list.
3. sort_patients_by_age(): Sorts patients by age.
4. sort_doctors_by_age(): Sorts doctors by age.
5. reverse_appointments(): Reverses the list of appointments.
6. append_appointment(appointment): Appends a new appointment to the list.
7. remove_appointment(appointment_id): Removes an appointment from the list.

Tuple-Related Methods:
1. find_max_min_age_patients(): Finds the maximum and minimum age of patients.
2. find_max_min_age_doctors(): Finds the maximum and minimum age of doctors.
3. count_medical_history_occurrences(condition): Counts the occurrences of a specific medical condition.

Set-Related Methods:
1. add_specialty(specialty): Adds a new specialty.
2. remove_specialty(specialty): Removes a specialty.
3. list_all_specialties(): Lists all specialties.
4. add_department(department): Adds a new department.
5. remove_department(department): Removes a department.
6. list_all_departments(): Lists all departments.
7. find_common_specialties(other_specialties): Finds common specialties between two sets.
8. find_unique_specialties(): Finds unique specialties in the hospital.
9. clear_specialties(): Clears all specialties.

Dictionary-Related Methods:
1. add_patient(patient_id, name, age, gender, medical_history): Adds a new patient to the hospital.
2. remove_patient(patient_id): Removes a patient from the hospital.
3. get_patient_details(patient_id): Gets patient details.
4. list_patients_by_gender(gender): Lists all patients by gender.
5. count_patients_by_gender(gender): Counts patients by gender.
6. add_doctor(doctor_id, name, age, specialty, department): Adds a new doctor to the hospital.
7. remove_doctor(doctor_id): Removes a doctor from the hospital.
8. get_doctor_details(doctor_id): Gets doctor details.
9. list_doctors_by_department(department): Lists all doctors by department.
10. count_doctors_by_department(department): Counts doctors by department.
11. update_patient_details(patient_id, new_details): Updates patient details.
12. update_doctor_details(doctor_id, new_details): Updates doctor details.
13. merge_patient_catalogs(other_catalog): Merges two patient catalogs.
14. merge_doctor_catalogs(other_catalog): Merges two doctor catalogs.
15. get_all_patient_ids(): Gets all patient IDs.
16. get_all_doctor_ids(): Gets all doctor IDs.
17. clear_patient_catalog(): Clears the patient catalog.
18. clear_doctor_catalog(): Clears the doctor catalog.

Example usage:
if __name__ == "__main__":
    print("Patient Catalog:")
    for patient_id, details in patient_catalog.items():
        print(f"{patient_id}: {details}")

    print("\nDoctor Catalog:")
    for doctor_id, details in doctor_catalog.items():
        print(f"{doctor_id}: {details}")

    print("\nSpecialties Available:")
    print(specialties)

    print("\nDepartments Available:")
    print(departments)

    print("\nAppointment Schedule:")
    for appointment_id, details in appointment_schedule.items():
        print(f"Appointment ID {appointment_id}: {details}")

    # Add and remove patients
    add_patient(6, "Frank", 60, "Male", {"Diabetes"})
    remove_patient(3)

    print("\nPatient Catalog After Changes:")
    for patient_id, details in patient_catalog.items():
        print(f"{patient_id}: {details}")

    # Get patient details
    print("\nPatient Details for ID 2:")
    print(get_patient_details(2))

    # List patients by gender
    print("\nMale Patients:")
    print(list_patients_by_gender("Male"))

    # Count patients by gender
    print("\nCount of Female Patients:")
    print(count_patients_by_gender("Female"))

    # Find patient index
    print("\nIndex of Patient ID 2:")
    print(find_patient_index(2))

    # Add and remove specialties
    add_specialty("Dermatology")
    remove_specialty("Orthopedics")

    # List all specialties
    print("\nAll Specialties:")
    print(list_all_specialties())

    # Add and remove departments
    add_department("Dermatology")
    remove_department("Orthopedics")

    # List all departments
    print("\nAll Departments:")
    print(list_all_departments())

    # Append and remove appointments
    append_appointment((206, 1, 101, "2023-10-06", "03:00 PM"))
    remove_appointment(202)

    print("\nAppointments After Changes:")
    for appointment in appointments:
        print(appointment)

    # Sort patients by age
    print("\nPatients Sorted by Age:")
    for patient in sort_patients_by_age():
        print(patient)

    # Sort doctors by age
    print("\nDoctors Sorted by Age:")
    for doctor in sort_doctors_by_age():
        print(doctor)

    # Reverse the list of appointments
    print("\nReversed List of Appointments:")
    print(reverse_appointments())

    # Find the maximum and minimum age of patients
    max_age_patients, min_age_patients = find_max_min_age_patients()
    print(f"\nMaximum Age of Patients: {max_age_patients}, Minimum Age of Patients: {min_age_patients}")

    # Find the maximum and minimum age of doctors
    max_age_doctors, min_age_doctors = find_max_min_age_doctors()
    print(f"\nMaximum Age of Doctors: {max_age_doctors}, Minimum Age of Doctors: {min_age_doctors}")

    # Count the occurrences of a specific medical condition
    print(f"\nOccurrences of 'Diabetes': {count_medical_history_occurrences('Diabetes')}")

    # Find common specialties between two sets
    other_specialties = {"Cardiology", "Dermatology", "Neurology"}
    print(f"\nCommon Specialties: {find_common_specialties(other_specialties)}")

    # Find unique specialties in the hospital
    print(f"\nUnique Specialties: {find_unique_specialties()}")

    # Update patient details
    update_patient_details(2, (2, "Bob", 46, "Male", {"Asthma", "Diabetes"}))
    print(f"\nUpdated Patient Details for ID 2: {get_patient_details(2)}")

    # Update doctor details
    update_doctor_details(102, (102, "Dr. Johnson", 41, "Neurology", "Neurology"))
    print(f"\nUpdated Doctor Details for ID 102: {get_doctor_details(102)}")

    # Merge two patient catalogs
    other_patient_catalog = {
        7: (7, "Grace", 40, "Female", {"Hypertension"}),
        8: (8, "Hank", 55, "Male", {"Arthritis"})
    }
    merge_patient_catalogs(other_patient_catalog)
    print("\nMerged Patient Catalog:")
    for patient_id, details in patient_catalog.items():
        print(f"{patient_id}: {details}")

    # Merge two doctor catalogs
    other_doctor_catalog = {
        106: (106, "Dr. Blue", 60, "Dermatology", "Dermatology"),
        107: (107, "Dr. Red", 50, "Neurology", "Neurology")
    }
    merge_doctor_catalogs(other_doctor_catalog)
    print("\nMerged Doctor Catalog:")
    for doctor_id, details in doctor_catalog.items():
        print(f"{doctor_id}: {details}")

    # Get all patient IDs
    print("\nAll Patient IDs:")
    print(get_all_patient_ids())

    # Get all doctor IDs
    print("\nAll Doctor IDs:")
    print(get_all_doctor_ids())

    # Clear the patient catalog
    clear_patient_catalog()
    print("\nPatient Catalog After Clearing:")
    print(patient_catalog)

    # Clear the doctor catalog
    clear_doctor_catalog()
    print("\nDoctor Catalog After Clearing:")
    print(doctor_catalog)
"""
# hospital_management.py

class HospitalManagement:
    """
    Hospital Management System

    This module uses lists, sets, tuples, and dictionaries to manage hospital data. It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

    Data Structures:

    1. Lists: To store collections of patients, doctors, and appointments.
    2. Tuples: To store immutable patient and doctor details.
    3. Sets: To manage unique specialties and departments.
    4. Dictionaries: To map patient IDs and doctor IDs to their details and manage appointments.
    """

    def __init__(self):
        # List of patients with details (Patient ID, Name, Age, Gender, Medical History)
        self.patients = [
            (1, "Alice", 30, "Female", {"Diabetes", "Hypertension"}),
            (2, "Bob", 45, "Male", {"Asthma"}),
            (3, "Charlie", 25, "Male", {"Allergy"}),
            (4, "Diana", 35, "Female", {"Thyroid"}),
            (5, "Eve", 50, "Female", {"Arthritis"})
        ]

        # List of doctors with details (Doctor ID, Name, Age, Specialty, Department)
        self.doctors = [
            (101, "Dr. Smith", 50, "Cardiology", "Cardiology"),
            (102, "Dr. Johnson", 40, "Neurology", "Neurology"),
            (103, "Dr. Brown", 45, "Orthopedics", "Orthopedics"),
            (104, "Dr. White", 35, "Pediatrics", "Pediatrics"),
            (105, "Dr. Green", 55, "General Medicine", "General Medicine")
        ]

        # List of appointments (Appointment ID, Patient ID, Doctor ID, Date, Time)
        self.appointments = [
            (201, 1, 101, "2023-10-01", "10:00 AM"),
            (202, 2, 102, "2023-10-02", "11:00 AM"),
            (203, 3, 103, "2023-10-03", "12:00 PM"),
            (204, 4, 104, "2023-10-04", "01:00 PM"),
            (205, 5, 105, "2023-10-05", "02:00 PM")
        ]

        # Set of unique specialties
        self.specialties = set()

        # Adding specialties from doctors
        for doctor in self.doctors:
            self.specialties.add(doctor[3])

        # Set of unique departments
        self.departments = set()

        # Adding departments from doctors
        for doctor in self.doctors:
            self.departments.add(doctor[4])

        # Dictionary to map patient IDs to their details
        self.patient_catalog = {patient[0]: patient for patient in self.patients}

        # Dictionary to map doctor IDs to their details
        self.doctor_catalog = {doctor[0]: doctor for doctor in self.doctors}

        # Dictionary to manage appointments
        self.appointment_schedule = {appointment[0]: appointment for appointment in self.appointments}

    # List-Related Methods
    def find_patient_index(self, patient_id):
        """Finds the index of a patient in the list."""
        for index, patient in enumerate(self.patients):
            if patient[0] == patient_id:
                return index
        return -1

    def find_doctor_index(self, doctor_id):
        """Finds the index of a doctor in the list."""
        for index, doctor in enumerate(self.doctors):
            if doctor[0] == doctor_id:
                return index
        return -1

    def sort_patients_by_age(self):
        """Sorts patients by age."""
        return sorted(self.patients, key=lambda patient: patient[2])

    def sort_doctors_by_age(self):
        """Sorts doctors by age."""
        return sorted(self.doctors, key=lambda doctor: doctor[2])

    def reverse_appointments(self):
        """Reverses the list of appointments."""
        return self.appointments[::-1]

    def append_appointment(self, appointment):
        """Appends a new appointment to the list."""
        self.appointments.append(appointment)
        print(f"Appointment '{appointment}' added.")

    def remove_appointment(self, appointment_id):
        """Removes an appointment from the list."""
        self.appointments = [a for a in self.appointments if a[0] != appointment_id]
        print(f"Appointment ID '{appointment_id}' removed.")

    # Tuple-Related Methods
    def find_max_min_age_patients(self):
        """Finds the maximum and minimum age of patients."""
        ages = [patient[2] for patient in self.patients]
        return max(ages), min(ages)

    def find_max_min_age_doctors(self):
        """Finds the maximum and minimum age of doctors."""
        ages = [doctor[2] for doctor in self.doctors]
        return max(ages), min(ages)

    def count_medical_history_occurrences(self, condition):
        """Counts the occurrences of a specific medical condition."""
        return sum(1 for patient in self.patients if condition in patient[4])

    # Set-Related Methods
    def add_specialty(self, specialty):
        """Adds a new specialty."""
        self.specialties.add(specialty)
        print(f"Specialty '{specialty}' added.")

    def remove_specialty(self, specialty):
        """Removes a specialty."""
        self.specialties.discard(specialty)
        print(f"Specialty '{specialty}' removed.")

    def list_all_specialties(self):
        """Lists all specialties."""
        return self.specialties

    def add_department(self, department):
        """Adds a new department."""
        self.departments.add(department)
        print(f"Department '{department}' added.")

    def remove_department(self, department):
        """Removes a department."""
        self.departments.discard(department)
        print(f"Department '{department}' removed.")

    def list_all_departments(self):
        """Lists all departments."""
        return self.departments

    def find_common_specialties(self, other_specialties):
        """Finds common specialties between two sets."""
        return self.specialties.intersection(other_specialties)

    def find_unique_specialties(self):
        """Finds unique specialties in the hospital."""
        return self.specialties.difference({"Cardiology", "Neurology", "Orthopedics", "Pediatrics", "General Medicine"})

    def clear_specialties(self):
        """Clears all specialties."""
        self.specialties.clear()
        print("All specialties cleared.")

    # Dictionary-Related Methods
    def add_patient(self, patient_id, name, age, gender, medical_history):
        """Adds a new patient to the hospital."""
        if patient_id not in self.patient_catalog:
            self.patient_catalog[patient_id] = (patient_id, name, age, gender, medical_history)
            print(f"Patient '{name}' added.")
        else:
            print(f"Patient ID '{patient_id}' already exists.")

    def remove_patient(self, patient_id):
        """Removes a patient from the hospital."""
        if patient_id in self.patient_catalog:
            patient_details = self.patient_catalog.pop(patient_id)
            print(f"Patient '{patient_details[1]}' removed.")
        else:
            print(f"Patient ID '{patient_id}' not found.")

    def get_patient_details(self, patient_id):
        """Gets patient details."""
        return self.patient_catalog.get(patient_id, "Patient not found.")

    def list_patients_by_gender(self, gender):
        """Lists all patients by gender."""
        return [patient for patient in self.patients if patient[3] == gender]

    def count_patients_by_gender(self, gender):
        """Counts patients by gender."""
        return sum(1 for patient in self.patients if patient[3] == gender)

    def add_doctor(self, doctor_id, name, age, specialty, department):
        """Adds a new doctor to the hospital."""
        if doctor_id not in self.doctor_catalog:
            self.doctor_catalog[doctor_id] = (doctor_id, name, age, specialty, department)
            self.specialties.add(specialty)
            self.departments.add(department)
            print(f"Doctor '{name}' added.")
        else:
            print(f"Doctor ID '{doctor_id}' already exists.")

    def remove_doctor(self, doctor_id):
        """Removes a doctor from the hospital."""
        if doctor_id in self.doctor_catalog:
            doctor_details = self.doctor_catalog.pop(doctor_id)
            print(f"Doctor '{doctor_details[1]}' removed.")
        else:
            print(f"Doctor ID '{doctor_id}' not found.")

    def get_doctor_details(self, doctor_id):
        """Gets doctor details."""
        return self.doctor_catalog.get(doctor_id, "Doctor not found.")

    def list_doctors_by_department(self, department):
        """Lists all doctors by department."""
        return [doctor for doctor in self.doctors if doctor[4] == department]

    def count_doctors_by_department(self, department):
        """Counts doctors by department."""
        return sum(1 for doctor in self.doctors if doctor[4] == department)

    def update_patient_details(self, patient_id, new_details):
        """Updates patient details."""
        if patient_id in self.patient_catalog:
            self.patient_catalog[patient_id] = new_details
            print(f"Updated details for patient ID '{patient_id}'.")
        else:
            print(f"Patient ID '{patient_id}' not found.")

    def update_doctor_details(self, doctor_id, new_details):
        """Updates doctor details."""
        if doctor_id in self.doctor_catalog:
            self.doctor_catalog[doctor_id] = new_details
            print(f"Updated details for doctor ID '{doctor_id}'.")
        else:
            print(f"Doctor ID '{doctor_id}' not found.")

    def merge_patient_catalogs(self, other_catalog):
        """Merges two patient catalogs."""
        for patient_id, details in other_catalog.items():
            if patient_id not in self.patient_catalog:
                self.patient_catalog[patient_id] = details
        print("Patient catalogs merged.")

    def merge_doctor_catalogs(self, other_catalog):
        """Merges two doctor catalogs."""
        for doctor_id, details in other_catalog.items():
            if doctor_id not in self.doctor_catalog:
                self.doctor_catalog[doctor_id] = details
                self.specialties.add(details[3])
                self.departments.add(details[4])
        print("Doctor catalogs merged.")

    def get_all_patient_ids(self):
        """Gets all patient IDs."""
        return list(self.patient_catalog.keys())

    def get_all_doctor_ids(self):
        """Gets all doctor IDs."""
        return list(self.doctor_catalog.keys())

    def clear_patient_catalog(self):
        """Clears the patient catalog."""
        self.patient_catalog.clear()
        print("Patient catalog cleared.")

    def clear_doctor_catalog(self):
        """Clears the doctor catalog."""
        self.doctor_catalog.clear()
        print("Doctor catalog cleared.")

# Example usage
if __name__ == "__main__":
    hospital = HospitalManagement()

    print("Patient Catalog:")
    for patient_id, details in hospital.patient_catalog.items():
        print(f"{patient_id}: {details}")

    print("\nDoctor Catalog:")
    for doctor_id, details in hospital.doctor_catalog.items():
        print(f"{doctor_id}: {details}")

    print("\nSpecialties Available:")
    print(hospital.specialties)

    print("\nDepartments Available:")
    print(hospital.departments)

    print("\nAppointment Schedule:")
    for appointment_id, details in hospital.appointment_schedule.items():
        print(f"Appointment ID {appointment_id}: {details}")

    # Add and remove patients
    hospital.add_patient(6, "Frank", 60, "Male", {"Diabetes"})
    hospital.remove_patient(3)

    print("\nPatient Catalog After Changes:")
    for patient_id, details in hospital.patient_catalog.items():
        print(f"{patient_id}: {details}")

    # Get patient details
    print("\nPatient Details for ID 2:")
    print(hospital.get_patient_details(2))

    # List patients by gender
    print("\nMale Patients:")
    print(hospital.list_patients_by_gender("Male"))

    # Count patients by gender
    print("\nCount of Female Patients:")
    print(hospital.count_patients_by_gender("Female"))

    # Find patient index
    print("\nIndex of Patient ID 2:")
    print(hospital.find_patient_index(2))

    # Add and remove specialties
    hospital.add_specialty("Dermatology")
    hospital.remove_specialty("Orthopedics")

    # List all specialties
    print("\nAll Specialties:")
    print(hospital.list_all_specialties())

    # Add and remove departments
    hospital.add_department("Dermatology")
    hospital.remove_department("Orthopedics")

    # List all departments
    print("\nAll Departments:")
    print(hospital.list_all_departments())

    # Append and remove appointments
    hospital.append_appointment((206, 1, 101, "2023-10-06", "03:00 PM"))
    hospital.remove_appointment(202)

    print("\nAppointments After Changes:")
    for appointment in hospital.appointments:
        print(appointment)

    # Sort patients by age
    print("\nPatients Sorted by Age:")
    for patient in hospital.sort_patients_by_age():
        print(patient)

    # Sort doctors by age
    print("\nDoctors Sorted by Age:")
    for doctor in hospital.sort_doctors_by_age():
        print(doctor)

    # Reverse the list of appointments
    print("\nReversed List of Appointments:")
    print(hospital.reverse_appointments())

    # Find the maximum and minimum age of patients
    max_age_patients, min_age_patients = hospital.find_max_min_age_patients()
    print(f"\nMaximum Age of Patients: {max_age_patients}, Minimum Age of Patients: {min_age_patients}")

    # Find the maximum and minimum age of doctors
    max_age_doctors, min_age_doctors = hospital.find_max_min_age_doctors()
    print(f"\nMaximum Age of Doctors: {max_age_doctors}, Minimum Age of Doctors: {min_age_doctors}")

    # Count the occurrences of a specific medical condition
    print(f"\nOccurrences of 'Diabetes': {hospital.count_medical_history_occurrences('Diabetes')}")

    # Find common specialties between two sets
    other_specialties = {"Cardiology", "Dermatology", "Neurology"}
    print(f"\nCommon Specialties: {hospital.find_common_specialties(other_specialties)}")

    # Find unique specialties in the hospital
    print(f"\nUnique Specialties: {hospital.find_unique_specialties()}")

    # Update patient details
    hospital.update_patient_details(2, (2, "Bob", 46, "Male", {"Asthma", "Diabetes"}))
    print(f"\nUpdated Patient Details for ID 2: {hospital.get_patient_details(2)}")

    # Update doctor details
    hospital.update_doctor_details(102, (102, "Dr. Johnson", 41, "Neurology", "Neurology"))
    print(f"\nUpdated Doctor Details for ID 102: {hospital.get_doctor_details(102)}")

    # Merge two patient catalogs
    other_patient_catalog = {
        7: (7, "Grace", 40, "Female", {"Hypertension"}),
        8: (8, "Hank", 55, "Male", {"Arthritis"})
    }
    hospital.merge_patient_catalogs(other_patient_catalog)
    print("\nMerged Patient Catalog:")
    for patient_id, details in hospital.patient_catalog.items():
        print(f"{patient_id}: {details}")

    # Merge two doctor catalogs
    other_doctor_catalog = {
        106: (106, "Dr. Blue", 60, "Dermatology", "Dermatology"),
        107: (107, "Dr. Red", 50, "Neurology", "Neurology")
    }
    hospital.merge_doctor_catalogs(other_doctor_catalog)
    print("\nMerged Doctor Catalog:")
    for doctor_id, details in hospital.doctor_catalog.items():
        print(f"{doctor_id}: {details}")

    # Get all patient IDs
    print("\nAll Patient IDs:")
    print(hospital.get_all_patient_ids())

    # Get all doctor IDs
    print("\nAll Doctor IDs:")
    print(hospital.get_all_doctor_ids())

    # Clear the patient catalog
    hospital.clear_patient_catalog()
    print("\nPatient Catalog After Clearing:")
    print(hospital.patient_catalog)

    # Clear the doctor catalog
    hospital.clear_doctor_catalog()
    print("\nDoctor Catalog After Clearing:")
    print(hospital.doctor_catalog)