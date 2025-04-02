import { mount } from '@vue/test-utils';
import { EditarMusicaHelper } from '../comp_editar/editarMusicaHelper';
import { Acordes, Parte } from '../../modelo/acordes';

describe('Editor Helper Musica', () => {
  
  
  it('No modifica', () => {
    let acordes = new Acordes([
        new Parte("p1", ["A", "B"]),
        new Parte("p2", ["A", "B"])], [0, 1, 1]);
      const acordesret = EditarMusicaHelper.normalizar_acordes(acordes);
      expect([0, 1, 1]).toEqual(acordesret.orden_partes);
  });


  
  it('Borra los que sobran 1', () => {
    let acordes = new Acordes([
        new Parte("p1", ["A", "B"]),
        new Parte("p2", ["A", "B"]),
        new Parte("p3", ["A", "B"]),
        new Parte("p4", ["A", "B"]),
        new Parte("p5", ["A", "B"]),
        new Parte("p6", ["A", "B"])], [0, 4, 4]);
      const acordesret = EditarMusicaHelper.normalizar_acordes(acordes);
      expect(acordesret.partes.length).toEqual(2);
      expect([0, 1, 1]).toEqual(acordesret.orden_partes);
  });


  
  it('Borra los que sobran 2', () => {
    let acordes = new Acordes([
        new Parte("p1", ["A", "B"]),
        new Parte("p2", ["A", "B"]),
        new Parte("p3", ["A", "B"]),
        new Parte("p4", ["A", "B"]),
        new Parte("p5", ["A", "B"]),
        new Parte("p6", ["A", "B"])], [2, 4, 4]);
      const acordesret = EditarMusicaHelper.normalizar_acordes(acordes);
      expect(acordesret.partes.length).toEqual(2);
      expect([0, 1, 1]).toEqual(acordesret.orden_partes);
  });


  
  it('Borra los que sobran 3', () => {
    let acordes = new Acordes([
        new Parte("p1", ["A", "B"]),
        new Parte("p2", ["A", "B"]),
        new Parte("p3", ["A", "B"]),
        new Parte("p4", ["A", "B"]),
        new Parte("p5", ["A", "B"]),
        new Parte("p6", ["A", "B"])], [4, 1, 1]);
      const acordesret = EditarMusicaHelper.normalizar_acordes(acordes);
      expect(acordesret.partes.length).toEqual(2);
      expect([0, 1, 1]).toEqual(acordesret.orden_partes);
  });


  
  it('Borra los que sobran 4', () => {
    let acordes = new Acordes([
        new Parte("p1", ["A", "B"]),
        new Parte("p2", ["A", "B"]),
        new Parte("p3", ["A", "B"]),
        new Parte("p4", ["A", "B"]),
        new Parte("p5", ["A", "B"]),
        new Parte("p6", ["A", "B"])], [3, 4, 4]);
      const acordesret = EditarMusicaHelper.normalizar_acordes(acordes);
      expect(acordesret.partes.length).toEqual(2);
      expect([0, 1, 1]).toEqual(acordesret.orden_partes);
  });


});
