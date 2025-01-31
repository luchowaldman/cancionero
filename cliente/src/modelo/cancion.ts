import { Acordes } from "./acordes";
import { Letra } from "./letra";

// src/cancion.ts
export class Cancion {
    
    constructor(
        public cancion: string,
        public banda: string,
        public acordes: Acordes = new Acordes([], []),
        public letras: Letra =  new Letra([]),
        public tempo: number = 12,
        public calidad: number = 0,
        public compas_cantidad: number = 4,
        public compas_unidad: number = 4,
        public escala: string = ""
    ){}

}
