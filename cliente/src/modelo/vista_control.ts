import { markRaw, ref } from 'vue';
import ComponenteMusicalLetraAcordes from '../components/ComponenteMusicalLetrayAcordes.vue';
import ComponenteMusicalAcordes from '../components/ComponenteMusicalAcordes.vue';
import ComponenteMusicalVerDetalles from '../components/ComponenteMusicalVerDetalles.vue';


export class VistaControl {
    tamanio_referencia: number;
    total_renglones: number;
    renglones_avanza: number;
    alto: number;
    tipo: string;
    clase: string;

    constructor(tamanio_referencia: number, renglones_antes: number, renglones_despues: number, tipo: string, clase: string, alto: number) {
        this.tamanio_referencia = tamanio_referencia;
        this.total_renglones = renglones_antes;
        this.renglones_avanza = renglones_despues;
        this.tipo = tipo;
        this.clase = clase;
        this.alto = alto;
    }

    getMarkRaw(): any {
        if (this.tipo === 'letra_acordes') {
            return markRaw(ComponenteMusicalLetraAcordes);
        }
        if (this.tipo === 'detalle') {
            return markRaw(ComponenteMusicalVerDetalles);
        }
        return markRaw(ComponenteMusicalAcordes);
    }
}