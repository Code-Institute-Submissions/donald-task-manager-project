function myFunction() {
  var x = document.getElementById("myTab");
  if (x.className === "toptab") {
    x.className += " responsive";
  } else {
    x.className = "toptab";
  }
}