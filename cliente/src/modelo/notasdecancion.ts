
import { Nota } from "./Midi/nota";
// src/cancion.ts
export class NotasParteCancion {
    nombre: string;
    notas: Nota[][];

    constructor(nombre: string, notas: Nota []) {
        this.nombre = nombre;
        this.notas = notas;
    }
}


export  class NotasCancion {
    partes: NotasParteCancion[];
    instrumento: string="";
    clave: string = "G";

    constructor(instrumento: string, partes: NotasParteCancion[], clave: string) {
        this.partes = partes;
        this.instrumento = instrumento;
        this.clave = clave;
    }
     
}
