import logging
import postos
import supermercados
import farmacia
from dbconnection import via_db
from fazconsulta import caminho_arquivo


def guardapostos():
    logging.basicConfig(filename='consulta.log', filemode='w', level=logging.DEBUG, )
    try:
        execute = via_db().cursor().execute(postos.query)
        print(execute)
        resultados = execute.fetchall()
        if resultados:
            with open(caminho_arquivo(), 'w', encoding='utf-8') as arquivo:
                cabecalho = ['LINHA']
                arquivo.write('\t'.join(cabecalho) + '\n')

                for row in resultados:
                    linha_formatada = '\t'.join(map(str, row)) + '\n'
                    arquivo.write(linha_formatada)

            print(f"Salvos em:{caminho_arquivo()}")

    except Exception as e:
        logging.error(f"Erro ao executar a consulta: {postos.query}", exc_info=True)
        print(f"Ocorreu um erro inesperado: {str(e)}")

    finally:
        via_db().cursor().close()

def guardasupermercados():
    logging.basicConfig(filename='consulta.log', filemode='w', level=logging.DEBUG)
    try:
        execute = via_db().cursor().execute(supermercados.query)
        print(execute)
        resultados = execute.fetchall()
        if resultados:
            with open(caminho_arquivo(),'w', encoding='utf-8') as arquivo:
               cabecalho = ['LINHA']
               arquivo.write('\t'.join(cabecalho)+'\n')

               for row in resultados:
                   linha_formatada = '\t'.join(map(str, row))+'\n'
                   arquivo.write(linha_formatada)

            print(f"Salvos em:{caminho_arquivo()}")

    except Exception as e:
        logging.error(f"Erro ao executar a consulta: {supermercados.query}", exc_info=True)
        print(f"Ocorreu um erro inesperado: {str(e)}")

    finally:
        via_db().cursor().close()

def guardafarmacia():
    logging.basicConfig(filename='consulta.log', filemode='w', level=logging.DEBUG, )
    try:
        execute = via_db().cursor().execute(farmacia.query)
        print(execute)
        resultados = execute.fetchall()
        if resultados:
            with open(caminho_arquivo(), 'w', encoding='utf-8') as arquivo:
                cabecalho = ['LINHA']
                arquivo.write('\t'.join(cabecalho) + '\n')

                for row in resultados:
                    linha_formatada = '\t'.join(map(str, row)) + '\n'
                    arquivo.write(linha_formatada)

            print(f"Salvos em:{caminho_arquivo()}")

    except Exception as e:
        logging.error(f"Erro ao executar a consulta: {farmacia.query}", exc_info=True)
        print(f"Ocorreu um erro inesperado: {str(e)}")

    finally:
        via_db().cursor().close()