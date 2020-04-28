 var closeNav = false;
function openNav() {
  closeNav = !closeNav;
  console.log(closeNav);
  if(closeNav){
  document.getElementById("mySidenav").style.width = "200px";
  document.getElementById("main").style.marginLeft = "200px";
  document.getElementById("mySidenav").style.marginTop = "62px";
}else{
    document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "100px";
}
}