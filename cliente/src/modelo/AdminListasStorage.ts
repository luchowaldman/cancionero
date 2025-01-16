import { Almacenado } from "./Almacenado";
import { item_lista } from "./item_lista";


export class AdminListasLocalStorage  {
    private almacen: Almacenado;
    public items_lista: item_lista[] = [];

    constructor(almacen: Almacenado) {
        this.almacen = almacen;
    }

    async getIndice(): Promise<item_lista[]> {
        let indice_almacen = [];
        let todo_almacen: [] = this.almacen.indice();
        for (let i = 0; i < todo_almacen.length; i++) {
            //console.log("Canción", todo_almacen[i]);
            indice_almacen.push(new item_lista(todo_almacen[i].cancion, todo_almacen[i].banda));
        }
        this.items_lista = indice_almacen;
        return this.items_lista;
    

    }
}