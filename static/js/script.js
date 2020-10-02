$(document).ready(function () {
    $(".sidenav").sidenav({draggable: "left"});
    

var elem = document.querySelector('.collapsible.expandable');
var instance = M.Collapsible.init(elem, {
  accordion: false
});
            
  });