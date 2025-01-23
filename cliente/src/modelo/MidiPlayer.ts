import * as Tone from "tone";

export class MidiPlayer {
  private instrument: Tone.Sampler;
  private isReady: boolean = false;
  private conectadoHandler?: (resultado: string) => void;

  constructor(samples: { [note: string]: string }) {
    this.instrument = new Tone.Sampler(samples).toDestination();
    this.instrument.toDestination();
  }

  public initialize(): void {
    Tone.start().then(() => {
      this.isReady = true;
      if (this.conectadoHandler) {
        this.conectadoHandler("MIDI Player is ready!");
      }
    }).catch(err => console.error(err));
  }

  public get isPlayerReady(): boolean {
    return this.isReady;
  }

  public setConectadoHandler(handler: (resultado: string) => void): void {
    this.conectadoHandler = handler;
  }

  public play(note: string, duration: number = 500): void {
    if (this.isReady) {
      this.instrument.triggerAttackRelease(note, duration / 1000);
    } else {
      console.error("MIDI Player is not ready");
    }
  }

  



public tocarNota(note: string): void {
  if (this.isReady) {
    this.instrument.triggerAttack(note);
  } else {
    console.error("MIDI Player is not ready");
  }
}

public soltarNota(note: string): void {
  if (this.isReady) {
    this.instrument.triggerRelease(note);
  } else {
    console.error("MIDI Player is not ready");
  }


  
}
}

export default MidiPlayer;
