import { NotasCancion } from "./NotasCancion";
import { Acordes } from "./acordes";
import { Letra } from "./letra";

// src/cancion.ts
export class Cancion {
    normalizar() {
        const acordes = this.acordes.GetTotalAcordes();
        const letras = this.letras.renglones.flat.length;
        if (letras < acordes) {
            this.letras.renglones.push(new Array(acordes - letras).fill(""));
        }
    }
    
    constructor(
        public cancion: string,
        public banda: string,
        public acordes: Acordes = new Acordes([], []),
        public letras: Letra =  new Letra([]),
        public bpm: number = 67,
        public calidad: number = 0,
        public compas_cantidad: number = 4,
        public compas_unidad: number = 4,
        public escala: string = "",
        public notas_cancion: NotasCancion[][] = []
    ){}

}
