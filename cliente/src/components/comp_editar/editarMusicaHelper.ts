
import { ref, Ref } from 'vue';
import { Acordes, Parte } from '../../modelo/acordes';
import { Cancion } from '../../modelo/cancion';


export class EditarMusicaHelper {
    static mixear(acordes: Acordes, mixeando_parte: number, refPartesSeleccionadas: number[]): Acordes {
        
        
        let partes_toret: Parte[] = acordes.partes.copyWithin(0, acordes.partes.length);
        let secuencia_toret: number[] = [];
        
        for (let i = 0; i < acordes.orden_partes.length; i++)
        {
            const per = acordes.orden_partes[i];
            const parte_toret = acordes.partes[per];
            let nombre_acorde = parte_toret.nombre;
            let parteIndex = 0;

            if (per === mixeando_parte) 
            {
                if (i < acordes.orden_partes.length - 1) 
                {
                    if (refPartesSeleccionadas.indexOf(acordes.orden_partes[i + 1]) !== -1)
                    {
                        nombre_acorde += "+" + acordes.partes[acordes.orden_partes[i + 1]].nombre;
                        parteIndex = partes_toret.findIndex(p => p.nombre === nombre_acorde);
                        if (parteIndex === -1) 
                        {
                            partes_toret.push(new Parte(nombre_acorde, parte_toret.acordes.concat(acordes.partes[acordes.orden_partes[i + 1]].acordes)));
                            parteIndex = partes_toret.length - 1;
                        }

                        i++;
                    }
                }                
            }

            parteIndex = partes_toret.findIndex(p => p.nombre === nombre_acorde);
            secuencia_toret.push(parteIndex);
            
        }
        return this.normalizar_acordes(new Acordes(partes_toret, secuencia_toret));
    }



    static normalizar_acordes(acordes: Acordes): Acordes 
    {
        let partes_toret: Parte[] = [];
        let secuencia_toret: number[] = [];
        
        for (let i = 0; i < acordes.orden_partes.length; i++)
        {
        const per = acordes.orden_partes[i];
        const parte_toret = acordes.partes[per];

            // Check if the part name already exists in secuencia_toret
            const parteIndex = partes_toret.findIndex(p => p.nombre === parte_toret.nombre);
            if (parteIndex === -1) {
                secuencia_toret.push(partes_toret.length);
                partes_toret.push(parte_toret);
            } else {
                secuencia_toret.push(parteIndex);
            }
        }
        return new Acordes(partes_toret, secuencia_toret);
    
    }
}

