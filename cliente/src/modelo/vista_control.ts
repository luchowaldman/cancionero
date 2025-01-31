import { markRaw, ref } from 'vue';
import ComponenteMusicalLetraAcordes from '../components/ComponenteMusicalLetrayAcordes.vue';
import ComponenteMusicalAcordesSeguidos from '../components/ComponenteMusicalAcordesSeguidos.vue';

import ComponenteMusicalLetra  from '../components/ComponenteMusicalLetra.vue';
import ComponenteMusicalAcordes from '../components/ComponenteMusicalAcordes.vue';
import ComponenteMusicalVerDetalles from '../components/ComponenteMusicalVerDetalles.vue';


export class VistaControl {
    tamanio_referencia: number;
    total_renglones: number;
    renglones_avanza: number;
    alto: number;
    tipo: string;
    clase: string;
    componente = ref();

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
        if (this.tipo === 'letra') {
            return markRaw(ComponenteMusicalLetra);
        }
        if (this.tipo === 'detalle') {
            return markRaw(ComponenteMusicalVerDetalles);
        }
        if (this.tipo === 'acordes_seguidos') {
            return markRaw(ComponenteMusicalAcordesSeguidos);
        }
        
        if (this.tipo === 'acordes') {
            return markRaw(ComponenteMusicalAcordes);
        }
        
        
        return markRaw(ComponenteMusicalAcordes);
        
    }
}