import { Cancion } from "./cancion";
import { item_lista } from "./item_lista";
import { AdminListasURL } from "./AdminListasURL";

export class GetCanciones {
    static obtenerCancion(item_lista: item_lista): Promise<Cancion>  {
        // Aquí puedes agregar la lógica para convertir item_lista en una instancia de Cancion
        const admin: AdminListasURL = new AdminListasURL('/data/canciones');
        return admin.GetCancion(item_lista);
    }
}


