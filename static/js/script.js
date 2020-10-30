$(document).ready(function () {
    $(".sidenav").sidenav({draggable: "left"});
    $('select').formSelect();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('.fixed-action-btn').floatingActionButton();
    $('.datepicker').datepicker({
        format: "mm/ dd/ yyyy",
        defaultDate: null,
        yearRange: 5,
        showClearBtn: true,
    }); 
    $('.slider').slider({
        Boolean: true,
        Number: 400,
        Number: 500,
    });
    var elem = document.querySelector('.collapsible.expandable');
    var instance = M.Collapsible.init(elem, {
    accordion: false
    });

$('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true,
    noWrap: true,
  }); 
            
});

