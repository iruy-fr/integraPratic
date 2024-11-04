import logging
import re
import clientes,postos,supermercados,farmacia
import fazconsulta
from dbconnection import via_db
from fazconsulta import caminho_arquivo,caminho_clientes, cabecalho_cad

def guardapostos():
    logging.basicConfig(filename='consulta.log', filemode='w', level=logging.DEBUG, )
    try:
        execute = via_db().cursor().execute(postos.query)
        resultados = execute.fetchall()
        if resultados:
            with open(caminho_arquivo(), 'w', encoding='utf-8') as arquivo:
                cabecalho = [f'{fazconsulta.cabecalho_cad()}']
                arquivo.write('\t'.join(cabecalho) + '\n')

                for row in resultados:
                    linha_formatada = '\t'.join(map(str, row)) + '\n'
                    arquivo.write(linha_formatada)

    except Exception as e:
        logging.error(f"Erro ao executar a consulta: {postos.query}", exc_info=True)
        print(f"Ocorreu um erro inesperado: {str(e)}")

    finally:
        via_db().cursor().close()

def guardasupermercados():
    logging.basicConfig(filename='consulta.log', filemode='w', level=logging.DEBUG)
    try:
        execute = via_db().cursor().execute(supermercados.query)
        resultados = execute.fetchall()
        if resultados:
            with open(caminho_arquivo(),'w', encoding='utf-8') as arquivo:
               cabecalho = [f'{fazconsulta.cabecalho_cad()}']
               arquivo.write('\t'.join(cabecalho)+'\n')

               for row in resultados:
                   linha_formatada = '\t'.join(map(str, row))+'\n'
                   arquivo.write(linha_formatada)

    except Exception as e:
        logging.error(f"Erro ao executar a consulta: {supermercados.query}", exc_info=True)
        print(f"Ocorreu um erro inesperado: {str(e)}")

    finally:
        via_db().cursor().close()

def guardafarmacia():
    logging.basicConfig(filename='consulta.log', filemode='w', level=logging.DEBUG, )
    try:
        execute = via_db().cursor().execute(farmacia.query)
        resultados = execute.fetchall()
        if resultados:
            with open(caminho_arquivo(), 'w', encoding='utf-8') as arquivo:
                cabecalho = [f'{fazconsulta.cabecalho_cad()}']
                arquivo.write('\t'.join(cabecalho) + '\n')

                for row in resultados:
                    linha_formatada = '\t'.join(map(str, row)) + '\n'
                    arquivo.write(linha_formatada)

    except Exception as e:
        logging.error(f"Erro ao executar a consulta: {farmacia.query}", exc_info=True)
        print(f"Ocorreu um erro inesperado: {str(e)}")

    finally:
        via_db().cursor().close()

def guardaclientes():
    logging.basicConfig(filename='consulta.log', filemode='w', level=logging.DEBUG)
    try:
        execute = via_db().cursor().execute(clientes.query)
        resultados = execute.fetchall()
        if resultados:
            with open(caminho_clientes(), 'w', encoding='utf-8') as arquivo:
                for row in resultados:
                    if row[1] == '9' and \
                            1 <= len(str(row[0])) < 8 and \
                            re.match(r'^[0-9]{0,9}$', str(row[0])):
                            linha_formatada = '72'+(str(row[0]).zfill(7))+'9'
                            arquivo.write(linha_formatada + '\n')

    except Exception as e:
        logging.error(f"Erro ao executar a consulta: {farmacia.query}", exc_info=True)
        print(f"Ocorreu um erro inesperado: {str(e)}")

    finally:
        via_db().cursor().close()