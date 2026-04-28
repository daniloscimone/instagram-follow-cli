# Instagram Follow CLI

Uno strumento CLI semplice e pulito per confrontare i tuoi follower e following su Instagram, usando solo l'export ufficiale dei dati. **Niente API personali, niente scraping, niente automazioni.**

## 🎯 A cosa serve

Questo tool ti aiuta a scoprire **chi segui ma che non ti segue indietro** su Instagram. Funziona scaricando i tuoi dati ufficiali tramite Meta (il proprietario di Instagram) e confrontandoli localmente nel tuo computer, completamente offline.

### Caratteristiche

✅ Usa solo l'export ufficiale di Meta  
✅ Nessuna credenziale personale richiesta  
✅ Nessun scraping, nessuna automazione  
✅ Completamente locale (offline dopo il download)  
✅ Output colorato e facile da leggere  
✅ Completamente open source  

### Cosa non fa

❌ Non usa le API di Instagram  
❌ Non accede al tuo account con credenziali  
❌ Non fa scraping web  
❌ Non interagisce automaticamente con Instagram  

## 📋 Requisiti

- Python 3.10 o superiore

## 🚀 Installazione rapida

### macOS e Linux

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

## 💻 Uso

Il modo più semplice per iniziare è:

```bash
python3 main.py
```

Il programma ti guida passo dopo passo:

1. **Username**: Inserisci il tuo nome utente Instagram
2. **Export**: Scegli se hai già scaricato il file o se devi ancora farlo
3. **Caricamento**: Trascina il file nel terminale oppure incolla il percorso
4. **Risultati**: Visualizza la lista colorata degli account non ricambiati

### Con opzioni

Se preferisci saltare alcuni passaggi:

```bash
python3 main.py --export /percorso/al/file.zip
```

## 📦 Come ottenere l'export da Instagram/Meta

### Passaggi esatti

1. Accedi a **Instagram.com** e vai alle **Impostazioni**
2. Vai su **Il tuo account** → **Scarica i tuoi dati**
3. Meta ti chiede il tipo di scaricamento:
   - **Intervallo di date**: Seleziona `Sempre`
   - **Formato**: Seleziona `JSON`
   - **Voci**: Seleziona `Follower e persone/Pagine seguite`
4. Scarica il file (di solito `.zip` o cartella)
5. Usa il file con il programma

### Formati supportati

- 📦 File `.zip` dell'export
- 📁 Cartella estratta dell'export
- 📄 File `followers_1.json` isolato

## 📊 Output

Il programma ti mostra:

- **Numero totale** di follower e following caricati
- **Tabella ordinata** con gli account che segui ma non ti seguono indietro
- **Nomi utente** pronti da copiare o verificare

Esempio di output:

```
Account seguiti da @tuousername
    che non seguono indietro

┏━━━━━┳━━━━━━━━━━━━━━━━┓
┃   # ┃ Username       ┃
┡━━━━━╇━━━━━━━━━━━━━━━━┩
│   1 │ account1       │
│   2 │ account2       │
│   3 │ account3       │
└─────┴────────────────┘
```

## 📁 Struttura del progetto

```
instagram-follow-cli/
├── main.py                              # Punto di avvio
├── src/instagram_follow_cli/
│   ├── __init__.py
│   ├── cli.py                          # Interfaccia CLI
│   ├── instagram_export.py              # Parser export
│   └── compare.py                       # Logica comparazione
├── tests/                               # Test automatici
├── pyproject.toml                       # Configurazione Python
├── LICENSE                              # MIT License
└── README.md                            # Questo file
```

## 🔧 Sviluppo

Se vuoi modificare il codice:

```bash
pip install -e .
python3 main.py
python -m unittest discover -s tests
```

## 📄 Licenza

Progetto distribuito sotto licenza **MIT**. Libero da usare, modificare e distribuire.

## 🤝 Contribuzioni

Segnalazioni di bug, suggerimenti e pull request sono benvenuti! Questo è un progetto open source pensato per la comunità.

## ⚠️ Disclaimer

Questo tool opera **esclusivamente** sui dati che esporti tu stesso da Meta. Non fa alcun accesso a Instagram per tuo conto e non memorizza dati. Usa le API ufficiali di Meta solo per il download iniziale del file.

