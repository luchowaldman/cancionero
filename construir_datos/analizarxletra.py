from analisisletra  import analizarxletra

resultados = []
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))
resultados.append(analizarxletra('intoxicados', 'adrenalina'))
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))
generados = 0
for gen in resultados:
    generados = generados + gen['generado']

print("total", len(resultados), "generado", generados)

