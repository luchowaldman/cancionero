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
        public calidad: number = 0
    ) {}
}
