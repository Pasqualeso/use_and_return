-- CREAZIONE ORDINE
CREATE TABLE ORDINE(
   ID_ORDINE                      INTEGER  PRIMARY KEY,
   TITOLO_ANNUNCIO                VARCHAR(64) NOT NULL,
   IMMAGINE                       LONGBLOB    NOT NULL,
   IMPORTO_PAGAMENTO              INTEGER  NOT NULL,
   DATA_INSERIMENTO_ORDINE        DATE     NOT NULL,
   ID_UTENTE_RF_ORDINE            INTEGER  NOT NULL,
   CONSTRAINT FK_Id_Utente_Ordine FOREIGN KEY (ID_UTENTE_RF_ORDINE) REFERENCES UTENTE (ID)
)