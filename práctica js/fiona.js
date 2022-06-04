/*hola esto es un 
comentario
de
varias
líneas */
console.log("Archivo error");
console.log(33);

//tipo de dato booleano
console.log(true);
console.log(false);

//operaciones aritméticas
console.log(4 + 5);
console.log(4 - 2);
console.log(4 * 3);
console.log(45 / 5);
console.log(10 % 2); //me da el resto de la división

console.log("casa" + "auto" + "mate");
console.log("Clark" + "Kent");

//clear() limpia la consola sirve solo en el navegador

/* 
variables: espacio de memoria que puedo almacenar 
(una cajita vacía o llena)
el nombre de la variable no tiene que ser una palabra reservada
*/
var nombre = "Burro";
var numero = 22;
var decimal = 22.5;
var verdad = true;
var falso = false;

console.log(nombre);
console.log(numero);
console.log(decimal);
console.log(verdad);

/*
convención de nombres de variables:
- upper Case: var NOMBRE2 = "Pancho"
- upper Camel Case: var NombreApellido = "Tony Stark"
- lower Camel Case: var equipoFutbol = "Bokita"
- snake Case: var color_favorito = "azul y amarillo"
*/

var nombre = "Gato con Botas";
console.log(nombre);
var nombre = 15;
console.log(nombre);

// constantes: no me permiten cambiar el valor
const PI = 3.141592653589;
console.log("Probando constantes");
console.log(PI);
/*
PI = 2.72985465132;
console.log(PI);
*/

var virus = "Covid-20";
var nombreUsuario = "Miranda Presley";
var password = "incorrecta";
console.log(virus);
/*
alert("Funca");
alert("Pinguinos mafiosos");
alert("Ejecutando virus: " + virus);
alert("El usuario: " + nombreUsuario);
alert("Su contraseña es: " + password);
*/

//prompt pide datos
/*
prompt("Ingrese su nombre: ");
prompt("Ingrese su teléfono: ");
*/
var datoCBU = prompt("Ingrese su CBU: ");
console.log(datoCBU);
alert("Su CBU es: " + datoCBU);
