$(document).ready(function(){
    
    /* --------------------------------------------------------
        Growl Function
    -----------------------------------------------------------*/
    function notify(from, align, icon, type, animIn, animOut, title, message){
       $.growl({
           icon: icon,
           title: title || 'Bootstrap Growl ',
           message: message || 'Turning standard Bootstrap alerts into awesome notifications',
           url: ''
       },{
               element: 'body',
               type: type,
               allow_dismiss: true,
               placement: {
                       from: from,
                       align: align
               },
               offset: {
                   x: 20,
                   y: 85
               },
               spacing: 10,
               z_index: 1031,
               delay: 2500,
               timer: 1000,
               url_target: '_blank',
               mouse_over: false,
               animate: {
                       enter: animIn,
                       exit: animOut
               },
               icon_type: 'class',
               template: '<div data-growl="container" class="alert" role="alert">' +
                               '<button type="button" class="close" data-growl="dismiss">' +
                                   '<span aria-hidden="true">&times;</span>' +
                                   '<span class="sr-only">Close</span>' +
                               '</button>' +
                               '<span data-growl="icon"></span>' +
                               '<span data-growl="title"></span>' +
                               '<span data-growl="message"></span>' +
                               '<a href="#" data-growl="url"></a>' +
                           '</div>'
       });
    };
    
    /* --------------------------------------------------------
        Welcome Message
    -----------------------------------------------------------*/
    notify('top', 'right', '', 'inverse', 'animated fadeIn', 'animated fadeOut', 'Welcome back ', '{{ username }}');
    
    /* --------------------------------------------------------
        Animations
    -----------------------------------------------------------*/
    $('body').on('click', '.animation-demo .ad-btn', function(){
        var animation = $(this).text();
        var cardImg = $(this).closest('.animation-demo').find('img');
        
        if (animation === "hinge") {
            animationDuration = 2100;
        }
        else {
            animationDuration = 1200;
        }
        
        cardImg.removeAttr('class');
        cardImg.addClass('animated '+animation);
        
        setTimeout(function(){
            cardImg.removeClass(animation);
        }, animationDuration);
    });

    /* --------------------------------------------------------
        Notifications and Dialog
    -----------------------------------------------------------*/
    /*
     * Notifications
     */ 
    $('.notifications > div > .btn').click(function(e){
        e.preventDefault();
        var nFrom = $(this).attr('data-from');
        var nAlign = $(this).attr('data-align');
        var nIcons = $(this).attr('data-icon');
        var nType = $(this).attr('data-type');
        var nAnimIn = $(this).attr('data-animation-in');
        var nAnimOut = $(this).attr('data-animation-out');
        
        notify(nFrom, nAlign, nIcons, nType, nAnimIn, nAnimOut);
    });

    /*
     * Dialogs
     */
 
    //Basic
    $('#sa-basic').click(function(){
        swal("Here's a message!");
    });
 
    //A title with a text under
    $('#sa-title').click(function(){
        swal("Here's a message!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis")
    });
 
    //Success Message
    $('#sa-success').click(function(){
        swal("Good job!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat, tincidunt vitae ipsum et, pellentesque maximus enim. Mauris eleifend ex semper, lobortis purus sed, pharetra felis", "success")
    });
 
    //Warning Message
    $('#sa-warning').click(function(){
        swal({   
            title: "Are you sure?",   
            text: "You will not be able to recover this imaginary file!",   
            type: "warning",   
            showCancelButton: true,   
            confirmButtonColor: "#DD6B55",   
            confirmButtonText: "Yes, delete it!",   
            closeOnConfirm: false 
        }, function(){   
            swal("Deleted!", "Your imaginary file has been deleted.", "success"); 
        });
    });
    
    //Parameter
    $('#sa-params').click(function(){
        swal({   
            title: "Are you sure?",   
            text: "You will not be able to recover this imaginary file!",   
            type: "warning",   
            showCancelButton: true,   
            confirmButtonColor: "#DD6B55",   
            confirmButtonText: "Yes, delete it!",   
            cancelButtonText: "No, cancel plx!",   
            closeOnConfirm: false,   
            closeOnCancel: false 
        }, function(isConfirm){   
            if (isConfirm) {     
                swal("Deleted!", "Your imaginary file has been deleted.", "success");   
            } else {     
                swal("Cancelled", "Your imaginary file is safe :)", "error");   
            } 
        });
    });
 
    //Custom Image
    $('#sa-image').click(function(){
        swal({   
            title: "Sweet!",   
            text: "Here's a custom image.",   
            imageUrl: "img/thumbs-up.png" 
        });
    });
 
    //Auto Close Timer
    $('#sa-close').click(function(){
        swal({   
           title: "Auto close alert!",   
           text: "I will close in 2 seconds.",   
           timer: 2000,   
           showConfirmButton: false 
       });
   });
    
    
    /* --------------------------------------------------------
        Calendar Widget
    -----------------------------------------------------------*/
    if($('.calendar-widget')[0]) {
        (function(){
            $('.calendar-widget').fullCalendar({
		contentHeight: 'auto',
		theme: true,
                header: {
                    right: '',
                    center: 'prev, title, next',
                    left: ''
                },
                defaultDate: '2014-06-12',
                editable: true,
                events: [
                    {
                        title: 'All Day',
                        start: '2014-06-01',
                        className: 'bg-cyan'
                    },
                    {
                        title: 'Long Event',
                        start: '2014-06-07',
                        className: 'bg-orange'
                    },
                    {
                        id: 999,
                        title: 'Repeat',
                        start: '2014-06-09',
                        className: 'bg-green'
                    },
                    {
                        id: 999,
                        title: 'Repeat',
                        start: '2014-06-16',
                        className: 'bg-amber'
                    },
                    {
                        title: 'Meet',
                        start: '2014-06-12',
                        className: 'bg-green'
                    },
                    {
                        title: 'Lunch',
                        start: '2014-06-12',
                        className: 'bg-cyan'
                    },
                    {
                        title: 'Birthday',
                        start: '2014-06-13',
                        className: 'bg-amber'
                    },
                    {
                        title: 'Google',
                        url: 'http://google.com/',
                        start: '2014-06-28',
                        className: 'bg-blue'
                    }
                ]
            });
        })();
    }
});