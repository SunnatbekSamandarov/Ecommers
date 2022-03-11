jQuery(function($){
$('button.catb').click(function(){
  $('.catb_list').toggleClass('active');

});
$('button.search').click(function(){
  $('.search_box').toggleClass('active');
  $(this).toggleClass('active');

});
	 $('.product_gal-pict').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: false,
      fade: true,
      asNavFor: '.product_gal-list'
    });
    $('.product_gal-list').slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      asNavFor: '.product_gal-pict',
      dots: false,
      nav:false,
      arrows:false,
      autoplay: true,
      autoplaySpeed: 6000,
      focusOnSelect: true,
    });	
    $('.products_list').slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      arrows:true,
      dots:false,
      autoplay: true,
      autoplaySpeed: 2000,
      responsive: [
      {
        breakpoint: 800,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        }
      }
    ]
    });  
      
    $('.pro_list').slick({
      slidesToShow: 2,
      slidesToScroll: 1,
      arrows:true,
      dots:false,
      autoplay: true,
      autoplaySpeed: 2000,
      responsive: [
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1
        }
      }
    ]
    }); 
  
    $('.quote_list').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      autoplay: true,
      fade: true,
      autoplaySpeed: 2000,
    });
    $('.diler_list').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      fade: true,
    });
    $('.doma_list').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      fade: true,
    });
    $('.mag_list').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      fade: true,
    });
});
$(window).on('scroll', function (event) {
    var scrollValue = $(window).scrollTop();
    if (scrollValue > 90) {
        $('nav.navbar').addClass('affix');
    } else{
        $('nav.navbar').removeClass('affix');
    }
});