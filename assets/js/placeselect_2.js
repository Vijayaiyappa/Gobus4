


function show2()
{  
  
  document.getElementById("get").classList.remove("inactive");
  document.getElementById("hid").style.display = "none";

  
  document.getElementById("hid2").style.display = ""; 
  document.getElementById("get2").classList.remove("inactive2");
  const a=document.querySelector("#myTable2");
  const x = a.querySelectorAll("li");

  
  x.forEach(o => {
    o.addEventListener("click",()=>{

      document.getElementById("myInput2").value =o.innerHTML;
      document.getElementById("hid2").style.display = "none";
    
    })
  });
  document.getElementById("hid2").style.display = "";
  
}


function myFunction2() {
 
  input = document.getElementById("myInput2");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable2");
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