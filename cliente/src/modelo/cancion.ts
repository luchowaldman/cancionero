import { Acordes } from "./acordes";
import { Letra } from "./letra";

// src/cancion.ts
export class Cancion {
    
    constructor(
        public titulo: string,
        public artista: string,
        public acordes: Acordes,
        public letra: Letra
    ) {}
}
