(function ($) {
    $(document).ready(function () {
        var $nav = $('.navbar');
        var lastScrollTop = 0;
        var direction;
        $(function () {
            $(window).scroll(function () {
                var scrollTop = $(this).scrollTop();

                if (lastScrollTop < scrollTop && scrollTop > $nav.outerHeight() && direction != 'down') {
                    //Scroll down
                    $nav.stop().fadeOut();
                    direction = 'down';
                } else if (lastScrollTop > scrollTop  && direction != 'up') {
                    // Scroll up
                    $nav.stop().fadeIn();
                    direction = 'up';
                }
                lastScrollTop = scrollTop;
            });
        });
    });
}(jQuery));