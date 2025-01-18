//* CLASE QUE SOLO DEVUELVE RESULTADOS TEORICOS */
export class Musica {
    notas: string[] = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
    modos: { [key: string]: number[] } = {};
    constructor() {
        this.modos['mayor'] = [2, 2, 1, 2, 2, 2, 1];
        this.modos['menor'] = [2, 1, 2, 2, 1, 2, 2];
     }
     
    // Devuelve el numero de nota
    numeroNota(nota: string): number {
        const note_find = this.notas.indexOf(nota);
        return note_find;
    }

    GetNotasdeescala(modo: string, nota: number) 
    {
        let nota_ind = nota;
        let acordes = [this.notas[nota_ind]];
        const modo_susecion: number[] = this.modos[modo];
        for (let i = 0; i < modo_susecion.length; i++) {
            nota_ind += modo_susecion[i];
            acordes.push(this.notas[nota_ind % (this.notas.length)]);
        }
        
        
        return acordes;
    }
}