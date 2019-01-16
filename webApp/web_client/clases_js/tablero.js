var lienzoTablero;
// '' is empty.
var piezasArray = new Array(['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '']);
//							 f, c
var clicksArray = new Array([-1, -1], [-1, -1]);
var Tablero = /** @class */ (function () {
    function Tablero() {
    }
    Tablero.iniciar = function () {
        //console.log(piezasArray[0]);
        var canvas = document.getElementById('lienzoTablero');
        lienzoTablero = canvas.getContext('2d');
        /*p23 = new Image();
        p23.src = "imgs/peonBlanco.png";
        lienzoTablero.drawImage(p23,410,300,30,50);*/
        this.dibujarTablero();
        document.getElementById('lienzoTablero').addEventListener('mousedown', function (e) {
            var ClientRect = canvas.getBoundingClientRect();
            Tablero.detectarPieza((e.clientX - ClientRect.left), (e.clientY - ClientRect.top));
        });
        //this.parseResponseToArray();
        //this.colocarPiezas();
        //window.addEventListener("load", this.colocarPiezas, false);
        //this.mover();
    };
    Tablero.marcar = function (f, c) {
        lienzoTablero.strokeStyle = "#ff0000";
        lienzoTablero.beginPath();
        lienzoTablero.moveTo(5 + (50 * c), 5 + (50 * f));
        lienzoTablero.lineTo(45 + (50 * c), 5 + (50 * f));
        lienzoTablero.lineTo(45 + (50 * c), 45 + (50 * f));
        lienzoTablero.lineTo(5 + (50 * c), 45 + (50 * f));
        lienzoTablero.lineTo(5 + (50 * c), 5 + (50 * f));
        lienzoTablero.stroke();
    };
    Tablero.mostrarArray = function () {
        for (var i = 0; i < piezasArray.length; i++) {
            console.log(piezasArray[i]);
        }
    };
    // Transforma la cadena recibida de la API en el array de piezas:
    Tablero.parseResponseToArray = function (response) {
        //let response : string = (<HTMLInputElement>document.getElementById("arrayTablero")).innerHTML;
        //(p : string, co : string, f : number, c : number)
        //[[Rb, Nb, Bb, Qb, Kb, Bb, Nb, Rb], [Pb, Pb, Pb, Pb, Pb, Pb, Pb, Pb], [ , , , , , , , ], [ , , , , , , , ], [ , , , , , , , ], [ , , , , , , , ], [Pw, Pw, Pw, Pw, Pw, Pw, Pw, Pw], [Rw, Nw, Bw, Qw, Kw, Bw, Nw, Rw]]
        var p = '';
        var co = '';
        var f = 0;
        var c = 0;
        //console.log(response);
        for (var i = 2; i < response.length; i++) {
            //console.log('p = ' + p + ', co = ' + co + ', f = ' + f + ', c = ' + c);
            if (f <= 7) {
                if (c <= 7) {
                    //console.log('f = ' + f + ', c = ' + c);
                    console.log('i = ' + i);
                    switch (response[i]) {
                        case 'R':
                            p = 'r';
                            break;
                        case 'N':
                            p = 'n';
                            break;
                        case 'B':
                            p = 'b';
                            break;
                        case 'Q':
                            p = 'q';
                            break;
                        case 'K':
                            p = 'k';
                            break;
                        case 'P':
                            if (i == 146) {
                                console.log('Line: 95');
                            }
                            p = 'p';
                            break;
                        case ' ':
                            p = '';
                            break;
                    }
                    if (p != '') {
                        co = response[i + 1];
                    }
                    else {
                        co = '';
                    }
                    i += 3;
                    console.log('p = ' + p + ' - co = ' + co + ' - f = ' + f + ' - c = ' + c);
                    this.colocarPiezas(p, co, f, c);
                    c++;
                }
                else {
                    if (p == '') {
                        co = '';
                    }
                    i += 1;
                    f++;
                    c = 0;
                }
            }
            else {
                break;
            }
        }
    };
    Tablero.juegoLibre = function () {
        /*for (var i = 0; i < 8; i++)
        {
            for (var j = 0; j < 8; j++)
            {
                this.colocarPiezas('e', '', i, j);
            }
        }*/
        //this.colocarPiezas('r', 'b', 0, 0);
        this.colocarPiezas('n', 'b', 0, 1);
        this.colocarPiezas('b', 'b', 0, 2);
        this.colocarPiezas('q', 'b', 0, 3);
        this.colocarPiezas('k', 'b', 0, 4);
        this.colocarPiezas('b', 'b', 0, 5);
        this.colocarPiezas('n', 'b', 0, 6);
        this.colocarPiezas('r', 'b', 0, 7);
        this.colocarPiezas('p', 'b', 1, 0);
        this.colocarPiezas('p', 'b', 1, 1);
        this.colocarPiezas('p', 'b', 1, 2);
        this.colocarPiezas('p', 'b', 1, 3);
        this.colocarPiezas('p', 'b', 1, 4);
        this.colocarPiezas('p', 'b', 1, 5);
        this.colocarPiezas('p', 'b', 1, 6);
        this.colocarPiezas('p', 'b', 1, 7);
        this.colocarPiezas('r', 'w', 7, 0);
        this.colocarPiezas('n', 'w', 7, 1);
        this.colocarPiezas('b', 'w', 7, 2);
        this.colocarPiezas('k', 'w', 7, 3);
        this.colocarPiezas('q', 'w', 7, 4);
        this.colocarPiezas('b', 'w', 7, 5);
        this.colocarPiezas('n', 'w', 7, 6);
        this.colocarPiezas('r', 'w', 7, 7);
        this.colocarPiezas('p', 'w', 6, 0);
        this.colocarPiezas('p', 'w', 6, 1);
        this.colocarPiezas('p', 'w', 6, 2);
        this.colocarPiezas('p', 'w', 6, 3);
        this.colocarPiezas('p', 'w', 6, 4);
        this.colocarPiezas('p', 'w', 6, 5);
        this.colocarPiezas('p', 'w', 6, 6);
        this.colocarPiezas('p', 'w', 6, 7);
    };
    Tablero.detectarPieza = function (x, y) {
        var j = 0;
        var f;
        var c;
        for (var i = 0; i <= 350; i += 50) {
            if ((y >= i) && (y <= (i + 50))) {
                var l = 0;
                for (var k = 0; k <= 350; k += 50) {
                    if ((x >= k) && (x <= (k + 50))) {
                        //console.log(j);
                        //console.log(l);
                        f = j;
                        c = l;
                        if (clicksArray[0][0] == -1) {
                            if (piezasArray[f][c] != 'e') {
                                clicksArray[0][0] = f;
                                clicksArray[0][1] = c;
                                this.marcar(f, c);
                            }
                        }
                        else {
                            clicksArray[1][0] = f;
                            clicksArray[1][1] = c;
                            this.colocarPiezas(piezasArray[clicksArray[0][0]][clicksArray[0][1]][0], piezasArray[clicksArray[0][0]][clicksArray[0][1]][1], clicksArray[1][0], clicksArray[1][1]);
                            // Limpio la casilla que se desocupó.
                            this.colocarPiezas('', '', clicksArray[0][0], clicksArray[0][1]);
                            clicksArray[0][0] = -1;
                            clicksArray[0][1] = -1;
                            clicksArray[1][0] = -1;
                            clicksArray[1][1] = -1;
                        }
                        break;
                    }
                    l++;
                }
            }
            j++;
        }
    };
    Tablero.mover = function () {
        /*[[Rb, Nb, Bb, Qb, Kb, Bb, Nb, Rb], [Pb, Pb, Pb, Pb, Pb, Pb, Pb, Pb], [  ,   ,   ,   ,   ,   ,   ,   ], [  ,   ,   ,   ,   ,   ,   ,   ], [  ,   ,   ,   ,   ,   ,   ,   ], [  ,   ,   ,   ,   ,   ,   ,   ], [Pw, Pw, Pw, Pw, Pw, Pw, Pw, Pw], [Rw, Nw, Bw, Qw, Kw, Bw, Nw, Rw]]*/
        /*let a = new Array();
        a[0][0].toInt();
        a[0][0] = "1";*/
        var p = document.getElementById("txtPieza").value;
        var co = document.getElementById("txtColor").value;
        var f = Number(document.getElementById("txtFila").value);
        var c = Number(document.getElementById("txtColumna").value);
        this.colocarPiezas(p, co, f, c);
        //[fila][columna]
        //[][]
        //lienzoTablero.translate(300, 300);
        /*lienzoTablero.beginPath();
        lienzoTablero.moveTo(110,70);
        lienzoTablero.lineTo(120,70);
        lienzoTablero.lineTo(140,80);
        lienzoTablero.fill();*/
    };
    Tablero.dibujarTablero = function () {
        lienzoTablero.strokeStyle = "#000000";
        for (var x = 0; x <= 300; x += 100) {
            for (var y = 0; y <= 300; y += 100) {
                lienzoTablero.fillStyle = "#ffffff";
                lienzoTablero.beginPath();
                lienzoTablero.moveTo(x, y);
                lienzoTablero.lineTo((x + 50), y);
                lienzoTablero.lineTo(x + 50, y + 50);
                lienzoTablero.lineTo(x, y + 50);
                lienzoTablero.lineTo(x, y);
                lienzoTablero.fill();
                lienzoTablero.stroke();
                lienzoTablero.fillStyle = "#000000";
                lienzoTablero.beginPath();
                lienzoTablero.moveTo(x, y + 50);
                lienzoTablero.lineTo((x + 50), y + 50);
                lienzoTablero.lineTo(x + 50, y + 100);
                lienzoTablero.lineTo(x, y + 100);
                lienzoTablero.lineTo(x, y + 50);
                lienzoTablero.fill();
                lienzoTablero.stroke();
                lienzoTablero.fillStyle = "#000000";
                lienzoTablero.beginPath();
                lienzoTablero.moveTo(x + 50, y);
                lienzoTablero.lineTo((x + 100), y);
                lienzoTablero.lineTo(x + 100, y + 50);
                lienzoTablero.lineTo(x + 50, y + 50);
                lienzoTablero.lineTo(x + 50, y);
                lienzoTablero.fill();
                lienzoTablero.stroke();
                lienzoTablero.fillStyle = "#ffffff";
                lienzoTablero.beginPath();
                lienzoTablero.moveTo(x + 50, y + 50);
                lienzoTablero.lineTo((x + 100), y + 50);
                lienzoTablero.lineTo(x + 100, y + 100);
                lienzoTablero.lineTo(x + 50, y + 100);
                lienzoTablero.lineTo(x + 50, y + 50);
                lienzoTablero.fill();
                lienzoTablero.stroke();
            }
        }
        /*lienzoTablero.beginPath();
        lienzoTablero.moveTo(48, 50);
        lienzoTablero.lineTo(38, 40);
        lienzoTablero.lineTo(38, 33);
        lienzoTablero.lineTo(43, 33);
        lienzoTablero.lineTo(45, 22.5);
        lienzoTablero.lineTo(42, 24.5);
        lienzoTablero.lineTo(35, 20);
        lienzoTablero.lineTo(29, 24.5);
        lienzoTablero.lineTo(26, 22.5);
        lienzoTablero.lineTo(28, 33);
        lienzoTablero.lineTo(33, 33);
        lienzoTablero.lineTo(33, 40);
        lienzoTablero.lineTo(23, 50);
        lienzoTablero.lineTo(48, 50);
        lienzoTablero.fill();
        lienzoTablero.stroke();

        lienzoTablero.beginPath();
        lienzoTablero.arc(35,20,2,10,Math.PI, true);
        lienzoTablero.fill();
        lienzoTablero.stroke();*/
    };
    Tablero.colocarPiezas = function (p, co, f, c) {
        //lienzoTablero.beginPath();
        //lienzoTablero.arc(150,150,50,0,Math.PI*2, false);
        //lienzoTablero.stroke();
        //lienzoTablero.lineWidth=10;
        //lienzoTablero.lineCap="round";
        //lienzoTablero.beginPath();
        //lienzoTablero.moveTo(230,150);
        //lienzoTablero.arc(200,150,30,0,Math.PI, false);
        //lienzoTablero.stroke();
        //lienzoTablero.lineWidth=5;
        //lienzoTablero.lineJoin="miter";
        /*lienzoTablero.beginPath();
        lienzoTablero.moveTo(110, 70);
        lienzoTablero.lineTo(120, 70);
        lienzoTablero.lineTo(120, 80);
        lienzoTablero.lineTo(110, 80);
        lienzoTablero.lineTo(110, 70);
        lienzoTablero.fill();
        lienzoTablero.stroke();*/
        //lienzoTablero.lineTo(195,155);
        // Para limpiar un casillero:
        // lienzoTablero.clearRect(180,10,240,60);
        // columna (x) = 0, 100, 200, 300
        // fila (y) = 50, 150, 250, 350
        //lienzoTablero.strokeStyle = "#000000";
        if (!(c % 2)) {
            if (!(f % 2)) {
                lienzoTablero.strokeStyle = "#000000";
                lienzoTablero.fillStyle = "#ffffff";
            }
            if (!((f + 1) % 2)) {
                lienzoTablero.strokeStyle = "#ffffff";
                lienzoTablero.fillStyle = "#000000";
            }
        }
        if (!((c + 1) % 2)) {
            if (!(f % 2)) {
                lienzoTablero.strokeStyle = "#ffffff";
                lienzoTablero.fillStyle = "#000000";
            }
            if (!((f + 1) % 2)) {
                lienzoTablero.strokeStyle = "#000000";
                lienzoTablero.fillStyle = "#ffffff";
            }
        }
        /*if (p == 'n') // nothing (vacío)
        {
            lienzoTablero.beginPath();
            lienzoTablero.moveTo(10 + (50 * c), 10 + (50 * f));
            lienzoTablero.lineTo(60 + (50 * c), 10 + (50 * f));
            lienzoTablero.lineTo(60 + (50 * c), 60 + (50 * f));
            lienzoTablero.lineTo(10 + (50 * c), 60 + (50 * f));
            lienzoTablero.lineTo(10 + (50 * c), 10 + (50 * f));
            lienzoTablero.fill();
            lienzoTablero.stroke();
        }*/
        lienzoTablero.beginPath();
        lienzoTablero.moveTo(0 + (50 * c), 0 + (50 * f));
        lienzoTablero.lineTo(50 + (50 * c), 0 + (50 * f));
        lienzoTablero.lineTo(50 + (50 * c), 50 + (50 * f));
        lienzoTablero.lineTo(0 + (50 * c), 50 + (50 * f));
        lienzoTablero.lineTo(0 + (50 * c), 0 + (50 * f));
        lienzoTablero.fill();
        lienzoTablero.stroke();
        if (co == 'b') {
            lienzoTablero.fillStyle = "#000000";
        }
        if (co == 'w') {
            lienzoTablero.fillStyle = "#ffffff";
        }
        switch (p) {
            case 'p': // pawn (peón)
                lienzoTablero.beginPath();
                lienzoTablero.moveTo(38 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(28 + (50 * c), 30 + (50 * f));
                lienzoTablero.lineTo(28 + (50 * c), 20 + (50 * f));
                lienzoTablero.lineTo(23 + (50 * c), 20 + (50 * f));
                lienzoTablero.lineTo(23 + (50 * c), 30 + (50 * f));
                lienzoTablero.lineTo(13 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(38 + (50 * c), 40 + (50 * f));
                lienzoTablero.fill();
                lienzoTablero.stroke();
                lienzoTablero.beginPath();
                lienzoTablero.arc(25.5 + (50 * c), 17.5 + (50 * f), 7.5, 10, Math.PI, true);
                lienzoTablero.fill();
                lienzoTablero.stroke();
                piezasArray[f][c] = 'p' + co;
                break;
            case 'r': // root (torre)
                lienzoTablero.beginPath();
                lienzoTablero.moveTo(38 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(38 + (50 * c), 37 + (50 * f));
                lienzoTablero.lineTo(35 + (50 * c), 34 + (50 * f));
                lienzoTablero.lineTo(35 + (50 * c), 20 + (50 * f));
                lienzoTablero.lineTo(37 + (50 * c), 20 + (50 * f));
                lienzoTablero.lineTo(37 + (50 * c), 10 + (50 * f));
                lienzoTablero.lineTo(32 + (50 * c), 10 + (50 * f));
                lienzoTablero.lineTo(32 + (50 * c), 15 + (50 * f));
                lienzoTablero.lineTo(27 + (50 * c), 15 + (50 * f));
                lienzoTablero.lineTo(27 + (50 * c), 10 + (50 * f));
                lienzoTablero.lineTo(22 + (50 * c), 10 + (50 * f));
                lienzoTablero.lineTo(22 + (50 * c), 15 + (50 * f));
                lienzoTablero.lineTo(22 + (50 * c), 15 + (50 * f));
                lienzoTablero.lineTo(17 + (50 * c), 15 + (50 * f));
                lienzoTablero.lineTo(17 + (50 * c), 10 + (50 * f));
                lienzoTablero.lineTo(12 + (50 * c), 10 + (50 * f));
                lienzoTablero.lineTo(13 + (50 * c), 20 + (50 * f));
                lienzoTablero.lineTo(15 + (50 * c), 20 + (50 * f));
                lienzoTablero.lineTo(15 + (50 * c), 34 + (50 * f));
                lienzoTablero.lineTo(12 + (50 * c), 37 + (50 * f));
                lienzoTablero.lineTo(12 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(38 + (50 * c), 40 + (50 * f));
                lienzoTablero.fill();
                lienzoTablero.stroke();
                piezasArray[f][c] = 'r' + co;
                break;
            case 'n': // knight (caballo)
                lienzoTablero.beginPath();
                lienzoTablero.moveTo(35 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(38 + (50 * c), 36 + (50 * f));
                lienzoTablero.lineTo(38 + (50 * c), 26 + (50 * f));
                lienzoTablero.lineTo(35 + (50 * c), 22 + (50 * f));
                lienzoTablero.lineTo(32 + (50 * c), 20 + (50 * f));
                lienzoTablero.lineTo(32 + (50 * c), 14 + (50 * f));
                lienzoTablero.lineTo(29 + (50 * c), 19 + (50 * f));
                lienzoTablero.lineTo(26 + (50 * c), 14 + (50 * f));
                lienzoTablero.lineTo(25 + (50 * c), 20 + (50 * f));
                lienzoTablero.lineTo(17 + (50 * c), 27 + (50 * f));
                lienzoTablero.lineTo(20 + (50 * c), 30 + (50 * f));
                lienzoTablero.lineTo(27 + (50 * c), 26.5 + (50 * f));
                lienzoTablero.lineTo(25 + (50 * c), 32 + (50 * f));
                lienzoTablero.lineTo(15 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(35 + (50 * c), 40 + (50 * f));
                lienzoTablero.fill();
                lienzoTablero.stroke();
                piezasArray[f][c] = 'n' + co;
                break;
            case 'b': // bishop (alfil)
                lienzoTablero.beginPath();
                lienzoTablero.moveTo(38 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(28 + (50 * c), 30 + (50 * f));
                lienzoTablero.lineTo(28 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(33 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(35 + (50 * c), 14.5 + (50 * f));
                lienzoTablero.lineTo(25 + (50 * c), 6 + (50 * f));
                lienzoTablero.lineTo(16 + (50 * c), 14.5 + (50 * f));
                lienzoTablero.lineTo(18 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(23 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(23 + (50 * c), 30 + (50 * f));
                lienzoTablero.lineTo(13 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(38 + (50 * c), 40 + (50 * f));
                lienzoTablero.fill();
                lienzoTablero.stroke();
                piezasArray[f][c] = 'b' + co;
                break;
            case 'q': // queen (reina)
                lienzoTablero.beginPath();
                lienzoTablero.moveTo(38 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(28 + (50 * c), 30 + (50 * f));
                lienzoTablero.lineTo(28 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(33 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(35 + (50 * c), 12.5 + (50 * f));
                lienzoTablero.lineTo(32 + (50 * c), 14.5 + (50 * f));
                lienzoTablero.lineTo(25 + (50 * c), 10 + (50 * f));
                lienzoTablero.lineTo(19 + (50 * c), 14.5 + (50 * f));
                lienzoTablero.lineTo(16 + (50 * c), 12.5 + (50 * f));
                lienzoTablero.lineTo(18 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(23 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(23 + (50 * c), 30 + (50 * f));
                lienzoTablero.lineTo(13 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(38 + (50 * c), 40 + (50 * f));
                lienzoTablero.fill();
                lienzoTablero.stroke();
                lienzoTablero.beginPath();
                lienzoTablero.arc(25 + (50 * c), 10 + (50 * f), 2, 10, Math.PI, true);
                lienzoTablero.fill();
                lienzoTablero.stroke();
                piezasArray[f][c] = 'q' + co;
                break;
            case 'k': // king (rey)
                lienzoTablero.beginPath();
                lienzoTablero.moveTo(38 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(28 + (50 * c), 30 + (50 * f));
                lienzoTablero.lineTo(28 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(33 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(35 + (50 * c), 14.5 + (50 * f));
                lienzoTablero.lineTo(27 + (50 * c), 13 + (50 * f));
                lienzoTablero.lineTo(27 + (50 * c), 9 + (50 * f));
                lienzoTablero.lineTo(29 + (50 * c), 9 + (50 * f));
                lienzoTablero.lineTo(29 + (50 * c), 7 + (50 * f));
                lienzoTablero.lineTo(27 + (50 * c), 7 + (50 * f));
                lienzoTablero.lineTo(27 + (50 * c), 5 + (50 * f));
                lienzoTablero.lineTo(25 + (50 * c), 5 + (50 * f));
                lienzoTablero.lineTo(25 + (50 * c), 7 + (50 * f));
                lienzoTablero.lineTo(23 + (50 * c), 7 + (50 * f));
                lienzoTablero.lineTo(23 + (50 * c), 9 + (50 * f));
                lienzoTablero.lineTo(25 + (50 * c), 9 + (50 * f));
                lienzoTablero.lineTo(25 + (50 * c), 13 + (50 * f));
                lienzoTablero.lineTo(16 + (50 * c), 14.5 + (50 * f));
                lienzoTablero.lineTo(18 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(23 + (50 * c), 23 + (50 * f));
                lienzoTablero.lineTo(23 + (50 * c), 30 + (50 * f));
                lienzoTablero.lineTo(13 + (50 * c), 40 + (50 * f));
                lienzoTablero.lineTo(38 + (50 * c), 40 + (50 * f));
                lienzoTablero.fill();
                lienzoTablero.stroke();
                piezasArray[f][c] = 'k' + co;
                break;
            default:
                piezasArray[f][c] = 'e';
                break;
        }
    };
    return Tablero;
}());
