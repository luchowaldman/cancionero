import { mount } from '@vue/test-utils';
import { EditarAcordesToTextoHelper } from '../comp_editar/editarAcordesToTextoHelper';
import { Acordes, Parte } from '../../modelo/acordes';

const retorno_carro = "\n";
describe('Editor Helper Musica', () => {
  
  

  
  it('Vacio', () => {
    const texto = "";

    let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
    const acordes = editar.texto_to_acordes(texto);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual("'vacio'");
  });

  
  it('Vacio', () => {
    const texto = "'vacio'";
    let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
    const acordes = editar.texto_to_acordes(texto);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual("'vacio'");
  });


  it('un acorde', () => {
    const texto = "'verso 1'A";
    let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
    const acordes = editar.texto_to_acordes(texto);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual("'verso 1'A");
  });


  
  it('dos acorde', () => {
    const texto = "'verso 1'A|B";
    let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
    const acordes = editar.texto_to_acordes(texto);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual("'verso 1'A|B");
  });

  
  it('cuatro acorde', () => {
    const texto = "'verso 1'C|F|G|C";
    let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
    const acordes = editar.texto_to_acordes(texto);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual(texto);
  });

  
  it('cuatro acorde*2', () => {
    const texto = "'verso 1'C|F|G|C*2";
    let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
    const acordes = editar.texto_to_acordes(texto);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual(texto);
  });

  it('cuatro acorde*4', () => {
    const texto = "'verso 1'C|F|G|C*4";
    let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
    const acordes = editar.texto_to_acordes(texto);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual(texto);
  });

  
  
  it('cuatro acordes sin nombre *4', () => {
    const texto = "C|F|G|C*4";
    let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
    const acordes = editar.texto_to_acordes(texto);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual("'v1'C|F|G|C*4");
  });

  
  
  it('cuatro acorde*4 con renglones', () => {
    const texto = "'verso 1'C|F|G|C*4" + retorno_carro + "'verso 2'A|B|C|D*2";
    let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
    const acordes = editar.texto_to_acordes(texto);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual(texto);
  });

  
  it('cuatro acorde*4 con renglones', () => {
    const texto = "'verso 1'C|F|G|C*4" + retorno_carro + "'verso 2'A|B|C|D*1";
    let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
    const acordes = editar.texto_to_acordes(texto);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);

    expect(textor).toEqual("'verso 1'C|F|G|C*4" + retorno_carro + "'verso 2'A|B|C|D");
  });

  it('cuatro acorde*4 con renglones', () => {
    const texto = "'verso 1'C|F|G|C*4" + retorno_carro + "'verso 2'A|B|C|D";
    let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
    const acordes = editar.texto_to_acordes(texto);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    
    expect(textor).toEqual(texto);
  });
  

  it('acorde_tocecto Vacio', () => {
    const acordes = new Acordes([new Parte("vacio", [])], [0]);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual("'vacio'");
  });



  it('Un Acorde', () => {
  const texto = "A";
  let editar: EditarAcordesToTextoHelper = new EditarAcordesToTextoHelper();
  
  const acordes = editar.texto_to_acordes(texto);
  const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
  expect(textor).toEqual("'v1'A");
  });

  
  it('to_Texto Un Acorde', () => {
    const acordes: Acordes = new Acordes([new Parte("Intro", ["A"])], [0]);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual("'Intro'A");
  });

    
  it('to_Texto Dos Acorde', () => {
    const acordes: Acordes = new Acordes([new Parte("Intro", ["A", "B"])], [0]);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual("'Intro'A|B");
  });


  it('to_Texto Dos Acorde', () => {
    const acordes: Acordes = new Acordes([new Parte("Intro", ["A", "B"])], [0]);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual("'Intro'A|B");
  });
    
  it('to_Texto 2 Partes Acorde x 2', () => {
    const acordes: Acordes = new Acordes([new Parte("Intro", ["A", "B"])
    , new Parte("Verso", ["C"])], [0, 0, 1]);
  
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual("'Intro'A|B*2" + retorno_carro + "'Verso'C"); 
  });


    
  it('to_Texto 2 Partes Acorde, repetida', () => {
    const acordes: Acordes = new Acordes([new Parte("Intro", ["A", "B"])
    , new Parte("Verso", ["C"])], [0, 1, 0]);
    const textor = EditarAcordesToTextoHelper.acordes_to_texto(acordes);
    expect(textor).toEqual("'Intro'A|B" + retorno_carro + "'Verso'C" + retorno_carro + "'Intro'"); 
  });


  

});
