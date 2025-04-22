
import { Cancion } from '../../modelo/cancion';
import { HtmlAcorde, HtmlAcordeSimple, HtmlAcordeConBr } from './html_acorde';

export class EditarHelper {

    static texto_x_objetoshtml(texto: string, cancion: Cancion): HtmlAcorde[] {
        //HtmlAcorde, HtmlAcordeSimple, HtmlAcordeConBr
        
        const acordes = cancion.acordes.GetTodosLosAcordes()
        if (acordes == null) {
            return [];
        }  
        return this.acordes_a_objetoshtml(texto, acordes);


    }

    static get_acorde(acordes: string[], id: number): string {
        if (id == -1) {
            return '';
        }
        if (id >= acordes.length) { 
            return '.';
        }
        
        return acordes[id];
    }

    
    static acordes_a_objetoshtml(texto: string, acordes: string[]): HtmlAcorde[] {
        //HtmlAcorde, HtmlAcordeSimple, HtmlAcordeConBr
        let tore: HtmlAcorde[] = [];
        let cont = 0;
        const partes = texto.split('|');
        partes.forEach(parte => {
            if (parte.includes('<br>')) {
                const partes_split = parte.split('<br>');
                
                tore.push(new HtmlAcordeConBr(this.get_acorde(acordes, cont), partes_split[0].length, partes_split[partes_split.length - 1].length, partes_split.length - 1, cont));
            } else {
                tore.push(new HtmlAcordeSimple(this.get_acorde(acordes, cont), parte.length, cont));
            }
            cont++;
        });
        return tore;

    }

    static html_astring(html: HtmlAcorde[]): string {
        let tore = '';
        html.forEach(element => {
            tore += element.renderizar();
        });
        return tore;
    }


static ArmarFondoEditarAcordes(texto_cancion: string,cancion: Cancion): string {
    return this.html_astring(this.texto_x_objetoshtml(texto_cancion,cancion));
    
    }
}