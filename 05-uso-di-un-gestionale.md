# Lezione 7 - Uso di un gestionale

<p align="center" style="width=100%;">
  <img width="100px" src="img/openemr-logo.png"  border="0px">
</p>

### Contenuti

1. [Cos'è un software gestionale](#cosè-un-software-gestionale)
    - [Gestionali locali e di rete](#gestionali-locali-e-di-rete)
    - [Funzioni principali](#funzioni-principali)
    - [Account](#account)
1. [openEMR](#openemr)
    - [Connessione](#connessione)
    - [Agenda]()
        - [Nuovo appuntamento]()
        - [Modifica un appuntamento]()
    - [Anagrafiche]()
        - [Nuova anagrafica]()
        - [Modifica anagrafica]()
    - [Promemoria]()
    - [Supporto]()
        - []()
        - []()
1. [Fonti](#fonti)

<div style="page-break-after: always;"></div>


# Cos'è un software gestionale

I software gestionali per studi medici sono applicazioni progettate per digitalizzare e semplificare le attività amministrative, cliniche e organizzative di uno studio medico. 

Consentono di **centralizzare le informazioni sui pazienti**, automatizzare prenotazioni e fatturazione, gestire **cartelle cliniche elettroniche** e migliorare la comunicazione tra il personale.

L'insieme di dati che un gestionale utilizza si chiama **database**.

## Gestionali locali e di rete

Un software gestionale può essere **installato e utilizzato su un solo computer**. Parliamo allora di un gestionale *in locale*.

Il limite principale di un gestionale locale è che può essere utilizzato da una sola postazione.

La scelta migliore è un gestionale **installato su un computer (server) che viene utilizzato a distanza** da altri computer  (client). Parliamo allora di un gestionale *in rete*. 

I client possono accedere a gestionale di rete tramite un normale browser web.

È la scelta migliore quando dobbiamo facilitare il lavoro di più persone che operano insieme, anche se è più difficile da impostare.

Nel nostro esempio useremo un gestionale in rete, in cui il ruolo di server è svolto dal computer del docente.

## Funzioni principali

- **Anagrafica pazienti**  
  Memorizzazione sicura dei dati anagrafici, contatti, recapiti d'emergenza e storia clinica di base.

- **Cartella clinica elettronica (EHR/EMR)**  
  Registrazione delle visite, referti, diagnosi, prescrizioni, allegati (esami, immagini) e note cliniche con tracciabilità delle modifiche.

- **Agenda e prenotazioni**  
  Calendario condiviso, gestione appuntamenti (manuale e online), promemoria automatici via SMS/Email e lista d'attesa.

- **Gestione fatturazione e pagamenti**  
  Emissione di fatture e ricevute, integrazione con sistemi di cassa/pos, gestione pagamenti, note spese e reportistica finanziaria.

- **Refertazione e integrazione con laboratori**  
  Inserimento referti, importazione/esportazione risultati di laboratorio e interfacce con sistemi esterni.

- **Gestione scadenze e ricette**  
  Promemoria per rinnovi prescrizioni, vaccini e follow-up clinici.

## Account

- **Amministratore (Admin)**  
  - Pieno controllo del sistema: creazione/gestione account, configurazioni generali, visibilità completa su dati amministrativi e finanziari.  
  - Competenze: impostare ruoli, backup, aggiornamenti, integrazioni con fatturazione/gestionali esterni.  
  - Note: deve avere permessi di sicurezza limitati ai soli responsabili della privacy.

- **Medico**  
  - Accesso alle cartelle cliniche dei propri pazienti, possibilità di scrivere note cliniche, prescrivere farmaci, caricare referti e visualizzare l'agenda personale.  
  - Permessi limitati alla modifica delle informazioni cliniche (spesso non può accedere ai report economici completi se non previsto).

- **Front Desk / Reception**  
  - Gestisce prenotazioni, check-in/check-out, aggiornamento anagrafiche, incassi e comunicazioni con i pazienti.  
  - Accesso parziale alle cartelle (visualizzazione anagrafica e storico appuntamenti) ma normalmente non alle note cliniche dettagliate.

- **Ruoli aggiuntivi (opzionali)**  
  - **Contabile**: accesso a fatturazione, report finanziari e gestione pagamenti.  
  - **Infermiere/Collaboratore**: accesso a informazioni cliniche rilevanti e possibilità di aggiornare triage o monitoraggi.

<div style="page-break-after: always;"></div>

# openEMR

**OpenEMR** è un software open source per la gestione delle cartelle cliniche elettroniche (EHR) e per la pianificazione delle attività di uno studio medico.

È uno dei sistemi più diffusi a livello mondiale perché gratuito, flessibile e conforme a diversi standard internazionali di sicurezza e privacy.

## Connessione

Per collegarci al gestionale di rete che useremo come esempio, dobbiamo collegarci alla rete wifi:

    LAN-simulator

Non sono richieste password. Apriamo poi un **browser** e digitiamo l'indirizzo:

    192.168.1.223:8080/openemr

Accediamo con i dati forniti dal docente.

L'account che ci è stato fornito è un **account di front desk**.

## Agenda

L'agenda è l'elemento fondamentale di questo software gestionale, almeno dal punto di vista del front desk.

Sono indicati gli **orari di disponibilità dei medici** e gli appuntamenti già presi.

L'agenda è divisa in diversi calendari, per poter gestire gli appuntamenti di più persone contemporaneamente.

IMMAGINE

### Nuovo appuntamento

PARLA BENE DI COME SI TROVA UNO SLOT DISPONIBILE

### Modifica un appuntamento

## Anagrafiche

### Nuova anagrafica

QUALI SONO I CAMPI FONDAMENTALI

### Modifica anagrafica

## Promemoria



## Supporto


<div style="page-break-after: always;"></div>

# Fonti
- [https://www.open-emr.org/wiki/](https://www.open-emr.org/wiki/)