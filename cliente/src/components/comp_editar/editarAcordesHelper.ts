
import { Cancion } from '../../modelo/cancion';

export class editarAcordesHelper {

    static splitear_parte(cancion: Cancion, parte: number, acorde: number) {
    }
    static mix_acorde(cancion: Cancion, orden_parte: number, acorde: number) {
        const renglones = cancion.letras.renglones.flat();
        let cont_renglones = 0;
        const parte_tomod = cancion.acordes.orden_partes[orden_parte];
        let nue_reng: string[] = [];

        if (acorde >= 0 && acorde < cancion.acordes.partes[parte_tomod].acordes.length - 1) {
            cancion.acordes.partes[parte_tomod].acordes[acorde] = 
                cancion.acordes.partes[parte_tomod].acordes[acorde] + " " +
                cancion.acordes.partes[parte_tomod].acordes[acorde + 1];
            cancion.acordes.partes[parte_tomod].acordes.splice(acorde + 1, 1);
        }



        for (let i = 0; i < cancion.acordes.orden_partes.length; i++) 
        {
            const orden_partenro = cancion.acordes.orden_partes[i];
            if (orden_partenro === parte_tomod)
            {
                if (orden_parte == orden_partenro) {
                    
                for (let j = 0; j < cancion.acordes.partes[orden_partenro].acordes.length; j++) 
                    {
                        if (j === acorde) {
                            nue_reng.push(renglones[cont_renglones] + " " + renglones[cont_renglones + 1]);
                            cont_renglones++;
                            cont_renglones++;
                        } else {
                            nue_reng.push(renglones[cont_renglones]);
                            cont_renglones++;

                        }
                        
                    }
                }
            }
            else 
            {
                for (let j = 0; j < cancion.acordes.partes[orden_partenro].acordes.length; j++) 
                {                    
                    nue_reng.push(renglones[cont_renglones]);
                    cont_renglones++;
                }


            }

            
        }

        cancion.letras.renglones = [nue_reng];
    }
}