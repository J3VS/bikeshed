$('.bikeImage').height($('.bikeImage').width());
$('.chosenImage').height($('.chosenImage').width());

function readURL(input) {
  var file = ($("#id_image"))[0].files[0];
  if (file) {
      var reader = new FileReader();

      reader.onload = function (e) {
          $('#bikeImage')
              .attr('src', e.target.result)
              .width($('.chosenImage').width())
              .height($('.chosenImage').height());
      };

      reader.readAsDataURL(file);
  }
}

$(document).on('change', '#id_image', readURL);
