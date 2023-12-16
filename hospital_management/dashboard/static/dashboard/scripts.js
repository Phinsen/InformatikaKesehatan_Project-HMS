// Define your functions

function toggleAdmissionForm(bedNumber) {
    var admissionSection = document.getElementById("admissionSection");
    var admissionButton = document.getElementById("admissionButton");
    var bedButton = document.querySelectorAll(".bed");

    if (admissionSection.style.display == "none") {
        admissionSection.style.display = "block";
        patientInfoSection.style.display = "none"
        admissionButton.innerText = "Cancel Patient";
        admissionButton.classList.add("cancel"); // Add the 'cancel' class to change button style
        bedButton.forEach(function (bed) {
            bed.style.pointerEvents = "auto"; // Enable bed buttons
        });
        document.getElementById('bedNumber').value = bedNumber; // Fill bed number
    } else {
        admissionSection.style.display = "none";
        admissionButton.innerText = "Admit Patient";
        admissionButton.classList.remove("cancel"); // Remove the 'cancel' class to revert button style
        bedButton.forEach(function (bed) {
            bed.style.pointerEvents = "none"; // Disable bed buttons
        });
        document.getElementById('bedNumber').value = ''; // Clear bed number
    }
}

function toggleTransferForm() {

}

function showBasicData() {
    document.getElementById('basicDataSection').style.display = 'block';
    document.getElementById('patientInfoSection').style.display = 'none';
}

function fillBedNumber(bedNumber) {
    document.getElementById('bedNumber').value = bedNumber;
}

function showPatientInfo() {
    document.getElementById('basicDataSection').style.display = 'none';
    document.getElementById('patientInfoSection').style.display = 'block';
}

function updateTime() {
    var today = new Date();
    var hours = today.getHours();
    var minutes = today.getMinutes();
    var seconds = today.getSeconds();

    hours = checkTime(hours);
    minutes = checkTime(minutes);
    seconds = checkTime(seconds);

    document.getElementById('time').innerHTML =
        hours + ":" + minutes + ":" + seconds;
    var t = setTimeout(updateTime, 1000);
}

function checkTime(i) {
    if (i < 10) { i = "0" + i };  // Add zero in front of numbers < 10
    return i;
}

function calculateBMI() {
    var size = parseFloat($('#sizeCm').val());
    var weight = parseFloat($('#weightKg').val());

    var bmi = (weight / ((size / 100) * (size / 100))).toFixed(2);
    var bsa = (0.007184 * Math.pow(size, 0.725) * Math.pow(weight, 0.425)).toFixed(2);

    $('#bmi').val(bmi);
    $('#bsa').val(bsa);
}

// Attach event listeners when the document is ready
$(document).ready(function() {
    $('#sizeCm').on('input', calculateBMI);
    $('#weightKg').on('input', calculateBMI);

    calculateBMI();
    updateTime();
});

function submitAll() {
    var form1 = $('#admit_patient_base');
    var form2 = $('#bed_occupancy');
    
    var formData1 = form1.serialize(); // Serialize form1
    var formData2 = form2.serialize(); // Serialize form2
    
    console.log('Form 1 data:', formData1);
    console.log('Form 2 data:', formData2);
    
     // Split the string based on '&'
    var formData1Array = formData1.split('&');

    // Initialize admissionNumber variable
    var admissionNumber = null;

    // Loop through the array to find the admission_number
    formData1Array.forEach(function (element) {
        var pair = element.split('=');
        if (pair[0] === 'admission_number') {
            admissionNumber = pair[1];
        }
    });
    // Replace admission_number value in formData1
    formData2 = formData2.replace(/admission_number=[^&]*/, 'admission_number=' + admissionNumber);
    
    console.log('Updated Form 2 data:', formData2); // Output the updated data for verification
    

    // Your AJAX calls
    $.ajax({
        type: "POST",
        url: form1.attr('action'),
        data: formData1,
        success: function(response) {
            console.log(response);
            
            // Display success message or update HTML content
            $('#submissionStatus').text('Patient data admitted successfully!');

            // Proceed with the second submission
            $.ajax({
                type: "POST",
                url: form2.attr('action'),
                data: formData2,
                success: function(response2) {
                    console.log(response2);

                    // Display success message or update HTML content
                    $('#submissionStatus').text('Patient Bed placement submitted successfully!\n Please reload the page!');
                },
                error: function(error) {
                    console.error('Error submitting form 2:', error);
                    $('#submissionStatus').text('Error in placing patient to bed');
                }
            });
        },
        error: function(error) {
            console.error('Error submitting form 1:', error);
            $('#submissionStatus').text('Error admitting patient.');
        }
    });
}