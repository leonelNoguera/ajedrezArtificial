//import db from 'sqlite';
//db.open('ajedrezArtificial.db')
//.then(() =>)
var tableroArray = "";
var AjedrezArtificial;
(function (AjedrezArtificial) {
    var QuerySender = /** @class */ (function () {
        function QuerySender() {
        }
        QuerySender.SendQuery = function () {
            var comando = document.getElementById("txtMovimiento").value;
            var xhttp = new XMLHttpRequest();
            xhttp.open("POST", "http://localhost:8080/", true);
            xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
            xhttp.send("comando=" + comando);
            xhttp.onreadystatechange = function () {
                if (xhttp.readyState == 4 && xhttp.status == 200) {
                    document.getElementById("arrayTablero").innerHTML = xhttp.responseText;
                    Tablero.parseResponseToArray(xhttp.responseText);
                    //return xhttp.responseText;
                }
            };
            //alert("...");
        };
        return QuerySender;
    }());
    AjedrezArtificial.QuerySender = QuerySender;
})(AjedrezArtificial || (AjedrezArtificial = {}));
