const offcanvas = document.querySelector("#offcanvas");
const openButton = document.getElementById("open-button");
const closeButton = document.getElementById("close-button");
const contactAnchor = document.getElementById("contact-anchor");

openButton.addEventListener("click", () => {
  offcanvas.style.right = "0";
});

closeButton.addEventListener("click", () => {
  offcanvas.style.right = "-350px";
});

contaxtAnchor.addEventListener("click", () => {
  offcanvas.style.right = "-350px";
});