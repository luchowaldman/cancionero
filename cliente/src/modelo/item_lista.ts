


export class item_lista {
    public origen: string;
    public escala: string;
    public compases: number;
    public compas_unidad: number;
    public compas_cantidad: number;
    public bpm: number;
    public calidad: number;

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
    }

    
}
