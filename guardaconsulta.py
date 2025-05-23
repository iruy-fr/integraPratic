import re, logging, os
import clientes,postos,supermercados,farmacia, restaurante
from dbconnection import via_db
from fazconsulta import caminho_arquivo,caminho_clientes, cabecalho_cad, caminho_cad


def guardapostos():
    logging.basicConfig(filename=r'C:\Trab99\consulta.log', filemode='w', level=logging.DEBUG)
    try:
        execute = via_db().cursor().execute(postos.query)
        resultados = execute.fetchall()
        if resultados:
            with open(caminho_arquivo(), 'w', encoding='cp1252') as arquivo:
                cabecalho = [f'{cabecalho_cad()}']
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
    logging.basicConfig(filename=r'C:\Trab99\consulta.log', filemode='w', level=logging.DEBUG)
    try:
        execute = via_db().cursor().execute(supermercados.query)
        resultados = execute.fetchall()
        if resultados:
            with open(caminho_arquivo(),'w', encoding='cp1252') as arquivo:
               cabecalho = [f'{cabecalho_cad()}']
               arquivo.write('\t'.join(cabecalho)+'\n')

               for row in resultados:
                   linha_formatada = '\t'.join(map(str, row))+'\n'
                   arquivo.write(linha_formatada)

    except Exception as e:
        logging.error(f"Erro ao executar a consulta: {supermercados.query}", exc_info=True)
        print(f"Ocorreu um erro inesperado: {str(e)}")

    finally:
        via_db().cursor().close()

def guardarestaurante():
    logging.basicConfig(filename=r'C:\Trab99\consulta.log', filemode='w', level=logging.DEBUG)
    try:
        execute = via_db().cursor().execute(supermercados.query)
        resultados = execute.fetchall()
        if resultados:
            with open(caminho_arquivo(),'w', encoding='cp1252') as arquivo:
               cabecalho = [f'{cabecalho_cad()}']
               arquivo.write('\t'.join(cabecalho)+'\n')

               for row in resultados:
                   linha_formatada = '\t'.join(map(str, row))+'\n'
                   arquivo.write(linha_formatada)

    except Exception as e:
        logging.error(f"Erro ao executar a consulta: {restaurante.query}", exc_info=True)
        print(f"Ocorreu um erro inesperado: {str(e)}")

    finally:
        via_db().cursor().close()

def guardafarmacia():
    logging.basicConfig(filename=r'C:\Trab99\consulta.log', filemode='w', level=logging.DEBUG)
    try:
        execute = via_db().cursor().execute(farmacia.query)
        resultados = execute.fetchall()
        if resultados:
            with open(caminho_arquivo(), 'w', encoding='cp1252') as arquivo:
                cabecalho = [f'{cabecalho_cad()}']
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
            with open(caminho_clientes(), 'w', encoding='cp1252') as arquivo:
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


def formatador_cad():
    logging.basicConfig(
        filename=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'format.log'),
        filemode='a',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    try:
        with open(caminho_cad(),'w', encoding='cp1252') as arquivo:
            for resultado in [f'{caminho_arquivo()}',f'{caminho_clientes()}']:
                with open(resultado, 'r', encoding='cp1252') as r:
                    arquivo.writelines(r)
                    logging.info(f"Arquivo concatenado gerado com sucesso em {caminho_cad()} com o arquivo {caminho_arquivo()} e clientes {caminho_clientes()}")
    except Exception as e:
        logging.error(f"Erro ao executar a concatenação", exc_info=True)
        print(f"Ocorreu um erro inesperado: {str(e)}")