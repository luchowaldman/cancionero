import { ref, Ref } from "vue";
import { EstadoSesion } from "./estadosesion";
import { ModeloConfiguracion } from "./modeloconfiguracion";
import { DirectorOffline } from "./directoroffline";
import { Director } from "./director";
import { Cancion } from "./cancion";
import { Acordes } from "./acordes";
import { Letra } from "./letra";
import { DirectorOnline } from "./directoronline";
import { item_lista } from "./item_lista";
import { GetCanciones } from './GetCanciones';

export class Aplicacion {
    public configuracionObj: ModeloConfiguracion = new ModeloConfiguracion();
    public director: Director = new DirectorOffline(this.configuracionObj);

    public viendo_pagina: Ref<string> = ref("tocar");
    public cancion: Ref<Cancion>  = ref(new Cancion("Cancion no cargada", "sin banda", new Acordes([], []), new Letra([])));
    public compas: Ref<number> = ref(-2);

    public editando_cancion: Ref<Cancion>  = ref(new Cancion("Cancion no cargada", "sin banda", new Acordes([], []), new Letra([])));
    public editando_item: Ref<item_lista> = ref(new item_lista("no song name", "no band name"));
    private CargarConfiguracion(): void {
        this.viendo_pagina.value = localStorage.getItem("viendo") || "tocar";        

          
        let config_load: string | null = localStorage.getItem("configuracion")
        if (!config_load)
            config_load = ""
        try {this.configuracionObj = JSON.parse(config_load);} catch (error) {};


        this.configuracionObj = new ModeloConfiguracion()
        this.configuracionObj.sesion = new EstadoSesion()
        this.configuracionObj.sesion.nombre = "default"
        this.configuracionObj.nombre = "default"
        localStorage.setItem("configuracion", JSON.stringify(this.configuracionObj))

    }

    

 cargar_edit() {
    let item = JSON.parse(localStorage.getItem("editando_cancion") || "{}");
    console.log("item", item);
    GetCanciones.obtenerCancion(item).then((cancion_get: Cancion) => {
        console.log("cancion_get", cancion_get);    
        this.editando_cancion.value = cancion_get;
      });
  }
  

    public acciono(valor: string, compas: number = 0) {

        switch (valor) {
          case 'next':
            this.director.click_siguiente();
            break;
          case 'previous':
            this.director.click_anterior();
            break;
            
          case 'setcancion':
            this.director.set_nro_cancion(compas);
            break;
          case 'play':
            this.director.click_play();
            break;
          case 'pause':
            this.director.click_pause();
            break;
          case 'update-compas':
            this.director.update_compas(compas);
            break;
          case 'conectar':
            console.log("conectar");
            this.Conectar();
            break;
          case 'desconectar':
            console.log("conectar");
            this.Desconectar();
            break;
            
          case 'tocar_cancion':
            this.director.set_nro_cancion(compas);
            break;
          case 'tocar':
          case 'listas':
          case 'config':
          case 'editar':
          case 'buscar':
      
            if (valor == 'editar') 
            {
              if (this.viendo_pagina.value == 'tocar') 
              {
                this.editando_item.value = this.director.getitemActual();
                localStorage.setItem("editando_cancion", JSON.stringify(this.editando_item.value));                
              }              
              this.cargar_edit();
            }
            
            if (valor == 'tocar') 
            {
              this.director.CargarLista();      
            }      
            this.viendo_pagina.value  = valor;
            localStorage.setItem("viendo", valor);            
            break;
          default:
            console.warn(`Acción no reconocida: ${valor}`);
        }
        
      }

      
      
    Conectar() {
    }
  Desconectar() {
    
  }
  
  public width: number = window.innerWidth;
  public height: number = window.innerHeight;
    Iniciar(): void {
        this.CargarConfiguracion();
        if (this.viendo_pagina.value == 'editar') {
            this.cargar_edit();
        }

        
        console.log("La aplicación ha iniciado.");

    }
}