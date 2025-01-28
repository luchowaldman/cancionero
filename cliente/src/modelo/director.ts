
import { Configuracion } from '../modelo/configuracion';
import { Cliente } from '../modelo/client_socketio';
import { item_lista } from '../modelo/item_lista';
import { Almacenado } from './Almacenado';
import { AdminListasLocalStorage } from './AdminListasStorage';
import { AdminListasTocables } from './AdminIndiceListas';

export class Director {
    configuracion: Configuracion;
    cliente: Cliente;
    nro_compas: number;
    nro_cancion: number;
    lista: item_lista[];
    esDirector: boolean;
    
    private cambiosHandler?: (director: Director) => void;

    setcambiosHandler(handler: (director: Director) => void) {
        this.cambiosHandler = handler;
    }
    
    constructor(Configuracion: Configuracion, Cliente: Cliente) {
        this.configuracion = Configuracion;
        this.cliente = Cliente;
        this.configuracion.sesion.usuario_sesion = this.configuracion.nombre + "-" + Math.random()
        this.nro_compas = 0;
        this.nro_cancion = 0;
        this.lista = [];
        this.cliente.setconectadoHandler(this.handlerConectado.bind(this));
        this.cliente.setlistaHandler(this.onListaRecibida.bind(this));
        this.cliente.setcancionHandler(this.onNroCancionRecibido.bind(this));
        this.cliente.setcompasHandler(this.onNroCompasRecibido.bind(this));
        this.cliente.setstartCompasHandler(this.onStartCompasRecibido.bind(this));
        this.esDirector = false;

        }


    onGetDirector(director: string) {
        console.log("Director recibido", director);
        if (director == this.configuracion.sesion.usuario_sesion) {
        this.esDirector = true;
        }
    }



    onListaRecibida(listaBandas: string[], listaTemas: string[]) {

        console.log("Lista recibida", listaBandas, listaTemas);
        let bandas = listaBandas.join(',');
        let temas = listaTemas.join(',');
        this.lista = [];
        for (let i = 0; i < listaBandas.length; i++) {
            this.lista.push(new item_lista(temas[i], bandas[i]));    

        }
    }

    onNroCancionRecibido(nro: number) {
        this.nro_cancion  = nro;
        console.log("Nro Cancion recibido", nro);
    }
  
   onNroCompasRecibido(nro: number) {
    this.nro_compas  = nro;
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
        if (this.configuracion.sesion.iniciar_alcomienzo) {
            this.configuracion.sesion.estado = 'Conectando...';
            this.cliente.connect();
        } else {
            const admin_indiceslista = new AdminListasTocables();
            this.lista = admin_indiceslista.GetIndice("default");
            this.configuracion.sesion.estado = 'Inic. s/conexion';
        }

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