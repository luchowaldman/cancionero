
import { ModeloConfiguracion } from './modeloconfiguracion';
import { Cliente } from '../modelo/client_socketio';
import { item_lista } from '../modelo/item_lista';
import { Almacenado } from './Almacenado';
import { AdminListasLocalStorage } from './AdminListasStorage';
import { AdminListasTocables } from './AdminIndiceListas';
import { Cancion } from './cancion';
import { GetCanciones } from './GetCanciones';

import { Reproductor } from '../modelo/reproductor';
import { Musica } from './musica';


export class Director {
    configuracion: ModeloConfiguracion;
    cliente: Cliente;
    nro_compas: number;
    nro_cancion: number;
    lista: item_lista[];
    cancion_actual: Cancion;
    esDirector: boolean;
    reproductor: Reproductor = new Reproductor(2200, 99999999);
    musica: Musica = new Musica();
    
    private cambiosHandler?: (director: Director) => void;

    setcambiosHandler(handler: (director: Director) => void) {
        this.cambiosHandler = handler;
    }
    
    
    private cambiosCancionHandler?: (cancion: Cancion) => void;

    setcambiosCancionHandler(handler: (cancion: Cancion) => void) {
        this.cambiosCancionHandler = handler;
    }

    private cambiosCompasHandler?: (compas: number) => void;

    setcambiosCompasHandler(handler: (compas: number) => void) {
        this.cambiosCompasHandler = handler;
    }
    
    constructor(Configuracion: ModeloConfiguracion, Cliente: Cliente) {
        this.configuracion = Configuracion;
        this.cliente = Cliente;
        this.configuracion.sesion.usuario_sesion = this.configuracion.nombre + "-" + Math.random()
        this.nro_compas = 0;
        this.nro_cancion = 0;
        this.lista = [];
        this.cancion_actual = new Cancion("Cancion no cargada", "sin banda");
        this.cliente.setconectadoHandler(this.handlerConectado.bind(this));
        this.cliente.setlistaHandler(this.onListaRecibida.bind(this));
        this.cliente.setcancionHandler(this.onNroCancionRecibido.bind(this));
        this.cliente.setcompasHandler(this.onNroCompasRecibido.bind(this));
        this.cliente.setstartCompasHandler(this.onStartCompasRecibido.bind(this));
        this.cliente.setdirectorHandler(this.onCliente_SendDirector.bind(this));
        this.esDirector = false;
    }


     onCliente_SendDirector(directorrec: string) {
            console.log("Soy el nuevo director", directorrec, this.lista)
            this.cliente.set_lista(this.lista.map(item => item.banda), this.lista.map(item => item.cancion));
    }
          
    click_siguiente() {
        const nuevo_track = (this.nro_cancion + 1) % this.total_canciones;
        if (this.configuracion.sesion.estado == "conectado") {
            this.cliente.set_cancion(nuevo_track);
        } else {
            this.onNroCancionRecibido(nuevo_track);
        }

    }
     
      
    click_anterior() {
        const nuevo_track = (this.nro_cancion - 1) % this.total_canciones;
        if (this.configuracion.sesion.estado == "conectado") {
            this.cliente.set_cancion(nuevo_track);
        } else {
            this.onNroCancionRecibido(nuevo_track);
        }

    }

    click_play() {
        let contar_tiempo: boolean = false;
        
        if (this.configuracion.sesion.estado != "conectado") 
        {
            console.log("Play", this.nro_compas);
            this.reproductor = new Reproductor(this.musica.duracion_compas(this.cancion_actual) * 1000 , this.musica.total_compases(this.cancion_actual));
            this.reproductor.setIniciaCompasHandler(this.onNroCompasRecibido.bind(this));
            this.reproductor.iniciar();
        }
        else {
            if ((this.configuracion.sesion.estado == "conectado") && (this.esDirector)) 
                {
                    contar_tiempo = true;
                    
                }
        }
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




    handlerConectado(estado: string) {
        this.configuracion.sesion.estado = estado;
        console.log("conectado", estado)
        if (estado=="") {
            this.configuracion.sesion.estado = "conectado"
            this.cliente.unirme_sesion(this.configuracion.sesion.nombre, this.configuracion.sesion.usuario_sesion)
        }
          
        if (estado=="desconecado") {
            this.configuracion.sesion.estado = "desconectado"
        }
          if (estado=="error") {
            this.configuracion.sesion.estado = "error"
        }
        this.cambiosHandler?.(this);
    }

     Iniciar() 
    {
        this.configuracion.sesion.estado = 'iniciando...';
        const admin_indiceslista = new AdminListasTocables();
        this.lista = admin_indiceslista.GetIndice("default");

        if (this.configuracion.sesion.iniciar_alcomienzo) 
        {
            this.cliente.connect();
        } else 
        {
            this.configuracion.sesion.estado = 'Inic. s/conexion';
        }
        this.obtenerCancion()

    }
    obtenerCancion() {
        GetCanciones.obtenerCancion(this.lista[this.nro_cancion]).then((cancion_get: Cancion) => {
            this.cancion_actual = cancion_get;
            this.cambiosCancionHandler?.(cancion_get);
        });
        

    }
    


    get total_canciones(): number {
        return this.lista.length;
    }

     Conectar()
    {
        this.configuracion.sesion.estado = 'Conectando..';
        this.cliente.connect();
        

        

    }

}