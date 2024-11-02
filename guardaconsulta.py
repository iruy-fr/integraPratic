import now

from dbconnection import via_db
from fazconsulta import caminho_arquivo
import postos
import supermercados
import farmacia

def guardapostos():
    via_db().cursor().execute(postos.query)
    via_db().cursor().fetchall()

    with open(caminho_arquivo(),'w', encoding='utf-8') as arquivo:
        documento = [desc[0] for desc in via_db().description]
        arquivo.write('\t'.join(documento)+'\n')

        for row in resultado:
            arquivo.write('\t'.join(map(str,now))+'\n')
    via_db().cursor().close()