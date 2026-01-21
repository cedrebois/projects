function send() {
  const elementThought = document.querySelector(".thought-input").value;
  const elementConsideration = document.querySelector(".consideration-input").value;

  document.querySelector(".thought-output").innerText = `${elementThought}`
  document.querySelector(".consideration-output").innerText = `${elementConsideration}`
}