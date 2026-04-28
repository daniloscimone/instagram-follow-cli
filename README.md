# Instagram Follow CLI

CLI cross‑platform per confrontare i follower/following di un account Instagram in modo conforme alle API ufficiali.

## Obiettivo
- Inserire un nome utente.
- Se l’account è privato, guidare l’utente nel login/autorizzazione tramite API ufficiali.
- Confrontare **following** vs **followers** e mostrare chi non ricambia.

> Nota: Instagram non offre API pubbliche anonime per questi dati. È necessario usare le **API ufficiali** con autenticazione e permessi.

## Requisiti
- Python 3.10+

## Installazione (sviluppo)
```bash
python -m venv .venv
source .venv/bin/activate  # su Windows: .venv\Scripts\activate
pip install -e .
