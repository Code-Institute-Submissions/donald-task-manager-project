$(document).ready(function () {
    $(".sidenav").sidenav({draggable: "left"});
    $('select').formSelect();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('.datepicker').datepicker({
        format: "mm/ dd/ yyyy",
        defaultDate: null,
        yearRange: 5,
        showClearBtn: true,

    });    

    var elem = document.querySelector('.collapsible.expandable');
    var instance = M.Collapsible.init(elem, {
    accordion: false
    });

            
});