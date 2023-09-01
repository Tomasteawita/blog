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