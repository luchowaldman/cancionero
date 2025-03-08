export class AnalisisArmonico {
    nota: number;
    esta_enscala: boolean;
    alteracion: string;
    muestra: string;

    constructor(esta_enscala: boolean, nota: number, alteracion: string, muestra: string) {
        this.nota = nota;
        this.esta_enscala = esta_enscala;
        this.alteracion = alteracion;
        this.muestra = muestra;
    }
}