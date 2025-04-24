import { ref, Ref } from "vue";
import { EstadoSesion } from "../estadosesion";
import { ModeloConfiguracion } from "../modeloconfiguracion";
import { DirectorOffline } from "../directoroffline";
import { Director } from "../director";
import { Cancion } from "../cancion";
import { Acordes } from "../acordes";
import { Letra } from "../letra";
import { DirectorOnline } from "../directoronline";
import { item_lista } from "../item_lista";
import { GetCanciones } from '../GetCanciones';
import { AdminListasTocables } from "../AdminIndiceListas";

export class Aplicacion {
    public configuracionObj: ModeloConfiguracion = new ModeloConfiguracion();

    public viendo_pagina: Ref<string> = ref("editar");
    public cancion: Ref<Cancion>  = ref(new Cancion("Cancion no cargada", "sin banda", new Acordes([], []), new Letra([])));
    public item: Ref<item_lista> = ref(new item_lista("no song name", "no band name"));

    public compas: Ref<number> = ref(-2);
    public nro_cancion: Ref<number> = ref(-2);
    public estado: Ref<string> = ref("nuevo");
    public listacanciones: Ref<item_lista[]> = ref([]);
    public sesion: Ref<EstadoSesion> = ref(new EstadoSesion());
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

    


    public acciono(valor: string, compas: number = 0) {
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
        
        this. CargarLista("default", 0);
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