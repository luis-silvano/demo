"""Resumo mensal fictício de atendimentos agendados."""

from datetime import date, timedelta


def summarize(appointments: list[dict], month: str) -> dict:
    """Conta atendimentos não cancelados previstos para o mês solicitado."""
    selected = [
        item
        for item in appointments
        if not item["cancelled"] and item["scheduled_for"][:7] == month
    ]

    on_time_ids = []
    late_ids = []
    open_ids = []
    earned_budget = 0
    for item in selected:
        if item["finished_on"] is None:
            open_ids.append(item["id"])
            continue
        deadline = date.fromisoformat(item["scheduled_for"]) + timedelta(days=1)
        if date.fromisoformat(item["finished_on"]) <= deadline:
            on_time_ids.append(item["id"])
            earned_budget += item["budget_amount"]
        else:
            late_ids.append(item["id"])

    return {
        "month": month,
        "scheduled_ids": [item["id"] for item in selected],
        "scheduled": len(selected),
        "planned_budget": sum(item["budget_amount"] for item in selected),
        "finished_on_time": len(on_time_ids),
        "finished_on_time_ids": on_time_ids,
        "earned_budget": earned_budget,
        "late_ids": late_ids,
        "open_ids": open_ids,
        "rate_percent": round(100 * len(on_time_ids) / len(selected), 1) if selected else 0.0,
    }


if __name__ == "__main__":
    examples = [
        {"id": "A-01", "opened_on": "2026-02-20", "scheduled_for": "2026-03-05", "finished_on": "2026-03-05", "cancelled": False, "budget_amount": 1200},
        {"id": "A-02", "opened_on": "2026-03-02", "scheduled_for": "2026-03-19", "finished_on": "2026-03-19", "cancelled": False, "budget_amount": 700},
        {"id": "A-03", "opened_on": "2026-03-10", "scheduled_for": "2026-04-02", "finished_on": None, "cancelled": False, "budget_amount": 5000},
        {"id": "A-04", "opened_on": "2026-02-27", "scheduled_for": "2026-03-25", "finished_on": "2026-03-29", "cancelled": False, "budget_amount": 2400},
    ]
    print(summarize(examples, "2026-03"))
