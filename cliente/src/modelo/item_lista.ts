


export class item_lista {
    public origen: string;
    public escala: string;
    public compases: number;
    public compas_unidad: number;
    public compas_cantidad: number;
    public bpm: number;
    public calidad: number;

    public len_secuencia: number;
    public acordes: string;
    public len_partes: number[];

    constructor(
        public cancion: string,
        public banda: string
    ) {
        this.origen = '';
        this.escala = '';
        this.compases = 0;
        this.compas_unidad = 0;
        this.compas_cantidad = 4;
        this.bpm = 60;
        this.calidad = 1;
        this.origen = '';
        this.escala = '';
        this.len_secuencia = 0;
        this.acordes = '';
        this.len_partes = [];
    }

    
}
