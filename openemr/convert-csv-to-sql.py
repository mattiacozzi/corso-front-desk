#!/usr/bin/env python3
import csv
from pathlib import Path

# Configurazioni
csv_file = "input.csv"        # file CSV di input
sql_file = "output.sql"       # file SQL di output
table_name = "patient_data"   # nome tabella

# encodings da provare
ENCODINGS_TO_TRY = ['utf-8', 'utf-8-sig', 'cp1252', 'iso-8859-1']

def detect_encoding(path, encodings=ENCODINGS_TO_TRY, sample_size=8192):
    """
    Prova ad aprire e leggere un campione del file con diversi encoding.
    Restituisce l'encoding riuscito, oppure None se nessuno funziona.
    """
    for enc in encodings:
        try:
            with open(path, 'r', encoding=enc) as f:
                f.read(sample_size)
            return enc
        except UnicodeDecodeError:
            continue
        except Exception:
            # altri errori (p.es. file non trovato) li lasciamo risalire altrove
            raise
    return None

csv_path = Path(csv_file)
if not csv_path.exists():
    raise SystemExit(f"File non trovato: {csv_file}")

detected = detect_encoding(csv_file)
if detected:
    print(f"Encoding rilevato: {detected}")
    open_errors = 'strict'
else:
    # fallback: usiamo latin-1 / cp1252 e permettiamo replacement per evitare crash
    detected = 'iso-8859-1'
    open_errors = 'replace'
    print("Nessun encoding automatico rilevato; userò 'iso-8859-1' con errori='replace' come fallback.")

# Apri il CSV con l'encoding scelto
with open(csv_file, newline='', encoding=detected, errors=open_errors) as f_in:
    sample = f_in.read(8192)
    f_in.seek(0)

    # prova a sniffare il delimitatore
    try:
        dialect = csv.Sniffer().sniff(sample)
        delimiter = dialect.delimiter
        print(f"Delimiter rilevato: '{delimiter}'")
    except csv.Error:
        delimiter = ','
        print("Impossibile rilevare il delimitatore, uso ',' di default.")

    reader = csv.reader(f_in, delimiter=delimiter)
    try:
        headers = next(reader)
    except StopIteration:
        raise SystemExit("CSV vuoto o senza intestazione.")

    # pulisci intestazioni
    headers = [h.strip() for h in headers]

    # scriviamo gli INSERT in output.sql (output in UTF-8)
    with open(sql_file, 'w', encoding='utf-8', newline='\n') as f_out:
        for row in reader:
            # normalizziamo la lunghezza della riga rispetto alle intestazioni
            if len(row) < len(headers):
                row += [''] * (len(headers) - len(row))
            elif len(row) > len(headers):
                # se ci sono più campi di intestazioni, concateniamo gli extra nell'ultimo campo
                row = row[:len(headers)-1] + [delimiter.join(row[len(headers)-1:])]

            values = []
            for val in row:
                if val is None:
                    values.append("' '")
                    continue
                v = val.strip()
                if v == "" or v.upper() == "NULL":
                    values.append("' '")
                else:
                    # escape apici singoli: O'Brien -> O''Brien
                    safe = v.replace("'", "''")
                    values.append(f"'{safe}'")

            sql = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join(values)});"
            f_out.write(sql + "\n")

print(f"Conversione completata — file generato: {sql_file} (in UTF-8)")
