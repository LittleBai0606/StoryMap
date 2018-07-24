


/*-----------------------------------------------------------------------------------*/
/*	MENU
/*-----------------------------------------------------------------------------------*/
$(document).ready(function() {
	$('ul.sf-menu').superfish();
});


/*-----------------------------------------------------------------------------------*/
/*	IMAGE HOVER
/*-----------------------------------------------------------------------------------*/
 $(document).ready(function() {
        $('.box').mouseenter(function(e) {

            $(this).children('a').children('span').fadeIn(200);
        }).mouseleave(function(e) {

            $(this).children('a').children('span').fadeOut(200);
        });
    });
    
/*-----------------------------------------------------------------------------------*/
/*	HEADING
/*-----------------------------------------------------------------------------------*/
(function($){

	$.fn.dcHeader = function(options) {

		var defaults = {
			padding: 0,
			onLoad : function(){},
			beforeLoad : function(){}
		};
		var options = $.extend(defaults, options);
		
		return this.each(function(options){
			$(this).html('<span class="dchead left"></span><span class="dccontent">'+$(this).html()+'</span><span class="dchead right"></span><div class="clear"></div>');
			// onLoad callback;
			defaults.beforeLoad.call(this);
			$('span',this).css({display: 'block', textAlign: 'center'});
			$('.dchead.left, .dccontent').css({float: 'left'});
			$('.dchead.right').css({float: 'right'});
			var ht = $('.dccontent',this).height();
			var w = $(this).width();
			var wc = $('.dccontent',this).outerWidth(true) + (2*defaults.padding);
			var wp = Math.round((w - wc)/2);
			wc = w - (2*wp);
			$('.dccontent',this).css({padding: 0, width: wc+'px'});
			$('.dchead',this).css({padding: 0, height: ht+'px', width: wp+'px'});
			// onLoad callback;
			defaults.onLoad.call(this);
		});
	};
})(jQuery);



/*-----------------------------------------------------------------------------------*/
/*	MENU
/*-----------------------------------------------------------------------------------*/
$(window).bind("load", function() {
  
	// Add to menu container
	$('.menu').dcHeader({
		padding: 15,
		beforeLoad: function(){
			$('ul.sf-menu').superfish();
		}
	});
	
	// Add to header tags
	$('.line').dcHeader({padding: 10});
	
});


/*-----------------------------------------------------------------------------------*/
/*	TOGGLE
/*-----------------------------------------------------------------------------------*/
$(document).ready(function(){
//Hide the tooglebox when page load
$(".togglebox").hide();
//slide up and down when click over heading 2
$("h2").click(function(){
// slide toggle effect set to slow you can set it to fast too.
$(this).toggleClass("active").next(".togglebox").slideToggle("slow");
return true;
});
});


/*-----------------------------------------------------------------------------------*/
/*	TABS
/*-----------------------------------------------------------------------------------*/
$(document).ready(function() {
	//Default Action
	$(".tab_content").hide(); //Hide all content
	$("ul.tabs li:first").addClass("active").show(); //Activate first tab
	$(".tab_content:first").show(); //Show first tab content
	
	//On Click Event
	$("ul.tabs li").click(function() {
		$("ul.tabs li").removeClass("active"); //Remove any "active" class
		$(this).addClass("active"); //Add "active" class to selected tab
		$(".tab_content").hide(); //Hide all tab content
		var activeTab = $(this).find("a").attr("href"); //Find the rel attribute value to identify the active tab + content
		$(activeTab).fadeIn(); //Fade in the active content
		return false;
	});

});

/*-----------------------------------------------------------------------------------*/
/*	PRETTYPHOTO
/*-----------------------------------------------------------------------------------*/

$(document).ready(function(){
			$("a[rel^='prettyPhoto']").prettyPhoto({autoplay_slideshow: false, overlay_gallery: false, social_tools:false, deeplinking: false, theme:'pp_default', slideshow:5000});
		});

