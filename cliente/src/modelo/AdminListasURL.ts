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
            item.compas_unidad = data[i].compas_unidad;
            item.compas_cantidad = data[i].compas_cantidad;

            item.compases = data[i].compases;
            item.len_secuencia = data[i].len_secuencia;
            item.acordes = data[i].acordes;
            item.len_partes = data[i].len_partes;
            item.bpm = data[i].bpm;
            item.calidad = data[i].calidad;
            item.escala = data[i].escala;
            item.origen = 'url|' + this.url;
            item.len_secuencia = data[i].len_secuencia;
            item.acordes = data[i].acordes;
            item.len_partes = data[i].len_partes;
            items_lista.push(item);
        }
        return items_lista;

    }
    

    async GetCancion(item: item_lista): Promise<Cancion> {
        console.log("Buscar", item);
        const archivo = this.url + `/${item.banda.replace(/\s+/g, '-')}_${item.cancion.replace(/\s+/g, '-')}.json`
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
            data.bpm, data.calidad, data.compas_cantidad, data.compases_tiempo, data.escala
        );
    }

    async GetCancionxTema(banda: string, tema: string): Promise<Cancion> {
        //console.log("Busca cancion", banda, tema);
        return this.GetCancion(new item_lista(tema, banda));
    
    }

}

