

// src/cancion.ts
export class Reproductor  {
    private duracion_compas: number;
    private total_compases: number;
    private current_compas: number;

    private intervalId: any;

    

        constructor(duracion_compas: number, total_compases: number) 
        {
            this.duracion_compas = duracion_compas;
            this.total_compases = total_compases;
            this.current_compas = 0;
            this.intervalId = null;
        }
        private IniciaHandler?: () => void;
        private FinalizaHandler?: () => void;
        private IniciaCompasHandler?: (nro_compas: number) => void;

        public setIniciaHandler(handler: () => void) {
            this.IniciaHandler = handler;
        }

        public setFinalizaHandler(handler: () => void) {
            this.FinalizaHandler = handler;
        }

        public setIniciaCompasHandler(handler: (nro_compas: number) => void) {
            this.IniciaCompasHandler = handler;
        }    

        public setDuracion(duracion_compas: number) {
            this.duracion_compas = duracion_compas;
        }


        
        
        public iniciar() 
        {

            if (this.current_compas == 0) {
                
                if (this.IniciaHandler) {
                    this.IniciaHandler();
                }
            }
            
            if (this.IniciaCompasHandler) {
                this.IniciaCompasHandler(this.current_compas);
            }

            this.intervalId = setInterval(() => {
            this.current_compas++;            
            if (this.current_compas >= this.total_compases) {
                this.parar();
                        
            if (this.FinalizaHandler) {
                this.FinalizaHandler();
                }
            }
                else {
            if (this.IniciaCompasHandler) {
                this.IniciaCompasHandler(this.current_compas);
            }}

            }, this.duracion_compas);
        }

        pausar() {
            if (this.intervalId) {
                clearInterval(this.intervalId);
                this.intervalId = null;
            }
        }

        parar() {
            console.log("Parandoooo!");
            if (this.intervalId) {
                clearInterval(this.intervalId);
                this.intervalId = null;
            }
            this.current_compas = 0;
        }
    }


