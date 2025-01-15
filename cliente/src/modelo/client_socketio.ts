import { io, Socket } from "socket.io-client";

interface ServerToClientEvents {
    inicio_compas: (compas: number) => void;
    pausa: () => void;
    cambio_cancion: (nuevaCancion: number) => void;
}

interface ClientToServerEvents {
    iniciar_compas: (compas: number) => void;
    pausar: () => void;
    cambiar_cancion: (nuevaCancion: number) => void;
}

export class Cliente {
    private socket!: Socket<ServerToClientEvents, ClientToServerEvents>;

    private iniciarCompasHandler?: (compas: number) => void;
    public setIniciarCompasHandler(handler: (compas: number) => void): void {
        this.iniciarCompasHandler = handler;
    }

    private pausaHandler?: () => void;
    public setPausaHandler(handler: () => void): void {
        this.pausaHandler = handler;
    }

    private cambioCancionHandler?: (nuevaCancion: number) => void;
    public setCambioCancionHandler(handler: (nuevaCancion: number) => void): void {
        this.cambioCancionHandler = handler;
    }

    private urlserver: string;

    constructor(urlserver: string) {
        this.urlserver = urlserver;
    }
    public disconnect(): void 
    { 
        if (this.socket) 
            { 
                this.socket.disconnect();
                console.log("socket disconnected manually"); 
            } 
    }

    public connect(): void {
        let socket: Socket<ServerToClientEvents, ClientToServerEvents> = io(this.urlserver, {
            autoConnect: true,
            rejectUnauthorized: false,
            transports: ['websocket']
        });

        socket.on("connect", () => {
            console.log("socket connected");
        });

        socket.on("disconnect", () => {
            console.log("socket disconnected");
        });

        socket.on("inicio_compas", (compas) => {
            console.log("inicio_compas received with compas:", compas);
            this.iniciarCompasHandler?.(compas);
        });

        socket.on("pausa", () => {
            console.log("pausa received");
            this.pausaHandler?.();
        });

        socket.on("cambio_cancion", (nuevaCancion) => {
            console.log("cambio_cancion received:", nuevaCancion);
            this.cambioCancionHandler?.(nuevaCancion);
        });

        this.socket = socket;
    }

    public enviarIniciarCompas(compas: number): void {
        console.log("enviar iniciar_compas with compas:", compas);
        this.socket.emit('iniciar_compas', compas);
    }

    public enviarPausar(): void {
        console.log("enviar pausar");
        this.socket.emit('pausar');
    }

    public enviarCambiarCancion(nuevaCancion: number): void {
        console.log("enviar cambiar_cancion with nuevaCancion:", nuevaCancion);
        this.socket.emit('cambiar_cancion', nuevaCancion);
    }
}
