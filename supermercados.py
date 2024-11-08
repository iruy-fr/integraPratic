from fazconsulta import consulta_sexta


query = f"""
SELECT DISTINCT
    lpad('01', 2)
    || lpad('008', 3)
    || lpad(itemagro.item, 7, '0')
    || lpad(coalesce(itemagro.nrocodbar, '0'), 13, '0')
    || lpad(itemagro.grupo, 4, '0')
    || lpad('000', 3)
    || lpad(u_departamento.u_departamento_id, 3, '0')
    || rpad(u_removeacento(itemagro.descricao), 35)
    || lpad(' ', 3)
    || lpad(itemagro.unidade, 2)
    || lpad(' ', 2)
    || lpad(
        CASE itemagro.ebalanca
            WHEN 'S' THEN
                1
            ELSE
                0
        END, 1)
    || lpad(u_tribmerc.u_tribmerc_id, 3, '0')
    || lpad(coalesce(itemagro.nrocodbar, ' '), 20)
    || lpad(' ', 10)
    || lpad(coalesce((itemagro.pesoliquido * 100), 0), 10, '0')
    || lpad(itemagro.unidade, 2)
    || lpad('00000100', 8)
    || lpad(itemagro.ativo, 1)
    || lpad(' ', 2)
    || lpad(coalesce(itemagroestab.margemlucro, 0) * 100, 5, '0')
    || lpad('0000100', 7)
    || lpad('000000000000100', 15)
    || lpad(coalesce(itemagro.referencia, ' '), 20)
    || lpad(' ', 6)
    || lpad('0', 1)
    || lpad(coalesce((ncmporuf.aliquotaibptes + ncmporuf.aliquotaibptfednac) * 10000, 0), 10, '0')
    ||

/*       LPAD(COALESCE(itemagroestab.aliquotaibpt * 10000,0), 10, '0') ||*/ lpad(coalesce(regexp_replace(pclasfis.ncm, '[^[:digit:]]',
    ''), '0'), 8, '0')
    || '  '
    || lpad(coalesce(itemagro.trrcdanpitem, 0), 9, '0')
    || lpad(coalesce(itemagro.codcest, '0'), 7, '0')
    || lpad(coalesce((
        SELECT
            aliquotaesp
        FROM
            tribitem t
        WHERE
                t.tributacao = 29
            AND t.imposto = 26
            AND t.tributacao = itemagro.tributacao
    ), 0) * 100, 10, '0') linha
FROM
         itemagroestab
    INNER JOIN itemagro ON ( itemagro.item = itemagroestab.item )
    LEFT JOIN pclasfis ON ( pclasfis.clasfiscal = itemagro.clasfiscal )
    LEFT JOIN ncmporuf ON ( ncmporuf.ncm = pclasfis.clasfiscal )
                          AND ( ncmporuf.uf = 'RS' )
    INNER JOIN itemagro_u ON ( itemagro_u.item = itemagro.item )
    INNER JOIN itemgrupo ON ( itemgrupo.grupo = itemagro.grupo )
    INNER JOIN grupocontabil_u ON ( grupocontabil_u.grupocontabil = itemgrupo.grupocontabil )
    INNER JOIN u_departamento ON ( u_departamento.u_departamento_id = grupocontabil_u.u_departamento_id )
    INNER JOIN u_tribmerc ON ( u_tribmerc.u_tribmerc_id = itemagro_u.u_tribmerc_id )
    INNER JOIN u_vincnegdep ON ( u_vincnegdep.departamento = u_departamento.u_departamento_id )
WHERE
itemgrupo.grupo not in (880, 881)
 AND   ( itemagroestab.estab IN ( 1002, 1061, 1078, 1086,1100 ) )
    AND ( to_date(to_char(itemagro.ultalt, 'DD/MM/YYYY'), 'DD/MM/YYYY') >= TO_DATE('{consulta_sexta()}', 'DD/MM/YYYY') )
    AND ( u_vincnegdep.negocio IN (1, 2, 4, 5, 15)
          OR grupocontabil_u.grupocontabil = 38
          OR itemagro.grupo IN (   5,  23,  71,  151 , 365, 958,
                                 954,  445,  182,  1019, 1815, 1576,
                                 1708, 1897, 1966, 1664, 2158, 1602, 
                                 1664, 1801, 1802, 1865, 1501, 1550, 
                                 2010, 4000, 4001, 4002, 4003, 4004,
                                 4005, 4006, 4007, 4008, 4009,
                                 4010, 4011, 4012, 4013, 4014,
                                 4016, 4017, 4018, 4021, 4023,
                                 4025, 4027, 4029 ) )

           /* acima grupos da Farmácia

  /* AND (EXTRACT(HOUR FROM ITEMAGRO.ULTALT) BETWEEN 5 AND 19)

/*   AND ITEMAGROESTAB.USERID IN (SELECT USERID FROM PUSUARIO_U WHERE ESTAB IN (1002,1061,1078,1064,1072,1083))*/


UNION ALL



 /* Cadastro de Pessoas */

/* Pessoas Normais */

SELECT DISTINCT
    lpad('02', 2)
    || lpad('008', 3)
    || lpad(contamov.numerocm, 7, 0)
    ||
    CASE
        WHEN contamov.sexo = 'J' THEN
                '0'
        ELSE
            '1'
    END
    ||
    CASE
        WHEN associado = 'N' THEN
                1
        ELSE
            0
    END
    || rpad(contamov.nome, 30)
    || '000'
    || '000'
    || rpad(coalesce(rg, '0'), 18, '0')
    || rpad('0', 6, '0')
    || rpad('0', 11, '0')
    || rpad(nome, 50) linha
FROM
    contamov
WHERE
    ultalt >= TO_DATE('{consulta_sexta()}', 'DD/MM/YYYY')
UNION ALL



/* Pessoas Funcionario */

SELECT DISTINCT
    lpad('02', 2)
    || lpad('008', 3)
    || lpad(CAST(contamov.matfuncionario AS NUMBER), 7, 0)
    ||
    CASE
        WHEN contamov.sexo = 'J' THEN
                '0'
        ELSE
            '1'
    END
    ||
    CASE
        WHEN associado = 'N' THEN
                1
        ELSE
            0
    END
    || rpad(contamov.nome, 30)
    || '000'
    || '000'
    || rpad(coalesce(rg, '0'), 18, '0')
    || rpad('0', 6, '0')
    || rpad('0', 11, '0')
    || rpad(nome, 50) linha
FROM
    contamov
WHERE
        ultalt >= TO_DATE('{consulta_sexta()}', 'DD/MM/YYYY')
    AND contamov.matfuncionario IS NOT NULL
UNION ALL



/* Pessoas Associado */

SELECT DISTINCT
    lpad('02', 2)
    || lpad('008', 3)
    || lpad(CAST(contamov.matricula AS NUMBER), 7, 0)
    ||
    CASE
        WHEN contamov.sexo = 'J' THEN
                '0'
        ELSE
            '1'
    END
    ||
    CASE
        WHEN associado = 'N' THEN
                1
        ELSE
            0
    END
    || rpad(contamov.nome, 30)
    || '000'
    || '000'
    || rpad(coalesce(rg, '0'), 18, '0')
    || rpad('0', 6, '0')
    || rpad('0', 11, '0')
    || rpad(nome, 50) linha
FROM
    contamov
WHERE
        ultalt >= TO_DATE('{consulta_sexta()}', 'DD/MM/YYYY')
    AND contamov.matricula IS NOT NULL
UNION ALL



/* Cadastro de endereços */

/* Pessoas Normais */

SELECT DISTINCT
    '03'
    || '008'
    || lpad(contamov.numerocm, 7, 0)
    || '01'
    || rpad(contamov.nome, 30)
    || rpad(contamov.endereco, 30)
    || rpad(contamov.bairro, 15)
    || lpad(CAST(cidade.cidade AS NUMBER), 5, '0')
    || lpad(' ', 8, ' ')
    || lpad(coalesce(contamov.cep, '0'), 8, '0')
    || rpad(coalesce(contamov.cnpjf, '0'), 20)
    || rpad(coalesce(contamov.credencialagro, '0'), 20)
    || rpad(coalesce(contamov.telefone, ' '), 18, ' ')
    || lpad('0', 18, '0')
    || lpad(' ', 18, ' ')
    || rpad(coalesce(contamov.endereco, ' '), 60, ' ')
    || rpad(coalesce(to_number(regexp_replace(contamov.numeroend, '[^[:digit:]]')), 0), 60, ' ')
    || rpad(coalesce(contamov.complemento, ' '), 60, ' ')
    || rpad(coalesce(contamov.email, ' '), 60, ' ') linha
FROM
         contamov
    JOIN cidade ON ( cidade.cidade = contamov.cidade )
WHERE
    contamov.ultalt >= TO_DATE('{consulta_sexta()}', 'DD/MM/YYYY')
    AND contamov.matricula IS NOT NULL
    AND contamov.bairro IS NOT NULL
UNION ALL



/* Pessoas Funcionarios */

SELECT DISTINCT
    '03'
    || '008'
    || lpad(CAST(contamov.matfuncionario AS NUMBER), 7, 0)
    || '01'
    || rpad(contamov.nome, 30)
    || rpad(contamov.endereco, 30)
    || rpad(contamov.bairro, 15)
    || lpad(CAST(cidade.cidade AS NUMBER), 5, '0')
    || lpad(' ', 8, ' ')
    || lpad(coalesce(contamov.cep, '0'), 8, '0')
    || rpad(coalesce(contamov.cnpjf, '0'), 20)
    || rpad(coalesce(contamov.credencialagro, '0'), 20)
    || rpad(coalesce(contamov.telefone, ' '), 18, ' ')
    || lpad('0', 18, '0')
    || lpad(' ', 18, ' ')
    || rpad(coalesce(contamov.endereco, ' '), 60, ' ')
    || rpad(coalesce(to_number(regexp_replace(contamov.numeroend, '[^[:digit:]]')), 0), 60, ' ')
    || rpad(coalesce(contamov.complemento, ' '), 60, ' ')
    || rpad(coalesce(contamov.email, ' '), 60, ' ') linha
FROM
         contamov
    JOIN cidade ON ( cidade.cidade = contamov.cidade )
WHERE
        contamov.ultalt >= TO_DATE('{consulta_sexta()}', 'DD/MM/YYYY')
    AND contamov.matfuncionario IS NOT NULL
    
UNION ALL



/* Pessoas Associados */

SELECT DISTINCT
    '03'
    || '008'
    || lpad(CAST(contamov.matricula AS NUMBER), 7, 0)
    || '01'
    || rpad(contamov.nome, 30)
    || rpad(contamov.endereco, 30)
    || rpad(contamov.bairro, 15)
    || lpad(CAST(cidade.cidade AS NUMBER), 5, '0')
    || lpad(' ', 8, ' ')
    || lpad(coalesce(contamov.cep, '0'), 8, '0')
    || rpad(coalesce(contamov.cnpjf, '0'), 20)
    || rpad(coalesce(contamov.credencialagro, '0'), 20)
    || rpad(coalesce(contamov.telefone, ' '), 18, ' ')
    || lpad('0', 18, '0')
    || lpad(' ', 18, ' ')
    || rpad(coalesce(contamov.endereco, ' '), 60, ' ')
    || rpad(coalesce(to_number(regexp_replace(contamov.numeroend, '[^[:digit:]]')), 0), 60, ' ')
    || rpad(coalesce(contamov.complemento, ' '), 60, ' ')
    || rpad(coalesce(contamov.email, ' '), 60, ' ') linha
FROM
         contamov
    JOIN cidade ON ( cidade.cidade = contamov.cidade )
WHERE
        contamov.ultalt >= TO_DATE('{consulta_sexta()}', 'DD/MM/YYYY')
    AND contamov.matricula IS NOT NULL
    AND contamov.bairro IS NOT NULL
UNION ALL



/* Cadastro de Municipios */

SELECT DISTINCT
    '04'
    || lpad(cidade.cidade, 5, '0')
    || rpad(cidade.nome, 30)
    || lpad(cidade.uf, 2)
    || lpad(depara.ibge, 5, '0')
    || lpad('1058', 6, '0')
    || lpad(depara.uf, 2) dado
FROM
         u_depara_cidade depara
    JOIN cidade ON ( cidade.ibge = coalesce(depara.ibge, '10009') )
                   AND ( cidade.uf = coalesce(depara.dsuf, 'RS') )
"""