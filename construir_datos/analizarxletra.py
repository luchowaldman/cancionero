from analisisletra  import analizarxletra

resultados = []
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))
#resultados.append(analizarxletra('viejas-locas', 'adrenalina'))
#resultados.append(analizarxletra('viejas-locas', 'Leganlizenla'))
#resultados.append(analizarxletra('intoxicados', 'fuiste-lo-mejor'))
#resultados.append(analizarxletra('intoxicados', 'casi-sin-pensar'))
#resultados.append(analizarxletra('intoxicados', 'homero'))
#resultados.append(analizarxletra('intoxicados', 'nunca-Quise'))
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))

#resultados.append(analizarxletra('andres-calamaro', 'fuego'))
#resultados.append(analizarxletra('andres-calamaro', 'la-parte-de-adelante'))
#resultados.append(analizarxletra('andres-calamaro', 'flaca'))
#resultados.append(analizarxletra('andres-calamaro', 'cuando-no-estas'))
#resultados.append(analizarxletra('andres-calamaro', 'mi-gin-tinic'))
#resultados.append(analizarxletra('andres-calamaro', 'alta-suciedad'))
#resultados.append(analizarxletra('andres-calamaro', 'media-veronica'))
#resultados.append(analizarxletra('andres-calamaro', 'bohemio'))
#resultados.append(analizarxletra('andres-calamaro', 'el-salmon'))
#resultados.append(analizarxletra('andres-calamaro', 'soy-tuyo'))
#resultados.append(analizarxletra('andres-calamaro', 'loco'))

resultados.append(analizarxletra('andres-calamaro', 'cartas-sin-marcar'))
resultados.append(analizarxletra('andres-calamaro', 'donde-manda-marinero'))
resultados.append(analizarxletra('andres-calamaro', 'pasemos-a-otro-tema'))
resultados.append(analizarxletra('andres-calamaro', 'te-quiero-igual'))
resultados.append(analizarxletra('andres-calamaro', 'crimenes-perfectos'))
resultados.append(analizarxletra('andres-calamaro', 'ansia-en-plaza-francia'))
generados = 0
for gen in resultados:
    generados = generados + gen['generado']

print("total", len(resultados), "generado", generados)

