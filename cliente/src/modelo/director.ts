
import { ModeloConfiguracion } from './modeloconfiguracion';
import { item_lista } from '../modelo/item_lista';
import { AdminListasTocables } from './AdminIndiceListas';
import { Cancion } from './cancion';
import { GetCanciones } from './GetCanciones';
import { ref, Ref } from 'vue';
import { Acordes } from './acordes';
import { Letra } from './letra';



export class Director {
    configuracion: ModeloConfiguracion;
    esDirector: boolean;    
    public compas: Ref<number> = ref(-2);
    public cancion: Ref<Cancion>  = ref(new Cancion("Cancion no cargada", "sin banda", new Acordes([], []), new Letra([])));
    public bpm_encompas: Ref<number> = ref(0);
    
    
    
    protected cambiosListaHandler?: (lista: string) => void;
    protected cambiosNroCancionHandler?: (cancion: number) => void;
    protected cambiosCompasHandler?: (compas: number) => void;
    protected cambiosEstadoHandler?: (estado: string) => void;

    setcambiosListaHandler(handler: (lista: string) => void) {
        this.cambiosListaHandler = handler;
    }

    setcambiosEstadoHandler(handler: (estado: string) => void) {
        this.cambiosEstadoHandler = handler;
    }

    setcambiosNroCancionHandler(handler: (cancion: number) => void) {
        this.cambiosNroCancionHandler = handler;
    }

    setcambiosCompasHandler(handler: (compas: number) => void) {
        this.cambiosCompasHandler = handler;
    }
    
    constructor(configuracion: ModeloConfiguracion) 
    {
        this.configuracion = configuracion;
        this.esDirector = false;
    }


    user_set_nro_cancion(nro_cancion: number) {
        console.log("set_nro_cancion", nro_cancion);
    }

    user_set_update_compas(nro: number) {
        console.log("set_nro_cancion", nro);
        //console.log("Compas actualizado", nro);
    }

    click_pause() {
    }


    click_stop() {}
    iniciar_clock() 
    {
        

    }

    click_play() {
        console.log("CLICK PLAY DIRECTOR BASE", this.cambiosEstadoHandler);
    }   
          
  
  
  
        

    onGetDirector(director: string) {
        console.log("Director recibido CLASE BASE", director);
    }




   onStartCompasRecibido(nro: number) {
  }


    
    Iniciar() 
    {
        this.configuracion.sesion.estado = 'iniciando BASE';
        this.cambiosListaHandler?.("default"); 

    }
    

}