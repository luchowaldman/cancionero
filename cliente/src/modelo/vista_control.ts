import { markRaw, ref } from 'vue';
import ComponenteMusicalLetraAcordes from '../components/comp_tocar/ComponenteMusicalLetrayAcordes.vue';
import ComponenteMusicalAcordesSeguidos from '../components/comp_tocar/ComponenteMusicalAcordesSeguidos.vue';

import ComponenteMusicalLetra  from '../components/comp_tocar/ComponenteMusicalLetra.vue';
import ComponenteMusicalAcordes from '../components/comp_tocar/ComponenteMusicalAcordes.vue';
import ComponenteMusicalPartitura from '../components/ComponenteMusicalPartitura.vue';
import ComponenteMusicalVerDetalles from '../components/comp_tocar/ComponenteMusicalVerDetalles.vue';
import ComponenteMusicalTocar from '../components/comp_tocar/ComponenteMusicalTocar.vue';


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
        if (this.tipo === 'tocar') {
            return markRaw(ComponenteMusicalTocar);
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
        if (this.tipo === 'partitura') {
            return markRaw(ComponenteMusicalPartitura);
        }
        
        
        return markRaw(ComponenteMusicalAcordes);
        
    }
}