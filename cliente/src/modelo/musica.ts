//* CLASE QUE SOLO DEVUELVE RESULTADOS TEORICOS */
import { AnalisisArmonico } from '../modelo/analisis_armonico';
import { Cancion } from './cancion';
import { item_lista } from './item_lista';
export class Musica {

  get_renglontexto_de_compas(cancion: Cancion, nro_compas: number): number {
    const renglones = cancion.letras.renglones.flat().slice(0, nro_compas).join('');
    return renglones.split('/n').length;
    

  }

  getDistanciaNotas(nota1: string, nota2: string, escala: string): number {
    
    const acores_escala = this.GetNotasdeescala(escala);

    let octava_nota1 = 0;

    if (!isNaN(parseInt(nota1.slice(-1)))) {
        octava_nota1 = parseInt(nota1.slice(-1));
        
    }
    
    let octava_nota2 = 0;
    if (!isNaN(parseInt(nota2.slice(-1)))) {
        octava_nota2 = parseInt(nota2.slice(-1));
    }
    
    let nota_nombre1 = nota1.replace(/[0-9]/g, '');
    let nota_nombre2 = nota2.replace(/[0-9]/g, '');
    let nro_nota1 = acores_escala.indexOf(nota_nombre1);
    let nro_nota2 = acores_escala.indexOf(nota_nombre2);

    let distancia = nro_nota1 - nro_nota2 + ((octava_nota1 - octava_nota2) * 7);
    return distancia;
  } 
    
    
    getAnalisis(nota: string, acores_escala: string[]): AnalisisArmonico
    {
        
        let nota_sin_alteracion: string = nota;
        let alteracion: string = '';
        const alteraciones = ['4', '5', '6', '7', '9', '11', '13'];
        for (let i = 0; i < alteraciones.length; i++) {
            if (nota_sin_alteracion.includes(alteraciones[i])) {
                nota_sin_alteracion = nota_sin_alteracion.replace(alteraciones[i], '');
                alteracion = alteraciones[i];
            }
        }
        

        for (let i = 0; i < acores_escala.length; i++) {
            if (acores_escala[i] == nota_sin_alteracion) {
                return new AnalisisArmonico(true, i + 1, alteracion, nota);
            }
        }
        return new AnalisisArmonico(false, -1, '', nota);

    }

    notas: string[] = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
    modos: { [key: string]: number[] } = {};
    modos_paraacorde: { [key: string]: string[] } = {};
    constructor() {
        this.modos['mayor'] = [2, 2, 1, 2, 2, 2];
        this.modos['menor'] = [2, 1, 2, 2, 1, 2];
        this.modos_paraacorde['mayor'] = ['','m','m','','','m','dim'];
        this.modos_paraacorde['menor'] = ['m','dim','','m','m','',''];
     }


     
     total_compases(cancion: Cancion): number 
     {
        let total = 0;
        for (let i = 0; i < cancion.acordes.orden_partes.length; i++) {
            const indice = cancion.acordes.orden_partes[i];
            total += cancion.acordes.partes[indice].acordes.length;
        }
        return total;

     }

     duracion_cancion(cancion: Cancion): number 
     {
        return this.total_compases(cancion) * this.duracion_compas(cancion);
     }

     duracion_cancion_indice(cancion: item_lista): number 
     {
        return cancion.compases * ((60 / cancion.bpm) * cancion.compas_cantidad)
     }

     duracion_compas(cancion: Cancion): number 
     {
        return ((60 / cancion.bpm) * cancion.compas_cantidad);

     }

    // Devuelve el numero de nota
    numeroNota(nota: string): number {
        const note_find = this.notas.indexOf(nota);
        return note_find;
    }
    // Devuelve el numero de nota
    nombreNota(nota: number): string {
        return this.notas[nota];
    }

    GetNotasdeescala(escala: string) 
    {
        
        if (escala == "")
            return [];
        if (escala == undefined)
            return [];
        let buscar = escala;
        let modo_escala = 'mayor';
        if (escala.includes('m')) {
            buscar = buscar.replace('m', '');
            modo_escala = 'menor';
        }
        
        
        let nota_ind = this.numeroNota(buscar);
        const modo_susecion: number[] = this.modos[modo_escala];
        const modo_paraacorde: string[] = this.modos_paraacorde[modo_escala];

        let acordes = [this.notas[nota_ind] + modo_paraacorde[0]];
        for (let i = 0; i < modo_susecion.length; i++) {
            nota_ind += modo_susecion[i];
            acordes.push(this.notas[nota_ind % (this.notas.length)] );
        }
        
        return acordes;
        }

    
    GetAcordesdeescala(escala: string) 
    {

        if (escala == "")
            return [];
        if (escala == undefined)
            return [];
        let buscar = escala;
        let modo_escala = 'mayor';
        if (escala.includes('m')) {
            buscar = buscar.replace('m', '');
            modo_escala = 'menor';
        }
        
        
        let nota_ind = this.numeroNota(buscar);
        const modo_susecion: number[] = this.modos[modo_escala];
        const modo_paraacorde: string[] = this.modos_paraacorde[modo_escala];

        let acordes = [this.notas[nota_ind] + modo_paraacorde[0]];
        for (let i = 0; i < modo_susecion.length; i++) {
            nota_ind += modo_susecion[i];
            acordes.push(this.notas[nota_ind % (this.notas.length)] + modo_paraacorde[i+1]);
        }
        
        return acordes;
    }


    esMenor(nota1: string, nota2: string) {
        let nro_nota1 = this.numeroNota(nota1);
        let nro_nota2 = this.numeroNota(nota2);
        console.log("Emenor",nro_nota1, nro_nota2);
        if (nro_nota1 < nro_nota2) {
            return true;
        }
        return false;
    }
    getNotasdeacorde(acorde: string, escala: string = ''): string[] {
        let toRet: string[] = [];
        const notas = this.GetNotasdeescala(acorde);
        let esca_put = escala;
        toRet.push(notas[0] + esca_put);
        if (this.esMenor(notas[2], notas[0]))
        {
            console.log(esca_put, escala, notas[2] , notas[0]);
            esca_put = (parseInt(esca_put) + 1).toString();
            console.log(esca_put, escala);
        }
        toRet.push(notas[2] + esca_put);
        if ((this.esMenor(notas[4], notas[0])) && (esca_put == escala))
        {
            esca_put = (parseInt(esca_put) + 1).toString();
        }
        toRet.push(notas[4] + esca_put);

        return toRet;
    }
    

    


}