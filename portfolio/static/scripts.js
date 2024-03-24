// Array of phrases to display
const phrases = [
    "Get your Beloved Lost",
    "Find Your Missing Family",
    "Reunite With Your Lost Friend",
];

let currentIndex = 0; // Index to keep track of the current phrase
// Function to change the content of the div element
function changePhrase() {
    document.getElementById("phrase-container").innerHTML = phrases[currentIndex];
    currentIndex = (currentIndex + 1) % phrases.length;
}

setInterval(changePhrase, 3000);  // Call the changePhrase function every 5 seconds (5000 milliseconds)
