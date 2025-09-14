# Installazione di OpenEMR

Istruzioni [qui](https://www.open-emr.org/wiki/index.php/OpenEMR_7.0.3_Linux_Installation).

1. Scaricare dal sito ufficiale ed estrarre l'archivio:

    ```bash
    tar -pxvzf openemr-7.0.3.tar.gz
    ```
    
1. Rinominare la cartella solo come `openemr` e spostarla nella cartella `htdocs` di XAMPP:
    
    ```bash
    sudo mv openemr /opt/lampp/htdocs
    ```

1. Cambiare il nome del file `Cpdf.php` nella cartella di PHP (leggi [qui](https://www.open-emr.org/wiki/index.php/XAMPP_and_OpenEMR_Installation_in_OS_X#Download)):

    ```bash
    sudo mv /opt/lampp/lib/php/Cpdf.php /opt/lampp/lib/php/Cpdf.php.backup
    ```

1. Avviare XAMPP.

1. Visitare [http://localhost/openemr](http://localhost/openemr) e seguire le istruzioni di installazione.

1. Dati per l'installazione:

    | nome                  | commento                                          | valore          |
    |-----------------------|---------------------------------------------------|-----------------|
    | server host           | IP del server MySQL                               | `192.168.1.223` |
    | database name         | il nome del db in PHPmyAdmin                      | `openemr`       |
    | login name            | username per MySQL                                | `openemr`       |
    | password              | pass dell'utente sopra                            | `administrator` |
    | root account          | utente root di MySQL, crea l'utente sopra e il db | `root`          |
    | root password         | vedi tabella utenti in PHPmyAdmin                 | `lan`           |
    | user hostname         | IP del server PHP                                 | `192.168.1.223` |
    | initial login name    | nome amministratore                               | `administrator` |
    | initial user password | password amministratore                           | `administrator` |

1. Al passo 4 dell'installazione viene richiesto di modificare un file di configurazione di Apache:

    ```bash
    sudo cp /opt/lampp/apache2/conf/httpd.conf /opt/lampp/apache2/conf/httpd.conf.backup
    sudo nano /opt/lampp/apache2/conf/httpd.conf
    ```

    Aggiungere queste righe alla fine del file:
    
    ```php
    <Directory "/opt/lampp/htdocs/openemr">
        AllowOverride FileInfo
        Require all granted
    </Directory>
    <Directory "/opt/lampp/htdocs/openemr/sites">
        AllowOverride None
    </Directory>
    <Directory "/opt/lampp/htdocs/openemr/sites/*/documents">
        Require all denied
    </Directory>
    ```
1. Procedere con l'installazione. Al termine riavviare il server Apache.

1. Il gestionale è disponibile all'indirizzo:

        https://localhost/openemr

    oppure:

        [IP-address]/openemr

1. Per importare i dati degli utenti, importo da PHPmyAdmin nella tabella `patient_data` il file `patient-dump.sql`.