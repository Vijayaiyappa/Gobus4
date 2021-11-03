

function show3()

{
  document.getElementById("get").classList.remove("inactive");
  document.getElementById("hid").style.display = "none";

  document.getElementById("get2").classList.remove("inactive");
  document.getElementById("hid2").style.display = "none";
  
  const get1="get3"
  document.getElementById(get1).classList.remove("inactive3");
  const a=document.querySelector("#myTable3");
  const x = a.querySelectorAll("li");
  x.forEach(o => {
    o.addEventListener("click",()=>{

      document.getElementById("myInput3").value =o.innerHTML;
      document.getElementById("hid3").style.display = "none";
    
    })
  });
  document.getElementById("hid3").style.display = "";
  
}





function myFunction3() {
 
  input = document.getElementById("myInput3");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable3");
  tr = table.getElementsByTagName("li");
  for (i = 0; i < tr.length; i++) {
    mytext = tr[i].innerText.toUpperCase()
 
    if (mytext) {
      var len= filter.length;
     
      if(mytext.slice(0,len)==filter)
          {
            tr[i].style.display = "";
          }
      else
         {
          tr[i].style.display = "none";
        
         }

    }
           
  }
}