import { Acordes, Parte } from "./acordes";
import { Almacenado } from "./Almacenado";
import { Cancion } from "./cancion";
import { item_lista } from "./item_lista";
import { Letra } from "./letra";


export class AdminListasURL  {
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
        
        // console.log(data);
        let items_lista = []
        for (let i = 0; i < data.length; i++) {
            items_lista.push(new item_lista(data[i].cancion, data[i].banda, data[i].total_partes, data[i].total_orden_partes));
        }
        return items_lista;

    }

    async GetCancion(item: item_lista): Promise<Cancion> {
        const response = await fetch(`/public/data/${item.banda.replace(/\s+/g, '-')}_${item.cancion.replace(/\s+/g, '-')}.json`);
        const data = await response.json();
        
        let partes = []
        for (let i = 0; i < data.acordes.partes.length; i++) {
            partes.push(new Parte(data.acordes.partes[i].nombre, data.acordes.partes[i].acordes));
        }

        
        const acordes = new Acordes(partes, data.acordes.orden_partes);
    
        return new Cancion(
            data.cancion,
            data.banda,
            acordes,
            new Letra(data.letras) 
        );
}
}

