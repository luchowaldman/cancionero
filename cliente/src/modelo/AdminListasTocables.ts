import { Almacenado } from "./Almacenado";
import { item_lista } from "./item_lista";


export class AdminListasTocables  {
    private url: string;
    public items_lista: item_lista[] = [];

    constructor(url: string) {
        this.url = url;
        this.initialize();
    }

    private async initialize() {
        this.items_lista = await this.getIndice();
    }
    async getIndice(): Promise<item_lista[]> {
        console.log("Busca indice", this.url + `/indice.json`);
        const response = await fetch(this.url + `/indice.json`);
        const data = await response.json();
        let items_lista = []
        for (let i = 0; i < data.length; i++) {
            items_lista.push(new item_lista(data[i].cancion, data[i].banda, data[i].total_partes, data[i].total_orden_partes));
        }
        return items_lista;

    }

    GetCancion(banda: string, cancion: string): string {
        // Implementación específica para GeneradorListasURL
        return `https://example.com/${banda}/${cancion}`; // Ejemplo de retorno, reemplazar con lógica real
    }
}


