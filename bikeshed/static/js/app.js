function readURL(input) {
  var file = ($("#id_image"))[0].files[0];
  if (file) {
      var reader = new FileReader();

      reader.onload = function (e) {
        $('#chosenImage').css("background-image", "url(" + e.target.result + ")");
      };

      reader.readAsDataURL(file);
  }
}

$(document).on('change', '#id_image', readURL);
