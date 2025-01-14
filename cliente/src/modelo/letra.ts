
export class Letra {
    renglones: string[][];

    constructor(renglones: string[][]) {
        this.renglones = renglones;
    }

    getRenglones() {
        return this.renglones.flat();
    }
     
}
