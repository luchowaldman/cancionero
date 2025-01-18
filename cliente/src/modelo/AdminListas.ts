import { Almacenado } from "./Almacenado";
import { Cancion } from "./cancion";
import { item_lista } from "./item_lista";


export class AdminiListas  {

    constructor() {
    }

    async getIndice(): Promise<item_lista[]> {
        return [];
    }


    GetCancionxTema(banda: string, cancion: string): Promise<Cancion>  {
        // Implementación específica para GeneradorListasURL
        throw new Error("Method not implemented.");
    }
}
