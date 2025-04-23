
import { ModeloConfiguracion } from './modeloconfiguracion';
import { item_lista } from './item_lista';
import { AdminListasTocables } from './AdminIndiceListas';
import { Cancion } from './cancion';
import { GetCanciones } from './GetCanciones';

import { Reproductor } from './reproductor';
import { Musica } from './musica';
import { Director } from './director';


export class DirectorOffline extends Director {
    configuracion: ModeloConfiguracion;
    esDirector: boolean;
    reproductor: Reproductor = new Reproductor(2200);
    musica: Musica = new Musica();

    

    setcambiosCompasHandler(handler: (compas: number) => void) {
        this.cambiosCompasHandler = handler;
    }
    
    constructor(Configuracion: ModeloConfiguracion) {
        super(Configuracion);
        this.configuracion = Configuracion;
        this.esDirector = true;
    }   

          
    click_siguiente() {
    }
     
      
    click_anterior() {
    }

    
    user_set_nro_cancion(nro_cancion: number) {
        this.cambiosNroCancionHandler?.(nro_cancion);        
    }

    user_set_update_compas(nro: number) {
        this.cambiosCompasHandler?.(nro);
    }

    click_pause() {
        this.bpm_encompas.value = 0;
        this.cambiosEstadoHandler?.("pausa");
        this.reproductor.pausar();
    }

    click_stop() {
        this.cambiosEstadoHandler?.("nuevo");
        this.reproductor.pausar();
        this.bpm_encompas.value = 0;
        this.cambiosCompasHandler?.(-2);
    }

    override click_play() {

        
            //console.log("Play", this.cambiosHandler);
            
            this.cambiosEstadoHandler?.("tocando");
            this.cambiosCompasHandler?.(this.compas.value + 1);
            this.reproductor = new Reproductor((60 / this.cancion.value.bpm) * 1000);
            this.reproductor.setIniciaCicloHandler(this.onInicioCiclo.bind(this));
            this.reproductor.iniciar();
            
    }
          
  
  
    onInicioCiclo() {
        this.bpm_encompas.value = this.bpm_encompas.value + 1;
        
        
        console.log("BPM en compas", this.bpm_encompas.value);
        if (this.bpm_encompas.value >= this.cancion.value.compas_cantidad) {
            this.cambiosCompasHandler?.(this.compas.value + 1);
            this.bpm_encompas.value = 0;
        }

        
        
      }
      
  
  
        

    onGetDirector(director: string) {
        console.log("Director recibido", director);
        if (director == this.configuracion.sesion.usuario_sesion) {
        this.esDirector = true;
        }
    }

  
  
  

}