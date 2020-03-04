$(document).ready(function (){
  $('body').scrollspy({ target: '.navbar',offset: $('.navbar-nav').height()+50});

  $('.nav-link').on('click', function(){
    var clickedItem = $(this).attr('href');
    $('html, body').animate({
        scrollTop: $(clickedItem).offset().top - $('.navbar-nav').height()*1.15
    }, 500);
  });

	$('.btn').on('click', function(){
		var clickedItem = $(this).attr('href');
		$('html, body').animate({
				scrollTop: $(clickedItem).offset().top - $('.navbar-nav').height()*1.15 - 50
		}, 500);
	});

	$('.navbar-nav>li>a').on('click', function(){
			$('.navbar-collapse').collapse('hide');
	});

	$('.collapse').collapse()

});
$('.navbar-collapse').collapse('hide')
