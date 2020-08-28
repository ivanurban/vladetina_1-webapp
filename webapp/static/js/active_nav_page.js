
//VERSION THAT SUPPORTS SUBLINKS
function setActive() {
  // aObj = document.getElementById('active_nav').getElementsByTagName('a');
 
  let last='';
  aObj = document.getElementById('active_nav').getElementsByTagName('a');

  console.log(aObj)

	  for(i=0;i<aObj.length;i++) { 
		    if(document.location.href.indexOf(aObj[i].href)>=0) {
		      
		      last = aObj[i];
		  
			 }		
	   }

   last.className = 'active';	 	  
}


window.onload = setActive;


//VERSION THAT DOES NOT SUPPORT SUBLINKS
// function setActive() {
//   // aObj = document.getElementById('active_nav').getElementsByTagName('a');
 
 
//   aObj = document.getElementById('active_nav').getElementsByTagName('a');

//   console.log(aObj)

// 	  for(i=0;i<aObj.length;i++) { 
// 		    if(document.location.href.indexOf(aObj[i].href)>=0) {
		      
// 		      aObj[i].className = 'active';
		  
// 			 }		
// 	   }

   	  
// }


// window.onload = setActive;
