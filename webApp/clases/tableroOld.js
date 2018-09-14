function iniciar()
{
	var elemento=document.getElementById('lienzoTablero');
	var w=document.getElementById('texto');
	alert(w.getText);
	lienzoTablero=elemento.getContext('2d');
	
	dibujarTablero(lienzoTablero);
	colocarPiezas();
}

function colocarPiezas()
{
	var p8=new Image();
	p8.src="imgs/peonNegro.png";
	var p9=new Image();
	p9.src="imgs/peonNegro.png";
	var p10=new Image();
	p10.src="imgs/peonNegro.png";
	var p11=new Image();
	p11.src="imgs/peonNegro.png";
	var p12=new Image();
	p12.src="imgs/peonNegro.png";
	var p13=new Image();
	p13.src="imgs/peonNegro.png";
	var p14=new Image();
	p14.src="imgs/peonNegro.png";
	var p15=new Image();
	p15.src="imgs/peonNegro.png";

	var p16=new Image();
	p16.src="imgs/peonBlanco.png";
	var p17=new Image();
	p17.src="imgs/peonBlanco.png";
	var p18=new Image();
	p18.src="imgs/peonBlanco.png";
	var p19=new Image();
	p19.src="imgs/peonBlanco.png";
	var p20=new Image();
	p20.src="imgs/peonBlanco.png";
	var p21=new Image();
	p21.src="imgs/peonBlanco.png";
	var p22=new Image();
	p22.src="imgs/peonBlanco.png";
	var p23=new Image();
	p23.src="imgs/peonBlanco.png";
	
	p8.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p8,60,100,30,50);
	}, false);

	p9.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p9,110,100,30,50);
	}, false);
	p10.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p10,160,100,30,50);
	}, false);
	p11.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p11,210,100,30,50);
	}, false);
	p12.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p12,260,100,30,50);
	}, false);
	p13.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p13,310,100,30,50);
	}, false);
	p14.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p14,360,100,30,50);
	}, false);
	p15.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p15,410,100,30,50);
	}, false);
	
	p16.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p16,60,350,30,50);
	}, false);
	p17.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p17,110,350,30,50);
	}, false);
	p18.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p18,160,350,30,50);
	}, false);
	p19.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p19,210,350,30,50);
	}, false);
	p20.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p20,260,350,30,50);
	}, false);
	p21.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p21,310,350,30,50);
	}, false);
	p22.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p22,360,350,30,50);
	}, false);
	p23.addEventListener("load", function()
	{
		lienzoTablero.drawImage(p23,410,350,30,50);
	}, false);
}

function dibujarTablero(lienzoTablero)
{
	lienzoTablero.fillRect(50,50,400,400);

	for (var i = 50; i < 450; i+=50)
	{
		for (var j = 50; j < 450; j+=50)
		{
			lienzoTablero.strokeRect(i,50,50,j);
			if ((!(i % 100)) && (j % 100))
			{
				lienzoTablero.clearRect((i+1),(j+1),49,49);
			}
			else
			{
				if ((i % 100) && (!(j % 100)))
				{
					lienzoTablero.clearRect((i+1),(j+1),49,49);
				}
			}
		}
	}
}

window.addEventListener("load", iniciar, false);