$(function() {

    var modifyHeaderOnScroll = function(section_index) {
        var header_colors = new Object();

        header_colors[1] = "#131313";
        header_colors[2] = "#E3E3E3";
        header_colors[3] = "#E3E3E3";

        $('#logo').css('color', header_colors[section_index]);
        $('.boff-link').css('color', header_colors[section_index]);

    }

    var expandProjectInfo = function(event) {

        var $selected = $(event.target);
        var $parent_portfolio = $($selected.parents('.portfolio'));
        var $detail_div = $($parent_portfolio.children('.project-details'));

        if($detail_div.css('opacity') == '1') {
            $selected.text('More Info');
            $detail_div.css('max-height', '0');
            $detail_div.css('opacity', '0');
        } else {
            $selected.text('Less Info');
            $detail_div.css('max-height', '1000px');
            $detail_div.css('opacity', '1');
        }

        if($selected.attr('class') != "project") {
            $selected = $selected.parent();
        }
        $selected.css('opacity', '1');
        $selected.css('height', 'auto');
    }

    var main = function() {
        // Start fullpage.js
        $('#fullpage').fullpage({
            autoScrolling: false,
            fitToSection: false,

            afterLoad: function(anchorLink, index) {
                modifyHeaderOnScroll(index);
            }
        });

        // Hijack clicking on projects in the portfolio
        $('.project-more-info').on('click', expandProjectInfo);
        

        $(document).ready(function() {
        });
    }

    main();
})