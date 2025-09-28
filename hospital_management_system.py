# Hospital Management System (Python Only, In-Memory, OOP Approach)

class Patient:
    next_id = 1
    def __init__(self, name, age, gender, problem):
        self.id = Patient.next_id
        Patient.next_id += 1
        self.name = name
        self.age = age
        self.gender = gender
        self.problem = problem

class Doctor:
    next_id = 1
    def __init__(self, name, specialty):
        self.id = Doctor.next_id
        Doctor.next_id += 1
        self.name = name
        self.specialty = specialty

class Appointment:
    next_id = 1
    def __init__(self, patient, doctor, date, time):
        self.id = Appointment.next_id
        Appointment.next_id += 1
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    # Patient Methods
    def add_patient(self, name, age, gender, problem):
        patient = Patient(name, age, gender, problem)
        self.patients.append(patient)
        print(f"Patient '{name}' added with ID {patient.id}.")

    def show_patients(self):
        if not self.patients:
            print("No patients registered.")
            return
        print("Patients List:")
        for p in self.patients:
            print(f"ID: {p.id}, Name: {p.name}, Age: {p.age}, Gender: {p.gender}, Problem: {p.problem}")

    # Doctor Methods
    def add_doctor(self, name, specialty):
        doctor = Doctor(name, specialty)
        self.doctors.append(doctor)
        print(f"Doctor '{name}' added with ID {doctor.id}.")

    def show_doctors(self):
        if not self.doctors:
            print("No doctors registered.")
            return
        print("Doctors List:")
        for d in self.doctors:
            print(f"ID: {d.id}, Name: {d.name}, Specialty: {d.specialty}")

    # Appointment Methods
    def schedule_appointment(self, patient_id, doctor_id, date, time):
        patient = next((p for p in self.patients if p.id == patient_id), None)
        doctor = next((d for d in self.doctors if d.id == doctor_id), None)
        if not patient or not doctor:
            print("Invalid patient or doctor ID.")
            return
        appt = Appointment(patient, doctor, date, time)
        self.appointments.append(appt)
        print(f"Appointment scheduled for Patient {patient.name} with Dr. {doctor.name} on {date} at {time}.")

    def show_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
            return
        print("Appointments List:")
        for a in self.appointments:
            print(f"ID: {a.id}, Patient: {a.patient.name}, Doctor: {a.doctor.name}, Date: {a.date}, Time: {a.time}")

# CLI Logic
def main():
    hms = HospitalManagementSystem()
    while True:
        print('\n--- Hospital Management System ---')
        print('1. Add Patient')
        print('2. List Patients')
        print('3. Add Doctor')
        print('4. List Doctors')
        print('5. Schedule Appointment')
        print('6. List Appointments')
        print('7. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            name = input('Enter patient name: ')
            age = input('Enter patient age: ')
            gender = input('Enter patient gender: ')
            problem = input('Enter patient problem: ')
            hms.add_patient(name, age, gender, problem)
        elif choice == '2':
            hms.show_patients()
        elif choice == '3':
            name = input('Enter doctor name: ')
            specialty = input('Enter specialty: ')
            hms.add_doctor(name, specialty)
        elif choice == '4':
            hms.show_doctors()
        elif choice == '5':
            hms.show_patients()
            patient_id = int(input('Enter patient ID: '))
            hms.show_doctors()
            doctor_id = int(input('Enter doctor ID: '))
            date = input('Enter appointment date (YYYY-MM-DD): ')
            time = input('Enter appointment time (HH:MM): ')
            hms.schedule_appointment(patient_id, doctor_id, date, time)
        elif choice == '6':
            hms.show_appointments()
        elif choice == '7':
            print('Exiting the system. Goodbye!')
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == "__main__":
    main()
