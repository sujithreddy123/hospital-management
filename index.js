let patients = [];
let doctors = [];
let appointments = [];

// Add Patient
document.getElementById('patientForm').onsubmit = function(e) {
    e.preventDefault();
    let name = document.getElementById('patientName').value;
    let age = document.getElementById('patientAge').value;
    let gender = document.getElementById('patientGender').value;
    let problem = document.getElementById('patientProblem').value;
    let id = patients.length + 1;
    patients.push({id, name, age, gender, problem});
    document.getElementById('patientForm').reset();
    updatePatients();
    updateAppointmentPatientOptions();
};

// Add Doctor
document.getElementById('doctorForm').onsubmit = function(e) {
    e.preventDefault();
    let name = document.getElementById('doctorName').value;
    let specialty = document.getElementById('doctorSpecialty').value;
    let id = doctors.length + 1;
    doctors.push({id, name, specialty});
    document.getElementById('doctorForm').reset();
    updateDoctors();
    updateAppointmentDoctorOptions();
};

// Schedule Appointment
document.getElementById('appointmentForm').onsubmit = function(e) {
    e.preventDefault();
    let patientId = parseInt(document.getElementById('appointmentPatient').value);
    let doctorId = parseInt(document.getElementById('appointmentDoctor').value);
    let date = document.getElementById('appointmentDate').value;
    let time = document.getElementById('appointmentTime').value;
    let patient = patients.find(p => p.id === patientId);
    let doctor = doctors.find(d => d.id === doctorId);
    let id = appointments.length + 1;
    appointments.push({id, patient, doctor, date, time});
    document.getElementById('appointmentForm').reset();
    updateAppointments();
};

function updatePatients() {
    let html = "<b>Patients:</b><br><ul>";
    for (let p of patients) {
        html += `<li>ID: ${p.id}, ${p.name}, Age: ${p.age}, Gender: ${p.gender}, Problem: ${p.problem}</li>`;
    }
    html += "</ul>";
    document.getElementById('patientsList').innerHTML = html;
}

function updateDoctors() {
    let html = "<b>Doctors:</b><br><ul>";
    for (let d of doctors) {
        html += `<li>ID: ${d.id}, ${d.name}, Specialty: ${d.specialty}</li>`;
    }
    html += "</ul>";
    document.getElementById('doctorsList').innerHTML = html;
}

function updateAppointments() {
    let html = "<b>Appointments:</b><br><ul>";
    for (let a of appointments) {
        html += `<li>ID: ${a.id}, Patient: ${a.patient.name}, Doctor: ${a.doctor.name}, Date: ${a.date}, Time: ${a.time}</li>`;
    }
    html += "</ul>";
    document.getElementById('appointmentsList').innerHTML = html;
}

function updateAppointmentPatientOptions() {
    let select = document.getElementById('appointmentPatient');
    select.innerHTML = "";
    for (let p of patients) {
        select.innerHTML += `<option value="${p.id}">${p.name}</option>`;
    }
}
function updateAppointmentDoctorOptions() {
    let select = document.getElementById('appointmentDoctor');
    select.innerHTML = "";
    for (let d of doctors) {
        select.innerHTML += `<option value="${d.id}">${d.name} (${d.specialty})</option>`;
    }
}

// Initialize appointment dropdowns if page is refreshed
updateAppointmentPatientOptions();
updateAppointmentDoctorOptions();
