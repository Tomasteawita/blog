const $id_image = document.querySelector("#id_image"),
  $imagePreView = document.querySelector("#imagePreView");

$id_image.addEventListener("change", () => {
  const field = $id_image.files;
  if (!field || !field.length) {
    $imagePreView.src = "";
    return;
  }
  
  const firstField = field[0];
  const objectURL = URL.createObjectURL(firstField);
  $imagePreView.src = objectURL;
});

// Obtén una referencia al div con el id "id_tags"
var divTags = document.querySelector("#id_tags");
var id_state = document.querySelector("#id_state");
// Obtén todos los elementos input dentro del div
var inputs = divTags.getElementsByTagName("input");

// Itera a través de los elementos input y aplica el estilo "width: 16px"
for (var i = 0; i < inputs.length; i++) {
  inputs[i].style.width = "16px";
}
id_state.style.width = "16px";

document.addEventListener("DOMContentLoaded", function() {
  // Obtén la referencia al campo de entrada por su id
  var dateInput = document.getElementById("id_date");

  // Crea una nueva instancia de la fecha actual
  var currentDate = new Date();

  // Formatea la fecha y la hora según tus necesidades
  var formattedDate = currentDate.toLocaleString(); // Cambia el formato según lo que desees

  // Establece el valor del campo de entrada con la fecha y hora actual
  dateInput.value = formattedDate;
});