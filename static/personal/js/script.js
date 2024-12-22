$(window).on("load", function () {

    "use strict";

    /* ===================================
            Loading Timeout
     ====================================== */

    setTimeout(function(){
        $('.preloader').fadeOut();

        $('.cd-transition-layer').addClass('closing').delay(1000).queue(function(){
            $(this).removeClass("visible closing opening").dequeue();
        });

    }, 1000);

});


jQuery(function ($) {


    "use strict";

    /* ===================================
        Side Menu
    ====================================== */

   $("#sidemenu_toggle").on("click", function () {
        $(".site-nav").toggleClass("active");
    }),$(".site-nav li a").on("click", function () {
        $(".site-nav").removeClass("active");
    });


    /* ===================================
         Counter
    ====================================== */


    $('.count').each(function () {
        $(this).appear(function () {
            $(this).prop('Counter', 0).animate({
                Counter: $(this).text()
            }, {
                duration: 3000,
                easing: 'swing',
                step: function (now) {
                    $(this).text(Math.ceil(now));
                }
            });
        });
    });

    $(".progress-bar").each(function () {
        $(this).appear(function () {
            $(this).animate({width: $(this).attr("aria-valuenow") + "%"}, 3000)
        });
    });


    /* ===================================
      Owl Carousel
     ====================================== */

    //Testimonial Slider

    $("#owl-client").owlCarousel({
        items: 1,
        margin:10,
        loop: true,
        dots: false,
        nav: true,
        navContainer: "#client-nav",
        responsive: {
            991: {
                items: 2,
            },
            600: {
                items: 1,
            },
            320: {
                items: 1,
            },
        }
    });

    $('.partners-slider').owlCarousel({
        items: 5,
        autoplay: 1500,
        smartSpeed: 1500,
        autoplayHoverPause: true,
        slideBy: 1,
        loop: true,
        margin: 30,
        dots: false,
        nav: false,
        responsive: {
            1200: {
                items: 5,
            },
            768: {
                items: 3,
            },
            480: {
                items: 2,
            },
            320: {
                items: 1,
            },
        }
    });

    /*============================================*
           Cube Portfolio
   * ============================================*/

    function portfolio(){

        $('#js-grid-mosaic-flat').cubeportfolio({
            layoutMode: 'mosaic',
            sortByDimension: true,
            mediaQueries: [ {
                width: 800,
                cols: 3,
            }, {
                width: 767,
                cols: 2,
            }, {
                width: 480,
                cols: 1,
            }],
            gapHorizontal: 15,
            gapVertical: 15,
            gridAdjustment: 'responsive',
            caption: 'zoom',

            // lightbox
            lightboxDelegate: '.cbp-lightbox',
            lightboxGallery: true,
            lightboxTitleSrc: 'data-title',
        });
    }

    $(document).ready(function() {

        setTimeout(function(){
            portfolio();
        }, 1000);

    });


    /* ===================================
    Mouse parallax
   ====================================== */


   $('.banner-slider,header').mousemove(function(e) {
    $('[data-depth]').each(function () {
        var depth = $(this).data('depth');
        var amountMovedX = (e.pageX * -depth/4);
        var amountMovedY = (e.pageY * -depth/4);

        $(this).css({
            'transform':'translate3d(' + amountMovedX +'px,' + amountMovedY +'px, 0)',
        });
    });
});

/* ===================================
  Animated Cursor
====================================== */

/* Animated Cursor */

function animatedCursor() {

    if ($(".aimated-cursor").length) {

        var e = {x: 0, y: 0}, t = {x: 0, y: 0}, n = .25, o = !1, a = document.getElementsByClassName("cursor"),
            i = document.getElementsByClassName("cursor-loader");
        TweenLite.set(a, {xPercent: -50, yPercent: -50}), document.addEventListener("mousemove", function (t) {
            var n = window.pageYOffset || document.documentElement.scrollTop;
            e.x = t.pageX, e.y = t.pageY - n
        }), TweenLite.ticker.addEventListener("tick", function () {
            o || (t.x += (e.x - t.x) * n, t.y += (e.y - t.y) * n , TweenLite.set(a, {x: t.x, y: t.y}))
        }),
            $(".animated-wrap").mouseenter(function (e) {
                TweenMax.to(this, .3, {scale: 2}), TweenMax.to(a, .3, {
                    scale: 1.5,
                    borderWidth: "1px",
                    opacity: .2
                }), TweenMax.to(i, .3, {
                    scale: 1.5,
                    borderWidth: "1px",
                    top: 1,
                    left: 1
                }), TweenMax.to($(this).children(), .3, {scale: .5}), o = !0
            }),
            $(".animated-wrap").mouseleave(function (e) {
                TweenMax.to(this, .3, {scale: 1}), TweenMax.to(a, .3, {
                    scale: 1,
                    borderWidth: "2px",
                    opacity: 1
                }), TweenMax.to(i, .3, {
                    scale: 1,
                    borderWidth: "2px",
                    top: 0,
                    left: 0
                }), TweenMax.to($(this).children(), .3, {scale: 1, x: 0, y: 0}), o = !1
            }),
            $(".animated-wrap").mousemove(function (e) {
                var n, o, i, l, r, d, c, s, p, h, x, u, w, f, m;
                n = e, o = 2, i = this.getBoundingClientRect(), l = n.pageX - i.left, r = n.pageY - i.top, d = window.pageYOffset || document.documentElement.scrollTop, t.x = i.left + i.width / 2 + (l - i.width / 2) / o, t.y = i.top + i.height / 2 + (r - i.height / 2 - d) / o, TweenMax.to(a, .3, {
                    x: t.x,
                    y: t.y
                }), s = e, p = c = this, h = c.querySelector(".animated-element"), x = 20, u = p.getBoundingClientRect(), w = s.pageX - u.left, f = s.pageY - u.top, m = window.pageYOffset || document.documentElement.scrollTop, TweenMax.to(h, .3, {
                    x: (w - u.width / 2) / u.width * x,
                    y: (f - u.height / 2 - m) / u.height * x,
                    ease: Power2.easeOut
                })
            }),
            $(".hide-cursor,.btn,.tp-bullets").mouseenter(function (e) {
                TweenMax.to(".cursor", .2, {borderWidth: "1px", scale: 2, opacity: 0})
            }), $(".hide-cursor,.btn,.tp-bullets").mouseleave(function (e) {
            TweenMax.to(".cursor", .3, {borderWidth: "2px", scale: 1, opacity: 1})
        }), $(".link").mouseenter(function (e) {
            TweenMax.to(".cursor", .2, {
                borderWidth: "0px",
                scale: 3,
                backgroundColor: "rgba(255,255,255,0.27)",
                opacity: .15
            })
        }), $(".navbar-brand.link").mouseenter(function (e) {
            TweenMax.to(".cursor", .2, {
                borderWidth: "0px",
                scale: 3,
                backgroundColor: "rgba(32,32,32,0.27)",
                opacity: .15
            })
        }), $(".crumbs .link").mouseenter(function (e) {
            TweenMax.to(".cursor", .2, {
                borderWidth: "0px",
                scale: 3,
                backgroundColor: "rgba(32,32,32,0.27)",
                opacity: .15
            })
        }), $(".link").mouseleave(function (e) {
            TweenMax.to(".cursor", .3, {
                borderWidth: "2px",
                scale: 1,
                backgroundColor: "rgba(255,255,255,0)",
                opacity: 1
            })
        })

    }

}

if ($(window).width() > 991) {
    setTimeout(function () {
        animatedCursor();
    }, 1000);
}
else{
    $('.aimated-cursor').addClass('magic');
}
$('header .side-menu').mouseenter(function () {
    $('header ~ .aimated-cursor').addClass('magic');
});
$('header .side-menu').mouseleave(function () {
    $('header ~ .aimated-cursor').removeClass('magic');
});


});


//----------JQuery-----------------//
$(function(){
    flag=0;
    $('.next').click(function(){
      if(flag == 0){
        $('.c1').css({'transform':'translateX(-100px) scale(1)','z-index':'9'});
        $('.c2').css({'transform':'translateX(100px) scale(1)','z-index':'9'});
        $('.c3').css({'transform':'translateX(0) scale(1.5)','z-index':'99'});
        flag = 1;
      } else if(flag == 1){
        $('.c3').css({'transform':'translateX(-100px) scale(1)','z-index':'9'});
        $('.c1').css({'transform':'translateX(100px) scale(1)','z-index':'9'});
        $('.c2').css({'transform':'translateX(0) scale(1.5)','z-index':'99'});
        flag = 2;
      }else if(flag == 2){
        $('.c2').css({'transform':'translateX(-100px) scale(1)','z-index':'9'});
        $('.c3').css({'transform':'translateX(100px) scale(1)','z-index':'9'});
        $('.c1').css({'transform':'translateX(0) scale(1.5)','z-index':'99'});
        flag = 0;
      }
    });
    $('.prev').click(function(){
      if(flag == 0){
        $('.c3').css({'transform':'translateX(-100px) scale(1)','z-index':'9'});
        $('.c1').css({'transform':'translateX(100px) scale(1)','z-index':'9'});
        $('.c2').css({'transform':'translateX(0) scale(1.5)','z-index':'99'});
        flag = 1;
      } else if(flag == 1){
        $('.c1').css({'transform':'translateX(-100px) scale(1)','z-index':'9'});
        $('.c2').css({'transform':'translateX(100px) scale(1)','z-index':'9'});
        $('.c3').css({'transform':'translateX(0) scale(1.5)','z-index':'99'});
        flag = 2;
      }else if(flag == 2){
        $('.c2').css({'transform':'translateX(-100px) scale(1)','z-index':'9'});
        $('.c3').css({'transform':'translateX(100px) scale(1)','z-index':'9'});
        $('.c1').css({'transform':'translateX(0) scale(1.5)','z-index':'99'});
        flag = 0;
      }
    });
  });
