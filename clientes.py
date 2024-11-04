query = """
SELECT U_PRATTIC_PESSOAS.CODPESSOA,    
       CASE COALESCE((SELECT CONCEITOPESSOA.NUMEROCM
                         FROM CONCEITOPESSOA   
                         JOIN CONCEITO ON CONCEITO.CONCEITO = CONCEITOPESSOA.CONCEITO
                        WHERE (CONCEITO.VENDABLOQUNF = 'S')
                         AND (CONCEITOPESSOA.NUMEROCM = CONTAMOV.NUMEROCM)),0)
                         WHEN 0 THEN
                          CASE COALESCE((SELECT PDUPREC.CLIENTE
                                            FROM PDUPREC
                                           WHERE (PDUPREC.QUITADA = 'N')
                                            AND (PDUPREC.CLIENTE = CONTAMOV.NUMEROCM)
                                            AND (PDUPREC.DTVENCTO < (SYSDATE-10))
                                            AND(ROWNUM = 1)),0)
                                            WHEN 0 THEN
                                             CASE COALESCE((SELECT PCHEQREC.CLIENTE
                                                               FROM PCHEQREC
                                                              WHERE (PCHEQREC.DTLANCA IS NULL)
                                                               AND (PCHEQREC.DTESTORNODEP IS NOT NULL)
                                                               AND(PCHEQREC.DTBOMPARA < (SYSDATE-10))
                                                               AND(PCHEQREC.CLIENTE = CONTAMOV.NUMEROCM)
                                                               AND (ROWNUM = 1)),0)
                                                               WHEN 0 THEN '0'
                                                                      ELSE '9'
                                                               END              
                                                                      ELSE '9'
                                                               END
                                                                      ELSE '9'    
                                                               END AS BLOQ
                                                                 FROM CONTAMOV
                                                                 LEFT JOIN U_PRATTIC_PESSOAS ON(U_PRATTIC_PESSOAS.NUMEROCM = CONTAMOV.NUMEROCM)
"""