import { Almacenado } from "./Almacenado";
import { Cancion } from "./cancion";
import { item_lista } from "./item_lista";


export class AdminListasLocalStorage  {
    async GetCancionxTema(banda: string, cancion: string): Promise<Cancion> {
        let indice = this.almacen.indice('canciones');
        const index = indice.findIndex(i => i.banda === banda && i.cancion === cancion);
        ///console.log("Busca cancion", banda, cancion, index);
        return this.almacen.obtenerTodasLasCanciones()[index];
    
    }

    GuardarCancion(item: item_lista, cancion: Cancion) {
        let indice = this.almacen.indice('canciones');
        const index = indice.findIndex(i => i.banda === item.banda && i.cancion === item.cancion);
        let canciones = this.almacen.obtenerTodasLasCanciones()
        if (index === -1) {
            indice.push(item);
            canciones.push(cancion);
        } else {
            indice[index] = item;
            canciones[index] = cancion;
        }
        this.almacen.guardarindice('canciones', indice);
            this.almacen.guardarTodasLasCanciones(canciones);
    }

    private almacen: Almacenado;
    constructor(almacen: Almacenado) {
        this.almacen = almacen;
    }

    async getIndice(): Promise<item_lista[]> {
        return this.almacen.indice('canciones');
    }

    
}