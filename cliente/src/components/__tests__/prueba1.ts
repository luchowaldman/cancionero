import { mount } from '@vue/test-utils';
import { EditarHelper } from '../comp_editar/editarHelper';
import { HtmlAcorde, HtmlAcordeConBr, HtmlAcordeSimple } from '../comp_editar/html_acorde';

describe('Editor Helper Letra', () => {
  
  
  it('Devuelve un acorde vacio', () => {
    let texto: string = "Un texto";
    let acordes: string[] = [];

    const objetos: HtmlAcorde[] = EditarHelper.acordes_a_objetoshtml(texto, acordes);
    expect(objetos.length).toBe(1);
    expect(objetos[0].acorde).toBe(".");
  });

  it('Devuelve acorde A', () => {
    let texto: string = "Un texto";
    let acordes: string[] = ["A"];

    const objetos: HtmlAcorde[] = EditarHelper.acordes_a_objetoshtml(texto, acordes);
    expect(objetos.length).toBe(1);
    expect(objetos[0].acorde).toBe("A");
  });

  
  it('Devuelve un acorde de 2', () => {
    let texto: string = "Un texto";
    let acordes: string[] = ["A", "B"];

    const objetos: HtmlAcorde[] = EditarHelper.acordes_a_objetoshtml(texto, acordes);
    expect(objetos.length).toBe(1);
    expect(objetos[0].acorde).toBe("A");
  });

  
  
  it('Devuelve 2 acordes', () => {
    let texto: string = "Un texto|con linea";
    let acordes: string[] = ["A", "B"];

    const objetos: HtmlAcorde[] = EditarHelper.acordes_a_objetoshtml(texto, acordes);
    expect(objetos.length).toBe(2);
    expect(objetos[0].acorde).toBe("A");
    expect(objetos[1].acorde).toBe("B");
  });


  
  it('Mismos BRs 1', () => {
    let texto: string = "Un texto<br>con linea";
    let acordes: string[] = ["A", "B"];
  const objetos: HtmlAcorde[] = EditarHelper.acordes_a_objetoshtml(texto, acordes);
    const texto_renderizado = EditarHelper.html_astring(objetos);
    
    const brCountTextoRenderizado = (texto_renderizado.match(/<br>/g) || []).length;
    expect(objetos.length).toBe(1);
  
  });

  it('Mismos BRs 2', () => {
    let texto: string = "Un texto<br><br>con linea";
    let acordes: string[] = ["A", "B"];
    const objetos: HtmlAcorde[] = EditarHelper.acordes_a_objetoshtml(texto, acordes);
    const texto_renderizado = EditarHelper.html_astring(objetos);  
    expect(objetos.length).toBe(1);
  
  });
  
  
  it('Un BR despues de fin de acorde', () => {
    let texto: string = "sad |<br>asd";
    let acordes: string[] = ["A", "B"];
    const objetos: HtmlAcorde[] = EditarHelper.acordes_a_objetoshtml(texto, acordes);
    const texto_renderizado = EditarHelper.html_astring(objetos);
    expect(objetos.length).toBe(2);
    expect(objetos[1] instanceof HtmlAcordeConBr).toBe(true);
    const htmlBR: HtmlAcordeConBr  = objetos[1] as HtmlAcordeConBr;
    expect(htmlBR.cantidadDeBr).toBe(1);
    expect(htmlBR.acorde).toBe("B");
    

    expect(texto_renderizado.split("<br>").length).toBe(1);

  });
  
  
// 
});
