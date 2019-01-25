//import db from 'sqlite';

//db.open('ajedrezArtificial.db')
	//.then(() =>)
let posicionLista : number = 0;
let tableroArray = "";

class QuerySender
{
	public static EjemploMultipleQueryes()
	{
		(<HTMLInputElement>document.getElementById("listaMovimientos")).value = 'init\na4\nb5\nNf3\nBa6\ne3\nbxa4\nRxa4\nBxf1\nKxf1\nNf6\nNe5\nNc6\nc4\nh5\nf4\nh4\nc5\nRh5\nQxh5';
	}

	public static SendQuery(comando = (<HTMLInputElement>document.getElementById("txtMovimiento")).value)
	{
		//let comando = (<HTMLInputElement>document.getElementById("txtMovimiento")).value;

        /*if (comando == 'init')
        {
        	for (var i = 0; i < 8; i++)
			{
				for (var j = 0; j < 8; j++)
				{
					Tablero.colocarPiezas('e', '', i, j);
				}
			}
        }*/

        console.log('Comando recibido en SendQuery(): ' + comando);

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

	public static SendMultipleQueryes(btn : string)
	{
		let lista = new Array();
		let cadena = (<HTMLInputElement>document.getElementById("listaMovimientos")).value;
		let cadenaAux : string = '';
		let elemento : string = '';
		let flag = true;
		
		for (var i = 0; i < cadena.length; i++)
		{
			if ((cadena[i] == ' ') && (cadena[i+1] == '<') && (cadena[i+2] == '-') && (cadena[i+3] == '-'))
			{
				i += 3;
			}
			else
			{
				cadenaAux += cadena[i];
			}
		}

		//cadena = cadenaAux;

		for (var i = 0; i < cadenaAux.length; i++)
		{
			if (cadenaAux[i] != '\n')
			{
				elemento += cadenaAux[i];
			}
			else
			{
				lista.push(elemento);
				elemento = '';
			}
			if (i == (cadenaAux.length - 1))
			{
				if (elemento != '')
				{
                	lista.push(elemento);
				}
                elemento = '';
            }
		}
		
		//console.log('La lista de comandos obtenida es: ' + lista);

		if (btn == 'init')
		{
			//console.log(cadenaAux);
			posicionLista = 0;
			
			this.SendQuery(lista[0]);
			cadena = '';

			for (var i = 0; i < cadenaAux.length; i++)
			{
				if ((cadenaAux[i] == '\n') && (flag))
				{
					cadena += ' <--\n';
					flag = false;
				}
				else
				{
					cadena += cadenaAux[i];
				}
			}

			(<HTMLInputElement>document.getElementById("listaMovimientos")).value = cadena;
		}
		else
		{
			if (btn == 'siguiente')
			{
				posicionLista++;
				
				//console.log('posicionLista == ' + posicionLista);
				
				this.SendQuery(lista[posicionLista]);
				flag = false;
				cadenaAux = '';

				// cadena:
				/*init
				a4 <--
				b5*/
				for (var i = 0; i < cadena.length; i++)
				{
					if ((cadena[i] == ' ') && (cadena[i+1] == '<') && (cadena[i+2] == '-') && (cadena[i+3] == '-'))
					{
						i += 4;
						cadenaAux += '\n';
						flag = true;
					}
					else
					{
						/*if (flag)
						{
							if (cadena[i] == '\n')
							{
								cadenaAux += ' <--\n';
							}
							else
							{
								if ((i + 1) == cadena.length)
								{
									cadenaAux += ' <--';
								}
							}
							flag = false;
							alert(cadenaAux);
						}
						else
						{
							cadenaAux += cadena[i];
						}*/
						if ((((i + 1) == cadena.length) || (cadena[i] == '\n')) && (flag))
						{
							if ((i + 1) == cadena.length)
							{
								cadenaAux += cadena[i] + ' <--';
							}
							else
							{
								cadenaAux += ' <--\n'
							}
							flag = false;
							//alert(cadenaAux);
						}
						else
						{
							cadenaAux += cadena[i];
						}
					}
				}

				(<HTMLInputElement>document.getElementById("listaMovimientos")).value = cadenaAux;
			}
		}

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