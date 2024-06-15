const YesExperience = document.getElementById('YesExperience');
const NoExperience = document.getElementById('NoExperience');
const PreviousEmployers = document.getElementById('PreviousEmployers');


function employerUpdate(){
if (NoExperience.checked){
    PreviousEmployers.style.display = "none";
} else if (YesExperience.checked){
    PreviousEmployers.style.display = "block";
}
}

employerUpdate();

YesExperience.addEventListener('change', employerUpdate);
NoExperience.addEventListener('change', employerUpdate);
