import { Cancion } from "./cancion";

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
      const canciones = this.obtenerTodasLasCanciones();
      return canciones.find((cancion) => cancion.cancion === nombre && cancion.banda === banda);
    }
  
    // Método para devolver un listado de todas las canciones almacenadas
    indice(): Cancion[] {
      return this.obtenerTodasLasCanciones();
    }
  
    // Método privado para obtener todas las canciones del localStorage
    private obtenerTodasLasCanciones(): Cancion[] {
      const canciones = localStorage.getItem(this.storageKey);
      return canciones ? JSON.parse(canciones) : [];
    }
  }
  