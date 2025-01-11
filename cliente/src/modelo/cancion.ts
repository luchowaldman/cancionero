import { Acordes } from "./acordes";
import { Letra } from "./letra";

// src/cancion.ts
export class Cancion {
    
    constructor(
        public cancion: string,
        public banda: string,
        public acordes: Acordes,
        public letra: Letra,
        public tempo: number = 60,
        public calidad: number = 0,
        public compas_cantidad: number = 4,
        public compas_unidad: number = 4
    ){}

    public getDuracionCompas(): number {
        return 60 / this.tempo;
    }
}
