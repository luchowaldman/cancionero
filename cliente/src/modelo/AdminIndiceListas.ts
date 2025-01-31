import { item_lista } from "./item_lista";


export class AdminListasTocables  {
    BorrarCancion(value: string, item: item_lista) {
        console.log('BorrarCancion', value, item)
        let lista = this.GetIndice(value)
        let index = lista.findIndex(x => x.banda == item.banda && x.cancion == item.cancion)
        if (index >= 0) {
            lista.splice(index, 1)
            this.SaveIndice(value, lista)
        }
    }

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


