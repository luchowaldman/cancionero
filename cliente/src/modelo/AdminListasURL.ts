import { Acordes, Parte } from "./acordes";
import { Cancion } from "./cancion";
import { item_lista } from "./item_lista";
import { Letra } from "./letra";
import { AdminiListas } from "./AdminListas";


export class AdminListasURL extends  AdminiListas {
    private url: string;
    public items_lista: item_lista[] = [];

    constructor(url: string) {
        super();
        this.url = url;
    }

    async getIndice(): Promise<item_lista[]> {
        console.log("Busca indice", this.url + `/indice.json`);
        const response = await fetch(this.url + `/indice.json`);
        const data = await response.json();
        let items_lista = []
        for (let i = 0; i < data.length; i++) {
            const item = new item_lista(data[i].cancion, data[i].banda);
            item.total_partes = data[i].total_partes;
            item.total_orden_partes = data[i].total_orden_partes;
            item.compases_tiempo = data[i].compases_tiempo;
            item.bpm = data[i].bpm;
            item.calidad = data[i].calidad;
            item.len_partes = data[i].len_partes;
            item.escala = data[i].escala;
            items_lista.push(item);
        }
        return items_lista;

    }
    

    async GetCancion(item: item_lista): Promise<Cancion> {
        console.log("Buscar", item);
        const archivo = (this.url + `/${item.banda.replace(/\s+/g, '-')}_${item.cancion.replace(/\s+/g, '-')}.json`).toLocaleLowerCase();
        console.log(archivo)
        const response = await fetch(archivo);
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
            new Letra(data.letras),
            data.tempo
        );
    }

    async GetCancionxTema(banda: string, tema: string): Promise<Cancion> {
        //console.log("Busca cancion", banda, tema);
        return this.GetCancion(new item_lista(tema, banda));
    
    }

}

