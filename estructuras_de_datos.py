#Tipos de datos  en python
from ast import Str
from os import setsid
from socket import TIPC_CONN_TIMEOUT
from tkinter import BooleanVar
from typing import Dict, List, Set, Tuple
from xmlrpc.client import Boolean

NOMBRE              TIPO    EJEMPLO
Enteros             int     3   500 10000
Punto Flotante      float   3.0 500.78  53.486
Cadenas de Texto    Str     "hola" 'hola' '20.000'
Listas              List    [10,"hola",20.5,"hombre"]
Diccionarios        Dict    {"palabra":"significado","clave":"valor"}
Tuplas              tuple   (10, 'hola', 200.4) #Orden inmutable de Objetos, no se editan
Sets                Set     {"a","b"} #Colección de objetos no ordenados, 
Booleanos           Bool    True False 