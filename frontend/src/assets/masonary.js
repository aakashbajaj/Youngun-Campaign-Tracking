$(document).ready(function () {
  var width = window.screen.width;
  if (width <= 768) {
    $(".card-columns").removeClass("card-columns").addClass("row");
    $(".columns").addClass("col-sm-12");
    $(".decks").addClass("card-deck pb-5");
  } else {
    $(".row").addClass("card-columns").removeClass("row");
    $(".columns").removeClass("col-sm-12");
    $(".decks").removeClass("card-deck pb-5");
  }

  $(window).on("resize", function () {
    var width = window.screen.width;
    if (width <= 768) {
      $(".card-columns").removeClass("card-columns").addClass("row");
      $(".columns").addClass("col-sm-12");
      $(".decks").addClass("card-deck pb-5");
    } else {
      $(".row").addClass("card-columns").removeClass("row");
      $(".columns").removeClass("col-sm-12");
      $(".decks").removeClass("card-deck pb-5");
    }
  });
});
