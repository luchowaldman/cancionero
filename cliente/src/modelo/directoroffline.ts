
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
        this.nro_compas = parseInt(nro.toString());
        this.cambiosCompasHandler?.(nro);
    }

    click_pause() {
        
        console.log("Pause");
        this.reproductor.pausar();
    }

    click_play() {

        
            //console.log("Play", this.cambiosHandler);
            this.estado = 'iniciando';
            
            //this.cambiosHandler?.(this);
            this.reproductor = new Reproductor(this.musica.duracion_compas(this.cancion_actual) * 1000);
            this.reproductor.setIniciaCicloHandler(this.onNroCompasRecibido.bind(this));
            this.reproductor.iniciar();
        
    }   
          
  
  
  
        

    onGetDirector(director: string) {
        console.log("Director recibido", director);
        if (director == this.configuracion.sesion.usuario_sesion) {
        this.esDirector = true;
        }
    }



    onListaRecibida(listaBandas: string[], listaTemas: string[]) {

        console.log("Lista recibida", listaBandas, listaTemas);
        this.lista = [];
        for (let i = 0; i < listaBandas.length; i++) {
            this.lista.push(new item_lista(listaTemas[i], listaBandas[i]));    

        }
        
        
    }

    onNroCancionRecibido(nro: number) {
        this.nro_cancion  = nro;
        localStorage.setItem('nro_cancion', this.nro_cancion.toString());
        console.log("Nro Cancion recibido", nro);
    }
  
   onNroCompasRecibido() 
   {
       this.cambiosCompasHandler?.(this.nro_compas);
  }
  
  

}