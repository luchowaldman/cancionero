import { Cancion } from "./cancion";
import { item_lista } from "./item_lista";

export class Almacenado {
    private storageKey: string;
  
    constructor(storageKey: string = 'canciones') {
      this.storageKey = storageKey;
    }
  
    // Método para agregar una canción al localStorage
    agregarCancion(cancion: Cancion): void {
      const canciones = this.obtenerTodasLasCanciones();
      
      
      const esta = canciones.find((cancion_existe) => cancion_existe.cancion === cancion.cancion && cancion_existe.banda === cancion.banda);
      if(esta){
        console.log("La cancion se actualiza");
        canciones[canciones.indexOf(esta)] = cancion;
        localStorage.setItem(this.storageKey, JSON.stringify(canciones));
        return;
      }

      canciones.push(cancion);
      localStorage.setItem(this.storageKey, JSON.stringify(canciones));
    }
  
    // Método para obtener una canción por su nombre
    obtenerCancion(nombre: string, banda: string): Cancion | undefined {
      nombre = nombre.toLocaleLowerCase();
      banda  = banda.toLocaleLowerCase();
      const canciones = this.obtenerTodasLasCanciones();
      console.log("Obtengo cancion", nombre, banda);
      
      let toret: Cancion | undefined = canciones.find((cancion) => cancion.cancion.toLocaleLowerCase() === nombre && cancion.banda.toLocaleLowerCase() === banda);
      if (!(toret === undefined)) {
        if (toret.compas_cantidad === undefined) {
          toret.compas_cantidad = 4;
          toret.compas_unidad = 4;
        }
      }

      return toret;
    }
  
    // Método para devolver un listado de todas las canciones almacenadas
    indice(nombre_indice: string): item_lista[] 
    {
        const item = localStorage.getItem('indice_' + nombre_indice);
        if (item) {
            return JSON.parse(item)

        }
        return []
    }

    guardarindice(nombre_indice: string, indice: item_lista[]) {
        localStorage.setItem('indice_' + nombre_indice, JSON.stringify(indice));
    }
  
    // Método privado para obtener todas las canciones del localStorage
    obtenerTodasLasCanciones(): Cancion[] {
      const canciones = localStorage.getItem(this.storageKey);
      return canciones ? JSON.parse(canciones) : [];
    }

    guardarTodasLasCanciones(canciones: Cancion[])  {
      localStorage.setItem(this.storageKey, JSON.stringify(canciones));
      
    }
    
  }
  