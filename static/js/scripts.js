function addReview() {
    url = "/reviews/create/" + $("#submit-review").val();
  
    $.ajax({
      type: "POST",
      url: url,
      data: $(this).serialize(),
      success: function (data) {
        showSuccToast('Review added Successfully!');
      },
      error: function (data) {
        showFailToast('Review is not added!', data.responseJSON.error);
      }
    });
  
    return false;
}

function addReviewRating() {
    url = "/reviews/createrating/" + $("#submit-review").val();
  
    $.ajax({
      type: "POST",
      url: url,
      data: $(this).serialize(),
      success: function (data) {
        showSuccToast('Review added Successfully!');
      },
      error: function (data) {
        showFailToast('Review is not added!', data.responseJSON.error);
      }
    });
  
    return false;
}

function send_offer() {
    console.log("hi");
    $.ajax({
      type: "POST",
      url: '/offers/create/' + $(this).val(),
      data: $('.modal-form').serialize(),
      success: function (data) {
      },
      error: function (data) {
      }
    });
}

function pet_description() {
    $.ajax({
      type: "POST",
      url: '/pets/create',
      data: $('.modal-form').serialize(),
      success: function (data) {
      },
      error: function (data) {
      }
    });
}

$('.send_btn.hire').on('click', send_offer);
$('.send_btn.pet').on('click', pet_description);
