import { Cancion } from "./cancion";
import { item_lista } from "./item_lista";
import { AdminListasURL } from "./AdminListasURL";
import { AdminListasLocalStorage } from "./AdminListasStorage";
import { Almacenado } from "./Almacenado";

export class GetCanciones {
    static obtenerCancion(item_lista: item_lista): Promise<Cancion>  {
        // Aquí puedes agregar la lógica para convertir item_lista en una instancia de Cancion
        if (item_lista == undefined) {
            return new Promise((resolve, reject) => {
                reject('item_lista es undefined');
            });

        }
        if (item_lista.origen == 'local') {
            const almacen = new Almacenado();
            const generadorlistasLS = new AdminListasLocalStorage(almacen);
            return generadorlistasLS.GetCancion(item_lista);
        }
        else {
            const admin: AdminListasURL = new AdminListasURL('/data/canciones');
            return admin.GetCancion(item_lista);
        }
}
}


