from analisisletra  import analizarxletra

resultados = []
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))
#resultados.append(analizarxletra('viejas-locas', 'adrenalina'))
#resultados.append(analizarxletra('viejas-locas', '638'))
resultados.append(analizarxletra('intoxicados', 'fuego'))
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))
#resultados.append(analizarxletra('intoxicados', 'esta-saliendo-el-sol'))
generados = 0
for gen in resultados:
    generados = generados + gen['generado']

print("total", len(resultados), "generado", generados)

