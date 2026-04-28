# Instagram Follow CLI

CLI cross-platform per confrontare follower e following di Instagram usando solo l'export ufficiale Instagram, senza API personali e senza scraping.

## Open Source

Questo repository è pensato per essere open source: chiunque può usarlo, modificarlo e proporre miglioramenti.
La licenza del progetto è [MIT](LICENSE).

## Obiettivo

- Chiedere interattivamente l'username.
- Chiedere username o link all'account.
- Caricare l'export ufficiale Instagram dell'utente.
- Mostrare chi segue l'account ma non viene ricambiato.

> Nota: questo progetto non usa API personali. Per gli account privati funziona tramite export ufficiale Instagram scaricato dopo login dell'utente.

## Requisiti

- Python 3.10+

## Installazione

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Su Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

## Uso

```bash
instagram-follow-cli
```

Il comando chiede lo username e il percorso dell'export ufficiale Instagram.

Per avere subito un'esecuzione completa, puoi passare l'export così:

```bash
instagram-follow-cli --username danilo --export ./instagram-export.zip
```

Puoi passare anche una cartella estratta oppure un file `.json` dell'export. Il tool cerca automaticamente follower e following dentro i contenuti scaricati da Instagram.

## Struttura

- `src/instagram_follow_cli/cli.py`: interfaccia CLI.
- `src/instagram_follow_cli/instagram_export.py`: lettura dell'export ufficiale Instagram.
- `src/instagram_follow_cli/instagram_api.py`: stub conservato solo per compatibilità futura.
- `src/instagram_follow_cli/compare.py`: logica di confronto tra follower e following.
- `pyproject.toml`: metadata, dipendenze e script console.
- `LICENSE`: licenza open source MIT.

## Aspetto del terminale

La CLI usa `rich` per un banner iniziale, pannelli colorati, prompt chiari e una tabella finale ordinata per gli account non ricambiati.

## Sviluppo

```bash
python -m pip install -e .
instagram-follow-cli
```

