
import { ModeloConfiguracion } from './modeloconfiguracion';
import { Cliente } from '../modelo/client_socketio';
import { item_lista } from '../modelo/item_lista';
import { AdminListasTocables } from './AdminIndiceListas';
import { Cancion } from './cancion';
import { GetCanciones } from './GetCanciones';

import { Reproductor } from '../modelo/reproductor';
import { Musica } from './musica';


export class Director {
    configuracion: ModeloConfiguracion;
    lista: item_lista[];
    cancion_actual: Cancion;
    esDirector: boolean;
    estado: string;
    
    nro_compas: number;
    nro_cancion: number;
    
    
    protected cambiosHandler?: (director: Director) => void;

    setcambiosHandler(handler: (director: Director) => void) {
        this.cambiosHandler = handler;
    }
    

    
    protected cambiosCancionHandler?: (cancion: Cancion) => void;

    setcambiosCancionHandler(handler: (cancion: Cancion) => void) {
        this.cambiosCancionHandler = handler;
    }

    protected cambiosCompasHandler?: (compas: number) => void;

    setcambiosCompasHandler(handler: (compas: number) => void) {
        this.cambiosCompasHandler = handler;
    }
    
    constructor(configuracion: ModeloConfiguracion) 
    {
        this.configuracion = configuracion;
        this.nro_compas = 0;
        this.nro_cancion = 0;
        this.lista = [new item_lista("intoxicados", "fuego") ];
        this.cancion_actual = new Cancion("Cancion no cargada", "sin banda");
        this.esDirector = false;
    }


     onCliente_SendDirector(directorrec: string) {
            console.log("Soy el nuevo director", directorrec, this.lista)
            this.esDirector = true;
    }
          
    click_siguiente() {
        const nuevo_track = (this.nro_cancion + 1) % this.total_canciones;
        this.onNroCancionRecibido(nuevo_track);
    }
     
      
    click_anterior() {
        const nuevo_track = (this.nro_cancion - 1) % this.total_canciones;
        this.onNroCancionRecibido(nuevo_track);
    }

    
    set_nro_cancion(nro_cancion: number) {
        const nuevo_track = nro_cancion % this.total_canciones;
        this.onNroCancionRecibido(nuevo_track);

    }

    update_compas(nro: number) {
        this.nro_compas = parseInt(nro.toString());
        this.cambiosCompasHandler?.(nro);
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


    CargarLista() {
        
        const admin_indiceslista = new AdminListasTocables();
        this.lista = admin_indiceslista.GetIndice("default");
        if (this.lista.length == 0) {
            this.lista = [new item_lista("fuego", "intoxicados")];
        }
    }
    
    Iniciar() 
    {
        this.configuracion.sesion.estado = 'iniciando BASE';

    }
    obtenerCancion() {
        GetCanciones.obtenerCancion(this.lista[this.nro_cancion]).then((cancion_get: Cancion) => {
            this.cancion_actual = cancion_get;
            this.cambiosCancionHandler?.(cancion_get);
        });
    }

    getitemActual() {
        return this.lista[this.nro_cancion];
    }
    


    get total_canciones(): number {
        return this.lista.length;
    }


}