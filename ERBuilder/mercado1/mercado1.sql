/*============================================================================*/
/* DBMS: PostgreSQL 11*/
/* Created on : 09/14/2019 7:49:46 PM                                           */
/*============================================================================*/


/*============================================================================*/
/*                                  TABLES                                    */
/*============================================================================*/
CREATE TABLE "precos1" (
  "preco_id"           SERIAL NOT NULL,
  "nome_produto"       VARCHAR(64) NOT NULL,
  "valor"              DOUBLE PRECISION,
  "data"               DATE NOT NULL,
CONSTRAINT "PK_precos1" PRIMARY KEY ("preco_id")
)
;

CREATE TABLE "precos2" (
  "preco_id"           SERIAL NOT NULL,
  "nome_produto"       VARCHAR(64) NOT NULL,
  "valor"              DOUBLE PRECISION,
  "data"               DATE NOT NULL,
CONSTRAINT "PK_precos2" PRIMARY KEY ("preco_id")
)
;

