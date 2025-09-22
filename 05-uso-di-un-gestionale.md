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
    - [Agenda]( #agenda)
        - [Nuovo appuntamento](#nuovo-appuntamento)
        - [Modifica di un appuntamento](#modifica-di-un-appuntamento)
    - [Anagrafiche](#anagrafiche)
        - [Nuova anagrafica](#nuova-anagrafica)
    - [Supporto](#supporto)
1. [Attività](#attività)
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

<p align="center" style="width=100%;">
  <img width="400px" src="img/oe-login.png" border="1px">
</p>

L'account che ci è stato fornito è un **account di front desk**. 

> Gli altri account possibili sono **medico**, **contabile** e **amministratore**.

Ogni account ha permessi e può compiere diverse attività, e pertanto ognuno ha una barra del menu leggermente diversa.

Al login, notiamo prima di tutto che l'interfaccia di openEMR è strutturata a **schede**, che possono essere gestite come in un browser web.

## Agenda

L'agenda è la scheda fondamentale di questo software gestionale (insieme all'anagrafica paziente), almeno dal punto di vista del front desk.

In agenda sono indicati gli **orari di disponibilità dei medici** e gli appuntamenti già presi.

L'agenda è divisa in diversi calendari, per poter gestire gli appuntamenti di più persone contemporaneamente.

<p align="center" style="width=100%;">
  <img width="670px" src="img/oe-fullday.png" border="1px">
</p>

L'interfaccia è molto simile a quella di Google Calendar.

### Nuovo appuntamento

Basta **selezionare il calendario corretto** e cliccare sul `+`. In alternativa possiamo fare clic direttamente su una zona vuota del calendario.

Le opzioni sono ancora una volta molto simili a quelle di Google Calendar.

<p align="center" style="width=100%;">
  <img width="380px" src="img/oe-new.png" border="1px">
</p>

Attenzione a impostare il tipo di evento a *Visita in studio*, a scegliere l'operatore (cioè il medico) e il paziente corretti.

<p align="center" style="width=100%;">
  <img width="350px" src="img/oe-searchpat.png" border="1px">
</p>

Dobbiamo impostare la durata dell'evento in minuti (default=15).

Possiamo anche impostare eventi **ricorrenti**, come riunioni, ecc.

Per essere certe di creare l'evento in un momento in cui il medico è disponibile, possiamo usare il bottone **Cerca disponibilità** (*Find available*). Ci verranno mostrate diverse opzioni di data e orario in cui il medico indicato non ha altri appuntamenti.

<p align="center" style="width=100%;">
  <img width="550px" src="img/oe-avail.png" border="1px">
</p>

### Modifica di un appuntamento

Per modificare un appuntamento già creato, basta fare doppio clic sull'appuntamento stesso. Vedremo la stessa interfaccia che abbiamo visto durante la creazione di un evento.

> Se stiamo modificando un evento ricorrente, ci verrà chiesto se vogliamo applicare le modifiche a tutti gli eventi, a quelli futuri o solo a quello corrente.

## Anagrafiche

Come sappiamo, un'anagrafica è la raccolta dei dati personali di un paziente.

Possiamo cercare nelle anagrafiche già esistenti mediante il **campo di ricerca in alto a destra** oppure selezionando **Finder** dal menu.

<p align="center" style="width=100%;">
  <img width="670px" src="img/oe-finder.png" border="1px">
</p>

Selezionando un paziente, potremo vedere i suoi dati anagrafici e gli appuntamenti futuri presso lo studio.

<p align="center" style="width=100%;">
  <img width="670px" src="img/oe-schedapat.png" border="1px">
</p>

Per modificare un'anagrafica (ad esempio per aggiornare un numero di telefono), è sufficiente cercare il paziente e aprire la sua scheda. 

Facendo clic sull'icona della matita possiamo modificare i dettagli del paziente.

### Nuova anagrafica

Per creare una nuova anagrafica, selezioniamo **Paziente** dal menu e poi **Nuovo/Cerca**. Potremmo anche usare questa interfaccia per cercare i pazienti, ma i metodi mostrati in precedenza sono senza dubbio più comodi.

Quando compiliamo un'anagrafica, non è necessario compilare **tutti i campi**, ma solo quelli importanti rispetto al nostro modo di lavorare.

> Possiamo spostarci al campo successivo **senza usare il mouse** usando il tasto `TAB` sulla tastiera.

<p align="center" style="width=100%;">
  <img width="450px" src="img/oe-anag-1.png" border="1px"><br>Dati anagrafici fondamentali
</p>

<p align="center" style="width=100%;">
  <img width="450px" src="img/oe-anag-2.png" border="1px"><br>Dati di contatto fondamentali
</p>

## Supporto

Possiamo leggere la **wiki** di openEMR per studiare tutte le sue funzionalità (vedi il link nelle Fonti), oppure chiedere supporto sul **forum di openEMR** ([https://community.open-emr.org/](https://community.open-emr.org/)).

<div style="page-break-after: always;"></div>

# Attività



<div style="page-break-after: always;"></div>

# Fonti
- [https://www.open-emr.org/wiki/](https://www.open-emr.org/wiki/)