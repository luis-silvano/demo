"""Prepara um envio fictício para um parceiro, sem executar chamadas de rede."""

import os


def resolve_token() -> str:
    """Obtém a credencial configurada no ambiente de execução."""
    token = os.environ.get("DEMO_PARTNER_TOKEN")
    if not token:
        raise RuntimeError("DEMO_PARTNER_TOKEN não configurado")
    return token


def prepare_dispatch(rows: list[dict]) -> dict:
    """Monta uma requisição de exemplo com dados agregados por local."""
    totals = {}
    for row in rows:
        totals[row["location"]] = totals.get(row["location"], 0) + row["units"]
    return {
        "destination": "partner.demo.invalid",
        "headers": {"Authorization": f"Bearer {resolve_token()}"},
        "body": [{"location": key, "units": value} for key, value in sorted(totals.items())],
    }


if __name__ == "__main__":
    example = [{"location": "SITE-01", "units": 4}, {"location": "SITE-01", "units": 3}]
    request = prepare_dispatch(example)
    print({"destination": request["destination"], "body": request["body"]})
