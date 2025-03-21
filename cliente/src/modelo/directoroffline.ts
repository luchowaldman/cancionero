
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
    nro_compas: number;
    nro_cancion: number;
    lista: item_lista[];
    cancion_actual: Cancion;
    esDirector: boolean;
    reproductor: Reproductor = new Reproductor(2200);
    musica: Musica = new Musica();
    

    setcambiosHandler(handler: (director: Director) => void) {
        this.cambiosHandler = handler;
    }
    
    

    setcambiosCancionHandler(handler: (cancion: Cancion) => void) {
        this.cambiosCancionHandler = handler;
    }


    setcambiosCompasHandler(handler: (compas: number) => void) {
        this.cambiosCompasHandler = handler;
    }
    
    constructor(Configuracion: ModeloConfiguracion) {
        super(Configuracion);
        this.configuracion = Configuracion;
        this.nro_compas = 0;
        this.nro_cancion = parseInt(localStorage.getItem('nro_cancion') || '0');
        this.lista = [new item_lista("intoxicados", "fuego") ];
        this.cancion_actual = new Cancion("Cancion no cargada", "sin banda");
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
        
        console.log("Pause");
        this.reproductor.pausar();
    }

    click_play() {

        
            console.log("Play", this.cambiosHandler);
            this.estado = 'iniciando';
            
            this.cambiosHandler?.(this);
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
        
        this.obtenerCancion()
    }

    onNroCancionRecibido(nro: number) {
        this.nro_cancion  = nro;
        localStorage.setItem('nro_cancion', this.nro_cancion.toString());
        this.obtenerCancion()
        console.log("Nro Cancion recibido", nro);
    }
  
   onNroCompasRecibido() 
   {
        if (this.estado == 'iniciando') {
            this.estado = 'tocando';
            this.cambiosHandler?.(this);
            
        } else { 
            this.nro_compas++;
        }
        this.cambiosCompasHandler?.(this.nro_compas);
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
        this.CargarLista();
        this.obtenerCancion()
        this.configuracion.sesion.estado = 'Desconectado';

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