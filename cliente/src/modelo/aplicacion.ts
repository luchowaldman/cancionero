import { ref, Ref } from "vue";
import { EstadoSesion } from "./estadosesion";
import { ModeloConfiguracion } from "./modeloconfiguracion";

export class Aplicacion {
    public configuracionObj: ModeloConfiguracion = new ModeloConfiguracion();
    public viendo: Ref<string> = ref("tocar");

    private CargarConfiguracion(): void {
        this.viendo.value = localStorage.getItem("viendo") || "tocar";        

let config_load: string | null = localStorage.getItem("configuracion")
if (!config_load)
  config_load = ""



try {
  this.configuracionObj = JSON.parse(config_load);
} catch (error) 
{
}


this.configuracionObj = new ModeloConfiguracion()
this.configuracionObj.sesion = new EstadoSesion()
this.configuracionObj.sesion.nombre = "default"
this.configuracionObj.nombre = "default"
localStorage.setItem("configuracion", JSON.stringify(this.configuracionObj))

    }

    Iniciar(): void {
        this.CargarConfiguracion();
        console.log("La aplicación ha iniciado.");

    }
}