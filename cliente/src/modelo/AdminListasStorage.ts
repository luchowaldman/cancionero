import { Almacenado } from "./Almacenado";
import { Cancion } from "./cancion";
import { item_lista } from "./item_lista";


export class AdminListasLocalStorage  {
    async GetCancionxTema(banda: string, cancion: string): Promise<Cancion> {
        let indice = this.almacen.indice();
        const index = indice.findIndex(i => i.banda === banda && i.cancion === cancion);
        ///console.log("Busca cancion", banda, cancion, index);
        return this.almacen.obtenerTodasLasCanciones()[index];
    
    }

    
        async GetCancion(item: item_lista): Promise<Cancion> {
            return this.GetCancionxTema(item.banda, item.cancion);
        }
    

    GuardarCancion(item: item_lista, cancion: Cancion) {
        let indice = this.almacen.indice();
        const index = indice.findIndex(i => i.banda === item.banda && i.cancion === item.cancion);
        let canciones = this.almacen.obtenerTodasLasCanciones()
        item.origen = 'local';
        if (index === -1) {
            indice.push(item);
            canciones.push(cancion);
        } else {
            indice[index] = item;
            canciones[index] = cancion;
        }
        this.almacen.guardarindice(indice);
            this.almacen.guardarTodasLasCanciones(canciones);
    }

    BorrarCancion(item: item_lista) {
        let indice = this.almacen.indice();
        const index = indice.findIndex(i => i.banda === item.banda && i.cancion === item.cancion);
        let canciones = this.almacen.obtenerTodasLasCanciones()
        if (index !== -1) {
            indice.splice(index, 1);
            canciones.splice(index, 1);
            this.almacen.guardarindice(indice);
            this.almacen.guardarTodasLasCanciones(canciones);
        }
    }

    listas() : string[] {
        let toret: string[] = ['default'];
        const item = localStorage.getItem('listas');
        console.log("listas", item);
        if (item) {
          toret = JSON.parse(item)
        }
        return toret;
      }

      guardar_lista_a_listas(lista: string) : string {

        let todas_listas: string[] = this.listas();
        if (todas_listas.indexOf(lista) === -1) {
            todas_listas.push(lista);
        }
        console.log(todas_listas);
        localStorage.setItem('listas', JSON.stringify(todas_listas));

        return lista;
      }
  
    private almacen: Almacenado;
    constructor(almacen: Almacenado) {
        this.almacen = almacen;
    }

    async getIndice(): Promise<item_lista[]> {
        return this.almacen.indice('canciones');
    }

    
}