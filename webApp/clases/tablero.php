<?php
class Tablero
{
	private $_matrizTablero;

	public function LoadTablero($url = "../tablero.txt")
	{
		//$retorno = "";
		try
		{
			$f = fopen($url, 'r');
			//fread($f, 10);
			$retorno = fgets($f);
		
			for ($i=0; $i < strlen($retorno); $i++)
			{
				echo $retorno[$i];
			}

		}
		catch(Exception $e)
		{
			echo "Error al intentar leer el archivo.";
		}


		//fread(handle, length)

		return $retorno;
	}

	function __construct()
	{
		$this->LoadTablero();
	}
}

$i = new Tablero();

//$i->StartTest();
?>
<textarea id="texto"></textarea>
<canvas id="lienzoTablero" width="500" height="500">
	<script src="clases/tableroOld.js">
	</script>
</canvas>