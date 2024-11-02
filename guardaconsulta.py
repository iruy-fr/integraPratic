import postos
import supermercados
import farmacia
from dbconnection import via_db
from fazconsulta import caminho_arquivo


def guardapostos():
    try:
        via_db().cursor().execute(postos.query)
        resultados = via_db().cursor().fetchall()


        if resultados:
            with open(caminho_arquivo(),'w', encoding='utf-8') as arquivo:
                documento = [desc[0] for desc in via_db().description]
                arquivo.write('\t'.join(documento)+'\n')

                for row in resultados:
                    arquivo.write('\t'.join(map(str,row))+'\n')
            print(f"Salvos em:{caminho_arquivo()}")
        else:
            print((f"Não foi salvo nenhum arquivo"))

    except Exception as e:
        print(f"Erro {e}")

    finally:
        via_db().cursor().close()

def guardasupermercados():
    try:
        via_db().cursor().execute(supermercados.query)
        resultados = via_db().cursor().fetchall()

        if resultados:
            with open(caminho_arquivo(), 'w', encoding='utf-8') as arquivo:
                documento = [desc[0] for desc in via_db().description]
                arquivo.write('\t'.join(documento) + '\n')

                for row in resultados:
                    arquivo.write('\t'.join(map(str, row)) + '\n')
            print(f"Salvos em:{caminho_arquivo()}")
        else:
            print((f"Não foi salvo nenhum arquivo"))

    except Exception as e:
        print(f"Erro {e}")

    finally:
        via_db().cursor().close()

def guardafarmacia():
    try:
        via_db().cursor().execute(farmacia.query)
        resultados = via_db().cursor().fetchall()

        if resultados:
            with open(caminho_arquivo(), 'w', encoding='utf-8') as arquivo:
                documento = [desc[0] for desc in via_db().description]
                arquivo.write('\t'.join(documento) + '\n')

                for row in resultados:
                    arquivo.write('\t'.join(map(str, row)) + '\n')
            print(f"Salvos em:{caminho_arquivo()}")
        else:
            print((f"Não foi salvo nenhum arquivo"))

    except Exception as e:
        print(f"Erro {e}")

    finally:
        via_db().cursor().close()