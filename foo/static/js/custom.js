$(document).ready(function() {
    $("#id_Date_Discovered").datepicker({changeYear: true, changeMonth:true, dateFormat: 'yy-mm-dd'});
    $("#id_AC_OPEN_DATE").datepicker({changeYear: true, changeMonth:true, dateFormat: 'yy-mm-dd'});
    $("#id_ONBOARDING_DATE").datepicker({changeYear: true, changeMonth:true, dateFormat: 'yy-mm-dd'});
})

document.getElementById('id_Loss_prevented_LCY').addEventListener('input', function(e){
    let naira = e.target.value;
    let pp =document.getElementById('id_Loss_prevented_USD').value
    var rate = document.getElementById('id_LCY_USD_RATE').value;
    
    var convert = parseFloat(naira) / parseFloat(rate)
    
    document.getElementById('id_Loss_prevented_USD').value = convert.toFixed(3)
    document.getElementById('id_Amount_Involved_LCY').value = naira
  })

