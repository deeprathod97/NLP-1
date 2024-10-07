document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        const squareFootage = document.getElementById('square_footage').value;
        const bedrooms = document.getElementById('bedrooms').value;
        const bathrooms = document.getElementById('bathrooms').value;

        if (squareFootage <= 0 || bedrooms <= 0 || bathrooms <= 0) {
            alert("Please enter valid positive numbers for all fields.");
            event.preventDefault(); // Prevent form submission
        }
    });
});