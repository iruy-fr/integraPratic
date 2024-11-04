from fazconsulta import caminho_cad,caminho_arquivo,caminho_clientes


def formatador_cad():
    with open(caminho_cad(),'w', encoding='utf-8') as arquivo:
        for resultado in [f'{caminho_arquivo()}',f'{caminho_clientes()}']:
            with open(resultado, 'r', encoding='utf-8') as r:
                arquivo.writelines(r)