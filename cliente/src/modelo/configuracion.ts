// src/cancion.ts
export class Sesion {
    nombre: string = "";
    estado: string = "";
    usuario_sesion: string = "";
    iniciar_alcomienzo: boolean = false;
    

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
