function checkname(){ 

var pattern = new RegExp('^[A - Z][a - z]{3 - 7}[0 - 9]{0 - 5}$') ;

var name = document.getElementById('user').value ; 
if(pattern.test(name))
document.getElementById("error").innerHTML = '' ; 
else
document.getElementById("error").innerHTML = "Username invalid" ;


}



function confirm(){
	
	
	var pass = document.getElementById('pass').value ; 
	var con = document.getElementById('com').value ; 
	if(pass == con)
	document.getElementById("mismatch").innerHTML = '' ; 
    else
    document.getElementById("mismatch").innerHTML = "Password did not match" ;
	
}

