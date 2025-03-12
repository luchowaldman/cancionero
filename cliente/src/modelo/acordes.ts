// src/cancion.ts
export class Parte {
    nombre: string;
    acordes: string[];

    constructor(nombre: string, acordes: string[]) {
        this.nombre = nombre;
        this.acordes = acordes;
    }
}


export class Acordes {
    partes: Parte[];
    orden_partes: number[];

    constructor(partes: Parte[], orden_partes: number[]) {
        this.partes = partes;
        this.orden_partes = orden_partes;
    }
     
        GetTodosLosAcordes() {
          let ret: string[] = [];
          for (let i = 0; i < this.orden_partes.length; i++) {
            ret = ret.concat(this.partes[this.orden_partes[i]].acordes);
          }
          return ret;
        }
    
}
