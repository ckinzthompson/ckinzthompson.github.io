$(document).ready(function (){
  $('body').scrollspy({ target: '.navbar',offset: $('.navbar-nav').height()});

  $('.nav-link').on('click', function(){
    var clickedItem = $(this).attr('href');
    $('html, body').animate({
        scrollTop: $(clickedItem).offset().top - $('.navbar-nav').height()
    }, 500);
  });

	$('.btn').on('click', function(){
		var clickedItem = $(this).attr('href');
		$('html, body').animate({
				scrollTop: $(clickedItem).offset().top - $('.navbar-nav').height() - 20
		}, 500);
	});

	$('.navbar-nav>li>a').on('click', function(){
			$('.navbar-collapse').collapse('hide');
	});

	// $('.collapse').collapse()
});
