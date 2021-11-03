

function show()
{
  document.getElementById("get2").classList.remove("inactive");
  document.getElementById("hid2").style.display = "none";

 
  test=document.getElementById("get").classList.remove("inactive");
  
 
  const a=document.querySelector("#myTable");
  const x = a.querySelectorAll("li");
  x.forEach(o => {
    o.addEventListener("click",()=>{
      
      document.getElementById("myInput").value =o.innerHTML;
      document.getElementById("hid").style.display = "none";
    
    })
  });
  document.getElementById("hid").style.display = "";

}







function myFunction() {
 
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
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