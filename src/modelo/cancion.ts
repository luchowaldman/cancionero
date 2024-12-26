import { Acordes } from "./acordes";

// src/cancion.ts
export class Cancion {
    
    constructor(
        public titulo: string,
        public artista: string,
        public letra: string,
        public acordes: Acordes
    ) {}
}
