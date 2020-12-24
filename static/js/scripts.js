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
