
import { EstadoSesion } from './estadosesion';

export class Configuracion {



    nombre: string = "default";
    
    sesion: EstadoSesion = new EstadoSesion();
    concecciones: string[] = [];
    datos: string[] = [];


    constructor() {
    }
     
}
