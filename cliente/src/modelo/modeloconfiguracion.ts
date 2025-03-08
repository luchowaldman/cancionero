
import { EstadoSesion } from './estadosesion';

export class ModeloConfiguracion {



    nombre: string = "default";
    
    sesion: EstadoSesion = new EstadoSesion();
    concecciones: string[] = [];
    datos: string[] = [];


    constructor() {
    }
     
}
