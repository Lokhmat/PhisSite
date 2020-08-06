function try_task(b)
{
	//alert(a);
	
	//document.getElementById('result').innerHTML = str(a);
	var ans_p = {
		get ans(){
			return document.getElementById('answer').value
		}

	}

	var ans_g = b;
	ans_g = ans_g.slice(15);
	ans_g = ans_g.slice(0,-18);
	
	
		if (ans_p.ans == ans_g ){
			
			document.getElementById('result').innerHTML = "Правильно, молодец!";
			
			
			document.getElementByClass('lol').click();
			
			document.querySelector("lol").click();
			//var but = document.getElementById("lol");
			//but.submit();
		}
		else{
			
			document.getElementById('result').innerHTML = "Неправильно!";
			document.writeline('<p>Hq</p>');
			
		}
		
}

function keks(){
	alert('Оно работает!!!!11!!1!1 ахахахахыщфлвафцоп');
}