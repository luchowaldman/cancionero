
export class Tiempo {
    formatSegundos(segundos: number): string {
        segundos = parseInt(segundos.toString());
        const minutos = Math.floor(segundos / 60);
        const segundosRestantes = segundos % 60;
        const minutosStr = minutos.toString().padStart(2, '0');
        const segundosStr = segundosRestantes.toString().padStart(2, '0');
        return `${minutosStr}:${segundosStr}`;
    }
}