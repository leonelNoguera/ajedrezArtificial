//import db from 'sqlite';

//db.open('ajedrezArtificial.db')
	//.then(() =>)
let tableroArray = "";
class QuerySender
{
	public static SendQuery()
	{
		let comando = (<HTMLInputElement>document.getElementById("txtMovimiento")).value;

		let xhttp : XMLHttpRequest = new XMLHttpRequest();
        xhttp.open("POST", "http://localhost:8080/", true);
        xhttp.setRequestHeader("content-type","application/x-www-form-urlencoded");
        xhttp.send("comando=" + comando);

        xhttp.onreadystatechange = () =>
		{
			if (xhttp.readyState == 4 && xhttp.status == 200)
			{
				//(<HTMLInputElement>document.getElementById("arrayTablero")).innerHTML = xhttp.responseText;

				Tablero.parseResponseToArray(xhttp.responseText);
				//return xhttp.responseText;
			}
		}
		//alert("...");
	}

	public static SendMultipleQueryes()
	{
		let lista = new Array();
		let cadena = (<HTMLInputElement>document.getElementById("listaMovimientos")).value;
		let elemento : string = '';
		
		for (var i = 0; i < cadena.length; i++)
		{
			if (cadena[i] != '\n')
			{
				elemento += cadena[i];
			}
			else
			{
				lista.push(elemento);
				elemento = '';
			}
			if (i == (cadena.length - 1)) {
                lista.push(elemento);
                elemento = '';
            }
		}
		console.log(lista);

		/*let xhttp : XMLHttpRequest = new XMLHttpRequest();
        xhttp.open("POST", "http://localhost:8080/", true);
        xhttp.setRequestHeader("content-type","application/x-www-form-urlencoded");
        xhttp.send("comando=" + comando);

        xhttp.onreadystatechange = () =>
		{
			if (xhttp.readyState == 4 && xhttp.status == 200)
			{
				//(<HTMLInputElement>document.getElementById("arrayTablero")).innerHTML = xhttp.responseText;

				Tablero.parseResponseToArray(xhttp.responseText);
				//return xhttp.responseText;
			}
		}*/
	}
}