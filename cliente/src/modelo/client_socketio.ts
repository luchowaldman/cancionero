import { io, Socket } from "socket.io-client";

interface ServerToClientEvents {
    replica: (usuario: string, datos: string[]) => void;
}

interface ClientToServerEvents {
    replicar: (sesion: string, usuario: string, datos: string[]) => void;
    unirme_sesion(sesion: string, usuario: string): void;
}

export class Cliente {
    private socket!: Socket<ServerToClientEvents, ClientToServerEvents>;

    private replicaHandler?: (datos: string[]) => void;
    public setreplicaHandler(handler: (datos: string[]) => void): void {
        this.replicaHandler = handler;
    }

    private conectadoHandler?: (resultado: string) => void;
    public setconectadoHandler(handler: (resultado: string) => void): void {
        this.conectadoHandler = handler;
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
            this.conectadoHandler?.("");
        });

        
        socket.on("connect_error", () => {
            console.log("socket connected");
            this.conectadoHandler?.("error");
        });


        

        socket.on("disconnect", () => {
            console.log("socket disconnected");
            this.conectadoHandler?.("desconecado");
        });
            
        socket.on("replica", (datos: string[]) => {
            console.log("inicio_compas received with compas:", datos);
            this.replicaHandler?.(datos);
        });

        this.socket = socket;
    }

    public replicar(sesion: string, usuario: string, datos: string[] ): void {
        this.socket.emit('replicar' ,sesion, usuario, datos);
    }


    public unirme_sesion(sesion: string, usuario: string): void {
        console.log("unirme_sesion", sesion, usuario);
        this.socket.emit('unirme_sesion', sesion, usuario);
    }

}
