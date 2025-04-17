
import Nota from "./Midi/nota";
// src/cancion.ts
export class CompacesPartitura {
    notas: Nota[][];

    constructor(notas: Nota [][]) {
        this.notas = notas;
    }
}


export  class PartituraInstrumento {
    compaces: CompacesPartitura[];
    instrumento: string="piano";
    clave: string = "G";
    escala: string = "C";

    
    constructor(instrumento: string, compaces: CompacesPartitura[], clave: string, escala: string) {
        this.escala = escala;
        this.compaces = compaces;
        this.instrumento = instrumento;
        this.clave = clave;
    }
     
}
