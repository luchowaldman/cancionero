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
import { AdminListasTocables } from "./AdminIndiceListas";

export class Aplicacion {
    public configuracionObj: ModeloConfiguracion = new ModeloConfiguracion();
    public director: Director = new DirectorOffline(this.configuracionObj);

    public viendo_pagina: Ref<string> = ref("tocar");
    public cancion: Ref<Cancion>  = ref(new Cancion("Cancion no cargada", "sin banda", new Acordes([], []), new Letra([])));
    public compas: Ref<number> = ref(-2);
    public nro_cancion: Ref<number> = ref(-2);
    public estado: Ref<string> = ref("nuevo");
    public listacanciones: Ref<item_lista[]> = ref([]);
    public sesion: Ref<EstadoSesion> = ref(new EstadoSesion());
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
    GetCanciones.obtenerCancion(item).then((cancion_get: Cancion) => {
        this.editando_cancion.value = cancion_get;
      });
  }
  

    public acciono(valor: string, compas: number = 0) {

      
        

        switch (valor) {
          case 'next':
            this.director.user_set_nro_cancion(this.nro_cancion.value + 1);
          //  this.viendo_pagina.value = 'tocar'
            break;
          case 'previous':
            this.director.user_set_nro_cancion(this.nro_cancion.value - 1);
           // this.viendo_pagina.value = 'tocar'
            break;
            
          case 'setcancion':
            this.director.user_set_nro_cancion(compas);
          //  this.viendo_pagina.value = 'tocar'
            break;
          case 'play':
            this.director.click_play();
            break;
          case 'pause':
            this.director.click_pause();
            break;
          case 'update-compas':
            this.director.user_set_update_compas(compas);
            this.viendo_pagina.value = 'tocar'
            break;
          case 'conectar':
            console.log("conectar");
            this.Conectar();
            break;
          case 'desconectar':
            console.log("conectar");
            this.Desconectar();
            break;
          case 'editar':
                if (this.viendo_pagina.value == 'tocar') {
                      this.editando_item.value = this.listacanciones.value[this.nro_cancion.value];
                      
                      localStorage.setItem("editando_cancion", JSON.stringify(this.editando_item.value));
                      this.cargar_edit();
                }
                this.viendo_pagina.value  = valor;
                break;
          
          case 'tocar_cancion':
            this.director.user_set_nro_cancion(compas);
            // Actualizo esto porque, ¿actualiza la vista?s
            this.viendo_pagina.value = 'listas'
            break;
          case 'tocar':
            //this.director.CargarLista();
            this.viendo_pagina.value  = valor;
            break;
          case 'listas':
            this.viendo_pagina.value  = valor;
            break;
          case 'config':
            this.viendo_pagina.value  = valor;
            break;
          case 'buscar':
            this.viendo_pagina.value  = valor;
            break;
          default:
            console.warn(`Acción no reconocida: ${valor}`);
        }

        
        localStorage.setItem("viendo", valor);            
        
        
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
        this.director.setcambiosCompasHandler((nro: number) => {
          this.CambiarCompas(nro);
        });
        
        this.director.setcambiosNroCancionHandler((nro: number) => {
          this.EstablecerCancion(nro);
        });
        this.director.Iniciar();

        this.CargarLista("default");
    }
  public CambiarCompas(nro: number): void {
    this.compas.value = nro;
    
  }
  public CargarLista(lista: string, cancion: number = 0): void {
    const admin_indiceslista = new AdminListasTocables();
    this.listacanciones.value = admin_indiceslista.GetIndice(lista)
    this.EstablecerCancion(cancion);
  }

  public EstablecerCancion(nro_cancion: number): void {
    console.log("Establecer Cancion", nro_cancion);
    this.nro_cancion.value = nro_cancion;
    GetCanciones.obtenerCancion(this.listacanciones.value[this.nro_cancion.value]).then((cancion_get: Cancion) => {
      this.cancion.value = cancion_get;
      this.compas.value = -2;
  });
  }

  
}