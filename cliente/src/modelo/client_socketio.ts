import { io, Socket } from "socket.io-client";

interface ServerToClientEvents {
    replica: (usuario: string, datos: string[]) => void;
    director: (director: string) => void;
    session: (bandas: string[], temas: string[], tocando: number, compas: number)=> void;
    lista: (bandas: string[], temas: string[])=> void;
    cancion: (nro: number)=> void;
    compas: (nro: number)=> void;
    start_compas: (nro: number)=> void;
    

}

interface ClientToServerEvents {
    replicar: (sesion: string, usuario: string, datos: string[]) => void;
    unirme_sesion(sesion: string, usuario: string): void;
    get_director(): void;
    get_sesion(): void;
    set_cancion(cancion: number): void;
    set_compas(compas: number): void;
    set_lista(bandas: string[], temas: string[]): void;
    setstart_compas(nro: number): void;
    
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
    private listaHandler?: (bandas: string[], temas: string[]) => void;
    public setlistaHandler(handler: (bandas: string[], temas: string[]) => void): void {
        this.listaHandler = handler;
    }
    
    private startCompasHandler?: (nro: number) => void;
    public setstartCompasHandler(handler: (nro: number) => void): void {
        this.startCompasHandler = handler;
    }

    private directorHandler?: (director: string) => void;
    public setdirectorHandler(handler: (director: string) => void): void {
        this.directorHandler = handler;
    }

    private sessionHandler?: (bandas: string[], temas: string[], tocando: number, compas: number) => void;
    public setsessionHandler(handler: (bandas: string[], temas: string[], tocando: number, compas: number) => void): void {
        this.sessionHandler = handler;
    }

    private cancionHandler?: (nro: number) => void;
    public setcancionHandler(handler: (nro: number) => void): void {
        this.cancionHandler = handler;
    }

    private compasHandler?: (nro: number) => void;
    public setcompasHandler(handler: (nro: number) => void): void {
        this.compasHandler = handler;
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


        socket.on("start_compas", (nro: number) => {
            console.log("start_compas received with nro:", nro);
            this.startCompasHandler?.(nro);
        });

        socket.on("disconnect", () => {
            console.log("socket disconnected");
            this.conectadoHandler?.("desconecado");
        });
            
        socket.on("replica", (datos: string[]) => {
            console.log("inicio_compas received with compas:", datos);
            this.replicaHandler?.(datos);
        });

        
        socket.on("director", (director: string) => {
            console.log("director received with compas:", director);
            this.directorHandler?.(director);
        });

        socket.on("session", (bandas: string[], temas: string[], tocando: number, compas: number) => {
            console.log("session received with bandas, temas, tocando, compas:", bandas, temas, tocando, compas);
            this.sessionHandler?.(bandas, temas, tocando, compas);
        });

        socket.on("cancion", (nro: number) => {
            console.log("cancion received with nro:", nro);
            this.cancionHandler?.(nro);
        });

        socket.on("compas", (nro: number) => {
            console.log("compas received with nro:", nro);
            this.compasHandler?.(nro);
        });

        socket.on("lista", (bandas: string[], temas: string[]) => {
            console.log("lista received with bandas, temas:", bandas, temas);
            this.listaHandler?.(bandas, temas);
        });

        this.socket = socket;
    }



    public unirme_sesion(sesion: string, usuario: string): void {
        console.log("unirme_sesion", sesion, usuario);
        this.socket.emit('unirme_sesion', sesion, usuario);
    }

    
    public replicar(sesion: string, usuario: string, datos: string[] ): void {
        this.socket.emit('replicar' ,sesion, usuario, datos);
    }

    public get_director(): void {
        this.socket.emit('get_director');
    }

    
    public get_sesion(): void {
        this.socket.emit('get_sesion');
    }

    public set_cancion(cancion: number): void {
        this.socket.emit('set_cancion', cancion);
    }

    public set_compas(compas: number): void {
        this.socket.emit('set_compas', compas);
    }

    
    public setinit_compas(compas: number): void {
        this.socket.emit('setstart_compas', compas);
    }

    public set_lista(bandas: string[], temas: string[]): void {
        console.log(bandas, temas);
        this.socket.emit('set_lista', bandas, temas);
    }

}
