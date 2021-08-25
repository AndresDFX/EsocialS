function ShowHideDiv() {
    var cambiarTrabajo = document.getElementById("pay_contract_no");
    var myDIV = document.getElementById("myDIV");
    myDIV.style.display = cambiarTrabajo.checked ? "block" : "none";
  }