// Button to start the survey
const startSurveyButton = document.querySelector("#start_survey");
if(startSurveyButton){
    startSurveyButton.addEventListener("click", function(){
        location.href = "/questions/0";
    });
}

// Trigger of choice selected from a question
const answer_choices = document.querySelectorAll('#answer_form input[type="radio"]');
for(const answer of answer_choices){
    answer.onclick = (e) => {
        document.getElementById("answer_form").submit();
    }
}