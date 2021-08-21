function ShowHideDiv() {
    var cambiarTrabajo = document.getElementById("cambiar_trabajo_yes");
    var myDIV = document.getElementById("myDIV");
    myDIV.style.display = cambiarTrabajo.checked ? "block" : "none";
  }