export class Tiempo {
    formatSegundos(segundos: number): string {
        const minutos = Math.floor(segundos / 60);
        const segundosRestantes = segundos % 60;
        const minutosStr = minutos.toString().padStart(2, '0');
        const segundosStr = segundosRestantes.toString().padStart(2, '0');
        return `${minutosStr}:${segundosStr}`;
    }
}