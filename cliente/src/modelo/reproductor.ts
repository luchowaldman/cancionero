

// src/cancion.ts
export class Reproductor  {
    private duracion_compas: number;
    public estado: 'pausa' | 'iniciando' | 'tocando' = "pausa";

    private intervalId: any;

    

        constructor(duracion_compas: number) 
        {
            this.duracion_compas = duracion_compas;
            this.intervalId = null;
        }
        private IniciaHandler?: () => void;
        private FinalizaHandler?: () => void;
        private IniciaCicloHandler?: () => void;

        public setIniciaHandler(handler: () => void) {
            this.IniciaHandler = handler;
        }

        public setFinalizaHandler(handler: () => void) {
            this.FinalizaHandler = handler;
        }

        public setIniciaCicloHandler(handler: () => void) {
            this.IniciaCicloHandler = handler;
        }    

        public setDuracion(duracion_compas: number) {
            this.duracion_compas = duracion_compas;
        }


        iniciado: boolean = false;
        
        public iniciar() 
        {

            if (!this.iniciado) {
                
                this.iniciado = true;
                if (this.IniciaHandler) {
                    this.IniciaHandler();
                }
                
            }
            
            this.intervalId = setInterval(() => {
                if (this.IniciaCicloHandler) {
                    this.IniciaCicloHandler();
                }

            }, this.duracion_compas);
        }

        pausar() {
            if (this.intervalId) {
                clearInterval(this.intervalId);
                this.intervalId = null;
            }
        }
    }


