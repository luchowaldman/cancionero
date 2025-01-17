import { io, Socket } from "socket.io-client";

interface ServerToClientEvents {
    replica: (datos: string[]) => void;
}

interface ClientToServerEvents {
    replicar: ([]) => void;
}

export class Cliente {
    private socket!: Socket<ServerToClientEvents, ClientToServerEvents>;

    private replicaHandler?: (datos: string[]) => void;
    public setreplicaHandler(handler: (datos: string[]) => void): void {
        this.replicaHandler = handler;
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

        socket.on("replica", (datos: string[]) => {
            console.log("inicio_compas received with compas:", datos);
            this.replicaHandler?.(datos);
        });

        this.socket = socket;
    }

    public replicar(datos: []): void {
        this.socket.emit('replicar', datos);
    }

}
