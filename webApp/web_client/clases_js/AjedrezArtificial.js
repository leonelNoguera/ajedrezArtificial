var lienzoTablero;
var lienzoPiezas;
var canvasPiezas;
// '' is empty.
var piezasArray = new Array(['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '']);
//							 f, c
var clicksTablero = new Array([-1, -1], [-1, -1]);
var clicksPiezas = new Array([-1, -1], [-1, -1]);
var Tablero = /** @class */ (function () {
    function Tablero() {
    }
    Tablero.iniciar = function () {
        //console.log(piezasArray[0]);
        var canvasTablero = document.getElementById('lienzoTablero');
        lienzoTablero = canvasTablero.getContext('2d');
        canvasPiezas = document.getElementById('lienzoPiezas');
        lienzoPiezas = canvasPiezas.getContext('2d');
        /*p23 = new Image();
        p23.src = "imgs/peonBlanco.png";
        lienzoTablero.drawImage(p23,410,300,30,50);*/
        this.dibujarTablero();
        document.getElementById('lienzoTablero').addEventListener('mousedown', function (e) {
            var ClientRect = canvasTablero.getBoundingClientRect();
            Tablero.detectarPieza((e.clientX - ClientRect.left), (e.clientY - ClientRect.top));
        });
        //this.parseResponseToArray();
        //this.colocarPiezas();
        //window.addEventListener("load", this.colocarPiezas, false);
        //this.mover();
    };
    Tablero.marcar = function (f, c, desde) {
        if (desde === void 0) { desde = 'tablero'; }
        if (desde == 'tablero') {
            lienzoTablero.strokeStyle = "#ff0000";
            lienzoTablero.beginPath();
            lienzoTablero.moveTo(5 + (50 * c), 5 + (50 * f));
            lienzoTablero.lineTo(45 + (50 * c), 5 + (50 * f));
            lienzoTablero.lineTo(45 + (50 * c), 45 + (50 * f));
            lienzoTablero.lineTo(5 + (50 * c), 45 + (50 * f));
            lienzoTablero.lineTo(5 + (50 * c), 5 + (50 * f));
            lienzoTablero.stroke();
        }
        else {
            lienzoPiezas.strokeStyle = "#ff0000";
            lienzoPiezas.beginPath();
            lienzoPiezas.moveTo(5 + (50 * c), 5 + (50 * f));
            lienzoPiezas.lineTo(45 + (50 * c), 5 + (50 * f));
            lienzoPiezas.lineTo(45 + (50 * c), 45 + (50 * f));
            lienzoPiezas.lineTo(5 + (50 * c), 45 + (50 * f));
            lienzoPiezas.lineTo(5 + (50 * c), 5 + (50 * f));
            lienzoPiezas.stroke();
        }
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
                    //console.log('p = ' + p + ' - co = ' + co + ' - f = ' + f + ' - c = ' + c);
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
        document.getElementById('lienzoPiezas').addEventListener('mousedown', function (e) {
            var ClientRect = canvasPiezas.getBoundingClientRect();
            Tablero.detectarPieza((e.clientX - ClientRect.left), (e.clientY - ClientRect.top), 'piezas');
        });
        this.dibujarPiezasExtra();
        for (var i = 0; i < 8; i++) {
            for (var j = 0; j < 8; j++) {
                this.colocarPiezas('e', '', i, j);
            }
        }
        this.colocarPiezas('r', 'b', 0, 0);
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
    Tablero.detectarPieza = function (x, y, desde) {
        if (desde === void 0) { desde = 'tablero'; }
        var f = 0;
        var c = 0;
        if ((desde == 'tablero') && (clicksPiezas[0][0] == -1)) {
            var j_1 = 0;
            for (var i = 0; i <= 350; i += 50) {
                if ((y >= i) && (y <= (i + 50))) {
                    var l = 0;
                    for (var k = 0; k <= 350; k += 50) {
                        if ((x >= k) && (x <= (k + 50))) {
                            //console.log(j);
                            //console.log(l);
                            f = j_1;
                            c = l;
                            if (clicksTablero[0][0] == -1) {
                                if (piezasArray[f][c] != 'e') {
                                    clicksTablero[0][0] = f;
                                    clicksTablero[0][1] = c;
                                    this.marcar(f, c);
                                }
                            }
                            else {
                                clicksTablero[1][0] = f;
                                clicksTablero[1][1] = c;
                                this.colocarPiezas(piezasArray[clicksTablero[0][0]][clicksTablero[0][1]][0], piezasArray[clicksTablero[0][0]][clicksTablero[0][1]][1], clicksTablero[1][0], clicksTablero[1][1]);
                                // Limpio la casilla que se desocupó.
                                this.colocarPiezas('', '', clicksTablero[0][0], clicksTablero[0][1]);
                                clicksTablero[0][0] = -1;
                                clicksTablero[0][1] = -1;
                                clicksTablero[1][0] = -1;
                                clicksTablero[1][1] = -1;
                            }
                            break;
                        }
                        l++;
                    }
                }
                j_1++;
            }
        }
        else {
            if (desde == 'piezas') {
                if (clicksPiezas[0][0] == -1) {
                    for (var i = 0; i <= 350; i += 50) {
                        //console.log(i);
                        if ((x >= i) && (x <= (i + 50))) {
                            if ((y >= 0) && (y <= 50)) {
                                f = 0;
                            }
                            else {
                                f = 1;
                            }
                            clicksPiezas[0][0] = f;
                            clicksPiezas[0][1] = c;
                            //console.log(c);
                            this.marcar(f, c, 'piezas');
                        }
                        c++;
                    }
                }
            }
            else {
                if ((desde == 'tablero') && (clicksPiezas[0][0] != -1)) {
                    for (var i = 0; i <= 350; i += 50) {
                        if ((x >= i) && (x <= (i + 50))) {
                            for (var j = 0; j <= 350; j += 50) {
                                if ((y >= j) && (y <= (j + 50))) {
                                    clicksPiezas[1][0] = f;
                                    clicksPiezas[1][1] = c;
                                    var co = 'b';
                                    var p = void 0;
                                    if (clicksPiezas[0][0] == 1) {
                                        co = 'w';
                                    }
                                    switch (clicksPiezas[0][1]) {
                                        case 0:
                                            p = 'r';
                                            break;
                                        case 1:
                                            p = 'n';
                                            break;
                                        case 2:
                                            p = 'b';
                                            break;
                                        case 3:
                                            p = 'q';
                                            break;
                                        case 4:
                                            p = 'k';
                                            break;
                                        case 5:
                                            p = 'p';
                                            break;
                                        default:
                                            break;
                                    }
                                    this.colocarPiezas(p, co, f, c);
                                    this.dibujarPiezasExtra();
                                    clicksPiezas[0][0] = -1;
                                    clicksPiezas[0][1] = -1;
                                    clicksPiezas[1][0] = -1;
                                    clicksPiezas[1][1] = -1;
                                }
                                f++;
                            }
                        }
                        c++;
                    }
                    //this.colocarPiezas(clicksPiezas[1][0], clicksPiezas[1][1], f, c);
                }
            }
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
    };
    Tablero.dibujarPiezasExtra = function () {
        lienzoPiezas.strokeStyle = "#000000";
        for (var x = 0; x <= 250; x += 50) {
            lienzoPiezas.fillStyle = "#ffffff";
            lienzoPiezas.beginPath();
            lienzoPiezas.moveTo(x, 0);
            lienzoPiezas.lineTo((x + 50), 0);
            lienzoPiezas.lineTo((x + 50), 50);
            lienzoPiezas.lineTo(x, 50);
            lienzoPiezas.lineTo(x, 0);
            lienzoPiezas.fill();
            lienzoPiezas.stroke();
            lienzoPiezas.beginPath();
            lienzoPiezas.moveTo(x, 50);
            lienzoPiezas.lineTo((x + 50), 50);
            lienzoPiezas.lineTo((x + 50), 100);
            lienzoPiezas.lineTo(x, 100);
            lienzoPiezas.lineTo(x, 50);
            lienzoPiezas.fill();
            lienzoPiezas.stroke();
        }
        lienzoPiezas.fillStyle = "#000000";
        // root (torre)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo(38, 40);
        lienzoPiezas.lineTo(38, 37);
        lienzoPiezas.lineTo(35, 34);
        lienzoPiezas.lineTo(35, 20);
        lienzoPiezas.lineTo(37, 20);
        lienzoPiezas.lineTo(37, 10);
        lienzoPiezas.lineTo(32, 10);
        lienzoPiezas.lineTo(32, 15);
        lienzoPiezas.lineTo(27, 15);
        lienzoPiezas.lineTo(27, 10);
        lienzoPiezas.lineTo(22, 10);
        lienzoPiezas.lineTo(22, 15);
        lienzoPiezas.lineTo(22, 15);
        lienzoPiezas.lineTo(17, 15);
        lienzoPiezas.lineTo(17, 10);
        lienzoPiezas.lineTo(12, 10);
        lienzoPiezas.lineTo(13, 20);
        lienzoPiezas.lineTo(15, 20);
        lienzoPiezas.lineTo(15, 34);
        lienzoPiezas.lineTo(12, 37);
        lienzoPiezas.lineTo(12, 40);
        lienzoPiezas.lineTo(38, 40);
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        // knight (caballo)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo((35 + 50), 40);
        lienzoPiezas.lineTo((38 + 50), 36);
        lienzoPiezas.lineTo((38 + 50), 26);
        lienzoPiezas.lineTo((35 + 50), 22);
        lienzoPiezas.lineTo((32 + 50), 20);
        lienzoPiezas.lineTo((32 + 50), 14);
        lienzoPiezas.lineTo((29 + 50), 19);
        lienzoPiezas.lineTo((26 + 50), 14);
        lienzoPiezas.lineTo((25 + 50), 20);
        lienzoPiezas.lineTo((17 + 50), 27);
        lienzoPiezas.lineTo((20 + 50), 30);
        lienzoPiezas.lineTo((27 + 50), 26.5);
        lienzoPiezas.lineTo((25 + 50), 32);
        lienzoPiezas.lineTo((15 + 50), 40);
        lienzoPiezas.lineTo((35 + 50), 40);
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        // bishop (alfil)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo((38 + 100), 40);
        lienzoPiezas.lineTo((28 + 100), 30);
        lienzoPiezas.lineTo((28 + 100), 23);
        lienzoPiezas.lineTo((33 + 100), 23);
        lienzoPiezas.lineTo((35 + 100), 14.5);
        lienzoPiezas.lineTo((25 + 100), 6);
        lienzoPiezas.lineTo((16 + 100), 14.5);
        lienzoPiezas.lineTo((18 + 100), 23);
        lienzoPiezas.lineTo((23 + 100), 23);
        lienzoPiezas.lineTo((23 + 100), 30);
        lienzoPiezas.lineTo((13 + 100), 40);
        lienzoPiezas.lineTo((38 + 100), 40);
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        // queen (reina)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo((38 + 150), 40);
        lienzoPiezas.lineTo((28 + 150), 30);
        lienzoPiezas.lineTo((28 + 150), 23);
        lienzoPiezas.lineTo((33 + 150), 23);
        lienzoPiezas.lineTo((35 + 150), 12.5);
        lienzoPiezas.lineTo((32 + 150), 14.5);
        lienzoPiezas.lineTo((25 + 150), 10);
        lienzoPiezas.lineTo((19 + 150), 14.5);
        lienzoPiezas.lineTo((16 + 150), 12.5);
        lienzoPiezas.lineTo((18 + 150), 23);
        lienzoPiezas.lineTo((23 + 150), 23);
        lienzoPiezas.lineTo((23 + 150), 30);
        lienzoPiezas.lineTo((13 + 150), 40);
        lienzoPiezas.lineTo((38 + 150), 40);
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        lienzoPiezas.beginPath();
        lienzoPiezas.arc((25 + 150), 10, 2, 10, Math.PI, true);
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        // king (rey)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo((38 + 200), 40);
        lienzoPiezas.lineTo((28 + 200), 30);
        lienzoPiezas.lineTo((28 + 200), 23);
        lienzoPiezas.lineTo((33 + 200), 23);
        lienzoPiezas.lineTo((35 + 200), 14.5);
        lienzoPiezas.lineTo((27 + 200), 13);
        lienzoPiezas.lineTo((27 + 200), 9);
        lienzoPiezas.lineTo((29 + 200), 9);
        lienzoPiezas.lineTo((29 + 200), 7);
        lienzoPiezas.lineTo((27 + 200), 7);
        lienzoPiezas.lineTo((27 + 200), 5);
        lienzoPiezas.lineTo((25 + 200), 5);
        lienzoPiezas.lineTo((25 + 200), 7);
        lienzoPiezas.lineTo((23 + 200), 7);
        lienzoPiezas.lineTo((23 + 200), 9);
        lienzoPiezas.lineTo((25 + 200), 9);
        lienzoPiezas.lineTo((25 + 200), 13);
        lienzoPiezas.lineTo((16 + 200), 14.5);
        lienzoPiezas.lineTo((18 + 200), 23);
        lienzoPiezas.lineTo((23 + 200), 23);
        lienzoPiezas.lineTo((23 + 200), 30);
        lienzoPiezas.lineTo((13 + 200), 40);
        lienzoPiezas.lineTo((38 + 200), 40);
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        // pawn (peón)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo((38 + 250), 40);
        lienzoPiezas.lineTo((28 + 250), 30);
        lienzoPiezas.lineTo((28 + 250), 20);
        lienzoPiezas.lineTo((23 + 250), 20);
        lienzoPiezas.lineTo((23 + 250), 30);
        lienzoPiezas.lineTo((13 + 250), 40);
        lienzoPiezas.lineTo((38 + 250), 40);
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        lienzoPiezas.beginPath();
        lienzoPiezas.arc((25.5 + 250), 17.5, 7.5, 10, Math.PI, true);
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        lienzoPiezas.fillStyle = "#ffffff";
        // root (torre)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo(38, (40 + 50));
        lienzoPiezas.lineTo(38, (37 + 50));
        lienzoPiezas.lineTo(35, (34 + 50));
        lienzoPiezas.lineTo(35, (20 + 50));
        lienzoPiezas.lineTo(37, (20 + 50));
        lienzoPiezas.lineTo(37, (10 + 50));
        lienzoPiezas.lineTo(32, (10 + 50));
        lienzoPiezas.lineTo(32, (15 + 50));
        lienzoPiezas.lineTo(27, (15 + 50));
        lienzoPiezas.lineTo(27, (10 + 50));
        lienzoPiezas.lineTo(22, (10 + 50));
        lienzoPiezas.lineTo(22, (15 + 50));
        lienzoPiezas.lineTo(22, (15 + 50));
        lienzoPiezas.lineTo(17, (15 + 50));
        lienzoPiezas.lineTo(17, (10 + 50));
        lienzoPiezas.lineTo(12, (10 + 50));
        lienzoPiezas.lineTo(13, (20 + 50));
        lienzoPiezas.lineTo(15, (20 + 50));
        lienzoPiezas.lineTo(15, (34 + 50));
        lienzoPiezas.lineTo(12, (37 + 50));
        lienzoPiezas.lineTo(12, (40 + 50));
        lienzoPiezas.lineTo(38, (40 + 50));
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        // knight (caballo)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo((35 + 50), (40 + 50));
        lienzoPiezas.lineTo((38 + 50), (36 + 50));
        lienzoPiezas.lineTo((38 + 50), (26 + 50));
        lienzoPiezas.lineTo((35 + 50), (22 + 50));
        lienzoPiezas.lineTo((32 + 50), (20 + 50));
        lienzoPiezas.lineTo((32 + 50), (14 + 50));
        lienzoPiezas.lineTo((29 + 50), (19 + 50));
        lienzoPiezas.lineTo((26 + 50), (14 + 50));
        lienzoPiezas.lineTo((25 + 50), (20 + 50));
        lienzoPiezas.lineTo((17 + 50), (27 + 50));
        lienzoPiezas.lineTo((20 + 50), (30 + 50));
        lienzoPiezas.lineTo((27 + 50), (26.5 + 50));
        lienzoPiezas.lineTo((25 + 50), (32 + 50));
        lienzoPiezas.lineTo((15 + 50), (40 + 50));
        lienzoPiezas.lineTo((35 + 50), (40 + 50));
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        // bishop (alfil)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo((38 + 100), (40 + 50));
        lienzoPiezas.lineTo((28 + 100), (30 + 50));
        lienzoPiezas.lineTo((28 + 100), (23 + 50));
        lienzoPiezas.lineTo((33 + 100), (23 + 50));
        lienzoPiezas.lineTo((35 + 100), (14.5 + 50));
        lienzoPiezas.lineTo((25 + 100), (6 + 50));
        lienzoPiezas.lineTo((16 + 100), (14.5 + 50));
        lienzoPiezas.lineTo((18 + 100), (23 + 50));
        lienzoPiezas.lineTo((23 + 100), (23 + 50));
        lienzoPiezas.lineTo((23 + 100), (30 + 50));
        lienzoPiezas.lineTo((13 + 100), (40 + 50));
        lienzoPiezas.lineTo((38 + 100), (40 + 50));
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        // queen (reina)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo((38 + 150), (40 + 50));
        lienzoPiezas.lineTo((28 + 150), (30 + 50));
        lienzoPiezas.lineTo((28 + 150), (23 + 50));
        lienzoPiezas.lineTo((33 + 150), (23 + 50));
        lienzoPiezas.lineTo((35 + 150), (12.5 + 50));
        lienzoPiezas.lineTo((32 + 150), (14.5 + 50));
        lienzoPiezas.lineTo((25 + 150), (10 + 50));
        lienzoPiezas.lineTo((19 + 150), (14.5 + 50));
        lienzoPiezas.lineTo((16 + 150), (12.5 + 50));
        lienzoPiezas.lineTo((18 + 150), (23 + 50));
        lienzoPiezas.lineTo((23 + 150), (23 + 50));
        lienzoPiezas.lineTo((23 + 150), (30 + 50));
        lienzoPiezas.lineTo((13 + 150), (40 + 50));
        lienzoPiezas.lineTo((38 + 150), (40 + 50));
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        lienzoPiezas.beginPath();
        lienzoPiezas.arc((25 + 150), (10 + 50), 2, 10, Math.PI, true);
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        // king (rey)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo((38 + 200), (40 + 50));
        lienzoPiezas.lineTo((28 + 200), (30 + 50));
        lienzoPiezas.lineTo((28 + 200), (23 + 50));
        lienzoPiezas.lineTo((33 + 200), (23 + 50));
        lienzoPiezas.lineTo((35 + 200), (14.5 + 50));
        lienzoPiezas.lineTo((27 + 200), (13 + 50));
        lienzoPiezas.lineTo((27 + 200), (9 + 50));
        lienzoPiezas.lineTo((29 + 200), (9 + 50));
        lienzoPiezas.lineTo((29 + 200), (7 + 50));
        lienzoPiezas.lineTo((27 + 200), (7 + 50));
        lienzoPiezas.lineTo((27 + 200), (5 + 50));
        lienzoPiezas.lineTo((25 + 200), (5 + 50));
        lienzoPiezas.lineTo((25 + 200), (7 + 50));
        lienzoPiezas.lineTo((23 + 200), (7 + 50));
        lienzoPiezas.lineTo((23 + 200), (9 + 50));
        lienzoPiezas.lineTo((25 + 200), (9 + 50));
        lienzoPiezas.lineTo((25 + 200), (13 + 50));
        lienzoPiezas.lineTo((16 + 200), (14.5 + 50));
        lienzoPiezas.lineTo((18 + 200), (23 + 50));
        lienzoPiezas.lineTo((23 + 200), (23 + 50));
        lienzoPiezas.lineTo((23 + 200), (30 + 50));
        lienzoPiezas.lineTo((13 + 200), (40 + 50));
        lienzoPiezas.lineTo((38 + 200), (40 + 50));
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        // pawn (peón)
        lienzoPiezas.beginPath();
        lienzoPiezas.moveTo((38 + 250), (40 + 50));
        lienzoPiezas.lineTo((28 + 250), (30 + 50));
        lienzoPiezas.lineTo((28 + 250), (20 + 50));
        lienzoPiezas.lineTo((23 + 250), (20 + 50));
        lienzoPiezas.lineTo((23 + 250), (30 + 50));
        lienzoPiezas.lineTo((13 + 250), (40 + 50));
        lienzoPiezas.lineTo((38 + 250), (40 + 50));
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
        lienzoPiezas.beginPath();
        lienzoPiezas.arc((25.5 + 250), (17.5 + 50), 7.5, 10, Math.PI, true);
        lienzoPiezas.fill();
        lienzoPiezas.stroke();
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
            case 'e':
                /*if (lienzoTablero.fillStyle == "#000000")
                {
                    lienzoTablero.fillStyle = "#ffffff";
                }*/
                /*lienzoTablero.beginPath();
                lienzoTablero.moveTo(0 + (50 * c), 0 + (50 * f));
                lienzoTablero.lineTo(50 + (50 * c), 0 + (50 * f));
                lienzoTablero.lineTo(50 + (50 * c), 50 + (50 * f));
                lienzoTablero.lineTo(0 + (50 * c), 50 + (50 * f));
                lienzoTablero.lineTo(0 + (50 * c), 0 + (50 * f));
                lienzoTablero.fill();
                lienzoTablero.stroke();*/
                piezasArray[f][c] = 'e';
                break;
        }
    };
    return Tablero;
}());
//import db from 'sqlite';
//db.open('ajedrezArtificial.db')
//.then(() =>)
var posicionLista = 0;
var tableroArray = "";
var QuerySender = /** @class */ (function () {
    function QuerySender() {
    }
    QuerySender.SendQuery = function (comando) {
        //let comando = (<HTMLInputElement>document.getElementById("txtMovimiento")).value;
        if (comando === void 0) { comando = document.getElementById("txtMovimiento").value; }
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
        var xhttp = new XMLHttpRequest();
        xhttp.open("POST", "http://localhost:8080/", true);
        xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
        xhttp.send("comando=" + comando);
        xhttp.onreadystatechange = function () {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                //(<HTMLInputElement>document.getElementById("arrayTablero")).innerHTML = xhttp.responseText;
                Tablero.parseResponseToArray(xhttp.responseText);
                //return xhttp.responseText;
            }
        };
        //alert("...");
    };
    QuerySender.SendMultipleQueryes = function (btn) {
        var lista = new Array();
        var cadena = document.getElementById("listaMovimientos").value;
        var cadenaAux = '';
        var elemento = '';
        var flag = true;
        for (var i = 0; i < cadena.length; i++) {
            if ((cadena[i] == ' ') && (cadena[i + 1] == '<') && (cadena[i + 2] == '-') && (cadena[i + 3] == '-')) {
                i += 3;
            }
            else {
                cadenaAux += cadena[i];
            }
        }
        //cadena = cadenaAux;
        for (var i = 0; i < cadenaAux.length; i++) {
            if (cadenaAux[i] != '\n') {
                elemento += cadenaAux[i];
            }
            else {
                lista.push(elemento);
                elemento = '';
            }
            if (i == (cadenaAux.length - 1)) {
                if (elemento != '') {
                    lista.push(elemento);
                }
                elemento = '';
            }
        }
        //console.log('La lista de comandos obtenida es: ' + lista);
        if (btn == 'init') {
            //console.log(cadenaAux);
            posicionLista = 0;
            this.SendQuery(lista[0]);
            cadena = '';
            for (var i = 0; i < cadenaAux.length; i++) {
                if ((cadenaAux[i] == '\n') && (flag)) {
                    cadena += ' <--\n';
                    flag = false;
                }
                else {
                    cadena += cadenaAux[i];
                }
            }
            document.getElementById("listaMovimientos").value = cadena;
        }
        else {
            if (btn == 'siguiente') {
                posicionLista++;
                //console.log('posicionLista == ' + posicionLista);
                this.SendQuery(lista[posicionLista]);
                flag = false;
                cadenaAux = '';
                // cadena:
                /*init
                a4 <--
                b5*/
                for (var i = 0; i < cadena.length; i++) {
                    if ((cadena[i] == ' ') && (cadena[i + 1] == '<') && (cadena[i + 2] == '-') && (cadena[i + 3] == '-')) {
                        i += 4;
                        cadenaAux += '\n';
                        flag = true;
                    }
                    else {
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
                        if ((((i + 1) == cadena.length) || (cadena[i] == '\n')) && (flag)) {
                            if ((i + 1) == cadena.length) {
                                cadenaAux += cadena[i] + ' <--';
                            }
                            else {
                                cadenaAux += ' <--\n';
                            }
                            flag = false;
                            //alert(cadenaAux);
                        }
                        else {
                            cadenaAux += cadena[i];
                        }
                    }
                }
                document.getElementById("listaMovimientos").value = cadenaAux;
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
    };
    return QuerySender;
}());
