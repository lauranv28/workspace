<?php
    header('Content-Type: application/json');
    $obj = array('experiencia' => [['empresa' => 'Microsoft', 'antiguedad' => 5], ['empresa' => 'Google', 'antiguedad' => 3]])
    $datos = array('nombre' => 'Laura', 'apellido' => 'Vargas');
    echo json_encode($obj);
?>