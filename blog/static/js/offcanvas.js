const offcanvas = document.querySelector("#offcanvas");
const openButton = document.getElementById("open-button");
const closeButton = document.getElementById("close-button");

openButton.addEventListener("click", () => {
  offcanvas.style.right = "0";
});

closeButton.addEventListener("click", () => {
  offcanvas.style.right = "-350px";
});