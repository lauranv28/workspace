async function obtenerDatos() {
  const response = await fetch("http://127.0.0.1:5500/datos.json");
  const json = await response.json();

  console.log(json);
  //console.log(JSON.parse(json));
  // console.log(JSON.stringify(json));
  console.log(json.nombre);
  console.log(json.direccion.colonia);
  console.log(json.experiencia);

  json.experiencia.forEach((elemento) => {
    console.log(elemento.empresa);
  });

  console.log(json.direccion.pagoAgua);
  console.log(json.direccion["pagoAgua"]);
  console.log(json["direccion"]["colonia"]);
}

obtenerDatos();
