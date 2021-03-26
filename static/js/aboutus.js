const employer = document.querySelector('#employer');
const jobseeker = document.querySelectorAll('#jobseeker');

employer.addEventListener("click", disable);
jobseeker.addEventListener("click", enable);

function disable() {
    document.getElementById("sentences").disabled = true;
    document.getElementById("describe").disabled = true;
    document.getElementById("formFileSm").disabled = true;
}

function enable() {
    document.getElementById("sentences").disabled = false;
    document.getElementById("describe").disabled = false;
    document.getElementById("formFileSm").disabled = false;
}