function language(x)
 {
 if (x==0)
 {
 document.getElementById("english").style.display="block";
 document.getElementById("telugu").style.display="none";
 return;
 }
 else
 {
 document.getElementById("english").style.display="none";
 document.getElementById("telugu").style.display="block";
 return;
 }
 }
function text(){
           var status=document.getElementById("typeof");
           if(status.value=="C")
           {
           document.getElementById("mycode").style.visibility="visible";
           }
           else
           {
           document.getElementById("mycode").style.visibility="hidden";
           }
        }
function validdeatils(){
   var status=document.getElementById("typeof");
   var amountfield=document.getElementById("Amount");
   var year=document.getElementById("yea");
   var month=document.getElementById("month");
   var days=document.getElementById("days");
   var inter=document.getElementById("inter");
   var decimal=  /[-+][0-9]+\.[0-9]+$/;
   if(status.value=="N")
           {
           alert("Please select correct type simple or compound")
           return false;
           }
   if(amountfield.value < 1 || amountfield.value =="")
           {
          alert("Please select correct  amount")
          return false;
           }
   if(inter.value=="" || inter.value<0)
           {

          alert("Please select correct  interest rate")
          return false;
           }
   let a = parseInt(inter.value)
   if(!parseInt(inter.value))
     {
      alert('select correct interest ')
      return false;
      }
   if(days.value=="" || month.value =="" || years.value=="" )
           {
          alert("Please select correct  years or days or months")
          return false;
           }
}
function text1(){
           var status=document.getElementById("typeof1");
           if(status.value=="C")
           {
           document.getElementById("mycode1").style.visibility="visible";
           }
           else
           {
           document.getElementById("mycode1").style.visibility="hidden";
           }
        }
function validdeatils1(){
   var status=document.getElementById("typeof1");
   var amountfield=document.getElementById("Amount1");
   var year=document.getElementById("yea1");
   var month=document.getElementById("month1");
   var days=document.getElementById("days1");
   var inter=document.getElementById("inter1");
   var decimal=  /[-+][0-9]+\.[0-9]+$/;
   if(status.value=="N")
           {
           alert("దయచేసి సరైన సమాధానాలను బారు వడ్డి లేదా అంత కట్టు ఎంచుకోండి")
           return false;
           }
   if(amountfield.value < 1 || amountfield.value =="")
           {
          alert("దయచేసి సరైన  అసలు ఈవండి")
          return false;
           }
   if(inter.value=="" || inter.value<0)
           {

          alert("దయచేసి సరైన వడ్డీ రేటును ఎంచుకోండి")
          return false;
           }
   let a = parseInt(inter.value)
   if(!parseInt(inter.value))
     {
      alert('సరైన వడ్డీ ఎంచుకోండి ')
      return false;
      }
   if(days.value=="" || month.value =="" || years.value=="" )
           {
          alert("దయచేసి సరైన సంవత్సరాలు లేదా రోజులు లేదా నెలలను ఎంచుకోండి")
          return false;
           }
}
