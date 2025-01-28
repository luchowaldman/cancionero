from analisisletra  import analizarxletra

resultados = []
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))
#resultados.append(analizarxletra('viejas-locas', 'adrenalina'))
resultados.append(analizarxletra('viejas-locas', 'Leganlizenla'))
resultados.append(analizarxletra('intoxicados', 'fuiste-lo-mejor'))
resultados.append(analizarxletra('intoxicados', 'casi-sin-pensar'))
resultados.append(analizarxletra('intoxicados', 'homero'))
resultados.append(analizarxletra('intoxicados', 'nunca-Quise'))
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))
generados = 0
for gen in resultados:
    generados = generados + gen['generado']

print("total", len(resultados), "generado", generados)

