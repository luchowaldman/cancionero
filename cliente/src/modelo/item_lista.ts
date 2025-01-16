


export class item_lista {
    public estado: string;
    public escala: string;
    public total_partes: number;
    public total_partes: number;
    public len_partes: number[];
    public total_orden_partes: number;
    public compases_tiempo: number;
    public bpm: number;
    public calidad: number;

    constructor(
        public cancion: string,
        public banda: string
    ) {
        this.estado = 'nocargado';
        this.escala = '';
        this.total_partes = 0;
        this.total_orden_partes = 0;
        this.compases_tiempo = 4;
        this.bpm = 60;
        this.calidad = 1;
        this.len_partes = [];
    }

    setTemaJSON(temaJSON: any) {
        this.escala = temaJSON.partes[0].acordes[0];
        this.total_partes = temaJSON.partes.length;
        this.total_orden_partes = temaJSON.orden_partes.length;
        this.estado = 'ok';
    }
}
