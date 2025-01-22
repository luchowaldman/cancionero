import { Almacenado } from "./Almacenado";
import { Cancion } from "./cancion";
import { item_lista } from "./item_lista";


export class AdminListasTocables  {

        // Método para devolver un listado de todas las canciones almacenadas
    GetIndice(lista: string): item_lista[] 
    {
        console.log('GetIndice', lista)
        const item = localStorage.getItem('indice_lst_' + lista);
        if (item) {
                return JSON.parse(item)
        }
        return []
    }

    SaveIndice(name_lista: string, lista: item_lista[] )
    {
        localStorage.setItem('indice_lst_' + name_lista, JSON.stringify(lista));
        
    }

    constructor() {
    }


}


