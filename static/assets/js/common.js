function openNav() {
  document.getElementById("mySidenav").style.right = "0px";
  document.getElementById("black").style.display = "inline";
}

function closeNav() {
  document.getElementById("mySidenav").style.right = "-220px";
  document.getElementById("black").style.display = "none";
}
function closebtn(){
	document.getElementById("printinfo").style.display = "none";
	document.getElementById("blackback").style.display = "none";
}
function printinfoview(){
	document.getElementById("printinfo").style.display = "inline";
	document.getElementById("blackback").style.display = "inline";
}
function openCloseToc(){
   if(document.getElementById("toc-content").style.visibility === "visible"){
       document.getElementById("toc-content").style.visibility = "hidden";
       document.getElementById("toc-content").style.opacity = "0";
   } else {
       document.getElementById("toc-content").style.visibility = "visible";
       document.getElementById("toc-content").style.opacity = "1";
   }
}