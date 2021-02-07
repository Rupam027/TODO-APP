
function  confirm()
{
	console.log("INSIDE CONFIRM");
	var pass = document.getElementById("pass").value ; 
	var com  = document.getElementById("com").value ;
	
	if(pass == com){
		document.getElementById("mismatch").innerHTML = "Password did not match" ;
		
	}
	else{
		document.getElementById("mismatch").innerHTML = " " ; 
	}
	
}


