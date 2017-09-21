/* --------------------------------------------------------
    Detact Mobile Browser
-----------------------------------------------------------*/
if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
   $('html').addClass('ismobile');
}

$(document).ready(function(){
    /* --------------------------------------------------------
        Tooltips
    -----------------------------------------------------------*/
    if($('[data-toggle="tooltip"]')[0]) {
	   $('[data-toggle="tooltip"]').tooltip();
    }
    
    
    /* --------------------------------------------------------
        Popover
    -----------------------------------------------------------*/
    if($('.pover')[0]) {
	   $('.pover').popover();
    }
    
    
    /* --------------------------------------------------------
        Scrollbar
    -----------------------------------------------------------*/
   function scrollBar(selector, theme) {
      $(selector).mCustomScrollbar({
         theme: theme,
         scrollInertia: 500,
      });
   }
        
   if (!$('html').hasClass('ismobile')) {
      //Scrollbar for sidebar
      scrollBar('#sidebar', 'minimal');
      
      //For custom
      if ($('.c-overflow')[0]) {
         scrollBar('.c-overflow', 'minimal');
      }
      
      //For Custom Dark
      if ($('.c-overflow-dark')[0]) {
         scrollBar('.c-overflow-dark', 'dark');
      }
   }
    
    
    /* --------------------------------------------------------
        Sidebar
    -----------------------------------------------------------*/
    $('body').on('click', '.sm-sub > a', function(e) {
        e.preventDefault();
        
        var s = $('#sidebar').css('width'); //This is to get the screen size. If it's 64px it's a mid screen size otherwise large/small screen.
        var x = $(this).closest('.sm-sub');
        
        if (s == '240px') { //Only fire this on large/small screen.
            x.find('ul').slideToggle(200);
            x.toggleClass('toggled');
            
        }
    });
    
    //Mobile Menu
    $('body').on('click', '#menu-trigger', function() {
        $(this).toggleClass('toggled');
        $('#sidebar').toggleClass('toggled');
    });
        
    
    /* --------------------------------------------------------
        Fullscreen browsing
    -----------------------------------------------------------*/
    $("[data-toggle='fullscreen']").click(function(e) {
        e.preventDefault();
        var docElement, request;
        
        if(!$(this).hasClass('toggled')){
            $(this).addClass('toggled');
            
            docElement = document.documentElement;
            request = docElement.requestFullScreen || docElement.webkitRequestFullScreen || docElement.mozRequestFullScreen || docElement.msRequestFullScreen;
        
            if(typeof request!="undefined" && request){
                request.call(docElement);
            }
        }
        else {
            $("[data-toggle='fullscreen']").removeClass('toggled');
            docElement = document;
            request = docElement.cancelFullScreen|| docElement.webkitCancelFullScreen || docElement.mozCancelFullScreen || docElement.msCancelFullScreen || docElement.exitFullscreen;
            if(typeof request!="undefined" && request){
                request.call(docElement);
            }
        }
    });
    
    
    /* --------------------------------------------------------
        TEXTAREA AUTOSIZE
    -----------------------------------------------------------*/
    if ($('.auto-size')[0]) {
	   autosize($('.auto-size'));
    }
    

    /* --------------------------------------------------------
        CHOSEN
    -----------------------------------------------------------*/
    if($('.tag-select')[0]) {
        $('.tag-select').chosen({
            width: '100%',
            allow_single_deselect: true
        });
    }
    
    
    /* --------------------------------------------------------
        DATETIME PICKER
    -----------------------------------------------------------*/
    //Date Time Picker
    if ($('.date-time-picker')[0]) {
	   $('.date-time-picker').datetimepicker();
    }
    
    //Time
    if ($('.time-picker')[0]) {
    	$('.time-picker').datetimepicker({
    	    format: 'LT'
    	});
    }
    
    //Date
    if ($('.date-picker')[0]) {
    	$('.date-picker').datetimepicker({
    	    format: 'DD/MM/YYYY'
    	});
    }
    
    
    /* --------------------------------------------------------
        NOUISLIDER
    -----------------------------------------------------------*/
    if($('.input-slider')[0]) {
        $('.input-slider').each(function(){
            var isStart = $(this).data('is-start');
            
            $(this).noUiSlider({
                start: isStart,
                range: {
                    'min': 0,
                    'max': 100,
                }
            });
        });
    }
	
    //Range slider
    if($('.input-slider-range')[0]) {
        $('.input-slider-range').noUiSlider({
            start: [30, 60],
            range: {
                'min': 0,
                'max': 100
            },
            connect: true
        });
    }
    
    //Range slider with value
    if($('.input-slider-values')[0]) {
        $('.input-slider-values').noUiSlider({
            start: [ 45, 80 ],
            connect: true,
            direction: 'rtl',
            behaviour: 'tap-drag',
            range: {
                'min': 0,
                'max': 100
            }
        });

        $('.input-slider-values').Link('lower').to($('#value-lower'));
        $('.input-slider-values').Link('upper').to($('#value-upper'), 'html');
    }
    
    
    /* --------------------------------------------------------
         COLOR PICKER
     -----------------------------------------------------------*/
    if ($('.color-picker')[0]) {
	    $('.color-picker').each(function(){
            var colorOutput = $(this).closest('.cp-container').find('.cp-value');
            $(this).farbtastic(colorOutput);
        });
    }
	
    
    /* --------------------------------------------------------
         SUMMERNOTE
     -----------------------------------------------------------*/
    if ($('.html-editor')[0]) {
	   $('.html-editor').summernote({
            height: 150
        });
    }
    
    if($('.html-editor-click')[0]) {
        //Edit
        $('body').on('click', '.hec-button', function(){
            $('.html-editor-click').summernote({
                focus: true
            });
            $('.hec-save').show();
        })
	
        //Save
        $('body').on('click', '.hec-save', function(){
            $('.html-editor-click').code();
            $('.html-editor-click').destroy();
            $('.hec-save').hide();
            notify('Content Saved Successfully!', 'success');
        });
    }
        
    //Air Mode
    if($('.html-editor-airmod')[0]) {
        $('.html-editor-airmod').summernote({
            airMode: true
        });
    }
    
    
    /** TYPEAHEAD **/
     if($('.typeahead')[0]) {
          
          var statesArray = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
            'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii',
            'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
            'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
            'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
            'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
            'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
            'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
            'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
          ];
        var states = new Bloodhound({
            datumTokenizer: Bloodhound.tokenizers.whitespace,
            queryTokenizer: Bloodhound.tokenizers.whitespace,
            local: statesArray
        });  
        
        $('.typeahead').typeahead({
            hint: true,
            highlight: true,
            minLength: 1
        },
        {
          name: 'states',
          source: states
        });
    }
    
    
    /* --------------------------------------------------------
        Light Gallery
     -----------------------------------------------------------*/
    if($('.lightbox')[0]) {
        $(".lightbox").lightGallery(); 
    }
    
    
    /* --------------------------------------------------------
        Media Elements
     -----------------------------------------------------------*/
    if($('audio, video')[0]) {
        $('video,audio').mediaelementplayer();
    }
    
    
    /* --------------------------------------------------------
        Wizard
     -----------------------------------------------------------*/
    if ($('.form-wizard-basic')[0]) {
    	$('.form-wizard-basic').bootstrapWizard({
    	    tabClass: 'fw-nav',
            'nextSelector': '.next', 
            'previousSelector': '.previous'
    	});
    }
    
    
    /* --------------------------------------------------------
        Link Prevent
     -----------------------------------------------------------*/
    if ($('.a-prevent')[0]) {
        $('body').on('click', '.a-prevent', function(e){
            e.preventDefault();
        });
    }
    
    
    /* --------------------------------------------------------
        Collapse Fix
     -----------------------------------------------------------*/
    if ($('.collapse')[0]) {
        
        //Add active class for opened items
        $('.collapse').on('show.bs.collapse', function (e) {
            $(this).closest('.panel').find('.panel-heading').addClass('active');
        });
   
        $('.collapse').on('hide.bs.collapse', function (e) {
            $(this).closest('.panel').find('.panel-heading').removeClass('active');
        });
        
        //Add active class for pre opened items
        $('.collapse.in').each(function(){
            $(this).closest('.panel').find('.panel-heading').addClass('active');
        });
    }
    
    
    /* --------------------------------------------------------
        Popover
     -----------------------------------------------------------*/
    if ($('[data-toggle="popover"]')[0]) {
        $('[data-toggle="popover"]').popover();
    }
    
    
    /* --------------------------------------------------------
        Action Header Search
    -----------------------------------------------------------*/
    if ($('.aha-trigger')[0]) {
         
        
        $('body').on('click', '.aha-trigger', function(e){
            e.preventDefault();
            x = $(this).closest('.action-header').find('.ah-search');
            
            x.fadeIn(300);
            x.find('.ahs-input').focus();
        });
        
        //Close Search
        $('body').on('click', '.ahs-close', function(){
            x.fadeOut(300);
            setTimeout(function(){
                x.find('.ahs-input').val('');
            }, 350);
        })
    }
    
    
    /* --------------------------------------------------------
        Profile Edit Toggle
    -----------------------------------------------------------*/
    if ($('[data-pmb-action]')[0]) {
        $('body').on('click', '[data-pmb-action]', function(e){
            e.preventDefault();
            var d = $(this).data('pmb-action');
            
            if (d === "edit") {
                $(this).closest('.pmb-block').toggleClass('toggled');
            }
            
            if (d === "reset") {
                $(this).closest('.pmb-block').removeClass('toggled');
            }
            
            
        });
    }
    
    
    /* --------------------------------------------------------
        Print
    -----------------------------------------------------------*/
    if ($('[data-action="print"]')[0]) {
        $('body').on('click', '[data-action="print"]', function(e){
            e.preventDefault();
            
            window.print();
        })
    }
    
    
    /* --------------------------------------------------------
        Login
    -----------------------------------------------------------*/
    if ($('.login-content')[0]) {
        //Add class to HTML. This is used to center align the logn box
        $('html').addClass('login-content');
        
        $('body').on('click', '.login-navigation > li', function(){
            var z = $(this).data('block');
            var t = $(this).closest('.lc-block');
            
            t.removeClass('toggled');
            
            setTimeout(function(){
                $(z).addClass('toggled');
            });
            
        })
    }
    
    
    /* --------------------------------------------------------
        Header Search
    -----------------------------------------------------------*/
    if ($('.top-search')[0]) {
        $('body').on('click', '.ts-input', function(){
            $(this).parent().addClass('toggled');
        });
        
        //Reset Search
        $('body').on('click', '.ts-reset', function() {
            $('.top-search .ts-input').val('');
            $('.top-search').removeClass('toggled');
        });
    }
    
    
    /* --------------------------------------------------------
        IE 9 Placeholder
    -----------------------------------------------------------*/
    if($('html').hasClass('ie9')) {
        $('input, textarea').placeholder({
            customClass: 'ie9-placeholder'
        });
    }
    
    
    /* --------------------------------------------------------
        Messages
    -----------------------------------------------------------*/
    if ($('#ms-menu-trigger')[0]) {
        $('body').on('click', '#ms-menu-trigger', function() {
            $('.ms-menu').toggleClass('toggled'); 
        });
    }
});

/* --------------------------------------------------------
    Date Time Widget
-----------------------------------------------------------*/
(function(){
    // Create a newDate() object
    var newDate = new Date();

    setInterval(function() {
        // Create a newDate() object and extract the seconds of the current time on the visitor's
        var seconds = new Date().getSeconds();

        // Add a leading zero to seconds value
        $("#t-sec").html(( seconds < 10 ? "0":"" ) + seconds);
    },100);

    setInterval(function() {
        // Create a newDate() object and extract the minutes of the current time on the visitor's
        var minutes = new Date().getMinutes();

        // Add a leading zero to the minutes value
        $("#t-min").html(( minutes < 10 ? "0":"" ) + minutes);
    },100);

    setInterval(function() {
        // Create a newDate() object and extract the hours of the current time on the visitor's
        var hours = new Date().getHours();

        // Add a leading zero to the hours value
        $("#t-hours").html(( hours < 10 ? "0" : "" ) + hours);
    }, 100);
})();

$(window).load(function(){ 
    /* --------------------------------------------------------
        Animate numbers
     -----------------------------------------------------------*/
    $('.mini-charts > div').each(function(){
        var target = $(this).find('.media-body > span');
        var toAnimate = $(this).find('.media-body > span').attr('data-value');
        // Animate the element's value from x to y:
        $({someValue: 0}).animate({someValue: toAnimate}, {
            duration: 2000,
            easing:'swing', // can be anything
            step: function() { // called on every step
                // Update the element's text with rounded-up value:
                target.text(commaSeparateNumber(Math.round(this.someValue)));
            }
        });

        function commaSeparateNumber(val){
            while (/(\d+)(\d{3})/.test(val.toString())){
                val = val.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
            }
            return val;
        }
    });
});
 