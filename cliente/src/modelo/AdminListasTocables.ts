import { Almacenado } from "./Almacenado";
import { item_lista } from "./item_lista";


export class AdminListasTocables  {
    private almacen: Almacenado;
    constructor(almacen: Almacenado) {
        this.almacen = almacen;
    }


    async getIndice(): Promise<item_lista[]> {
        return this.almacen.indice('tocables');
    }

    
    GuardarCancion(item: item_lista) {
        let indice = this.almacen.indice('tocables');
        const index = indice.findIndex(i => i.banda === item.banda && i.cancion === item.cancion);
        if (index === -1) {
            indice.push(item);
        } else {
            indice[index] = item;
        }
          this.almacen.guardarindice('tocables', indice);
    }
}


