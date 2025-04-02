import { mount } from '@vue/test-utils';
import { EditarMusicaHelper } from '../comp_editar/editarMusicaHelper';
import { Acordes, Parte } from '../../modelo/acordes';

describe('Editor Helper Musica', () => {
  
  
  it('No modifica', () => {
    let acordes = new Acordes([
        new Parte("p1", ["A", "B"]),
        new Parte("p2", ["A", "B"]),
        new Parte("p3", ["A", "B"])], [0, 1, 2]);
      const acordesret = EditarMusicaHelper.mixear(acordes, 1, []);
      expect([0, 1, 2]).toEqual(acordesret.orden_partes);
  });

  
  it('Une con siguiente', () => {
    let acordes = new Acordes([
        new Parte("p1", ["A", "B"]),
        new Parte("p2", ["A1", "B1"]),
        new Parte("p3", ["A", "B"])], [0, 1, 2]);
      const acordesret = EditarMusicaHelper.mixear(acordes, 0, [1]);
      expect(acordesret.orden_partes).toEqual([0, 1]);
      expect(acordesret.partes[0].acordes).toEqual(["A", "B", "A1", "B1"]);
  });


  
  it('Une con siguiente', () => {
    let acordes = new Acordes([
        new Parte("p1", ["A", "B"]),
        new Parte("p2", ["A", "B"]),
        new Parte("p3", ["A", "B"])], [0, 0, 1, 0 ,2]);
      const acordesret = EditarMusicaHelper.mixear(acordes, 0, [1, 2]);
      expect(acordesret.orden_partes).toEqual([0, 1, 2]);
  });




});
