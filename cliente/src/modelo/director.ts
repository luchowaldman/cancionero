
import { ModeloConfiguracion } from './modeloconfiguracion';
import { item_lista } from '../modelo/item_lista';
import { AdminListasTocables } from './AdminIndiceListas';
import { Cancion } from './cancion';
import { GetCanciones } from './GetCanciones';



export class Director {
    configuracion: ModeloConfiguracion;
    esDirector: boolean;
    estado: string = "pausado";
    
    
    protected cambiosListaHandler?: (lista: string) => void;
    protected cambiosNroCancionHandler?: (cancion: number) => void;
    protected cambiosCompasHandler?: (compas: number) => void;

    setcambiosListaHandler(handler: (lista: string) => void) {
        this.cambiosListaHandler = handler;
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

    click_play() {
        
    }   
          
  
  
  
        

    onGetDirector(director: string) {
        console.log("Director recibido CLASE BASE", director);
    }



    onListaRecibida(listaBandas: string[], listaTemas: string[]) {

        console.log("Lista recibida CLASE BASE", listaBandas, listaTemas);
    }

    onNroCancionRecibido(nro: number) {
        this.nro_cancion  = nro;
        this.obtenerCancion()
        console.log("Nro Cancion recibido", nro);
    }
  
   onNroCompasRecibido(nro: number) {
    this.nro_compas  = nro;
    this.cambiosCompasHandler?.(nro);
    console.log("Nro Compas recibido", nro);
  }
  

   onStartCompasRecibido(nro: number) {
    this.nro_compas  = nro;
    console.log("Star recibido", nro);
  }


    
    Iniciar() 
    {
        this.configuracion.sesion.estado = 'iniciando BASE';
        this.cambiosListaHandler?.("default"); 

    }
    

}