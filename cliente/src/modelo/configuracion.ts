// src/cancion.ts
export class Sesion {
    nombre: string = "";
    estado: string = "";
    

    constructor() {
    }
}


export class Configuracion {



    nombre: string = "default";
    
    sesion: Sesion = new Sesion();
    concecciones: string[] = [];
    datos: string[] = [];


    constructor() {
    }
     
}
