"""Indicador fictício de verificação de ciclos operacionais."""


def summarize(cycles: list[dict], month: str, minimum_score: int = 80) -> dict:
    """Conta ciclos com verificação registrada e leitura suficiente."""
    selected = [item for item in cycles if item["finished_on"][:7] == month]
    released_ids = []
    held_ids = []
    released_units = 0
    held_units = 0
    for item in selected:
        accepted = (
            item["verified"]
            and (item["sensor_score"] or minimum_score) >= minimum_score
        )
        if accepted:
            released_ids.append(item["id"])
            released_units += item["lot_units"]
        else:
            held_ids.append(item["id"])
            held_units += item["lot_units"]

    total = len(selected)
    return {
        "month": month,
        "cycles": total,
        "passing": len(released_ids),
        "released_ids": released_ids,
        "held_ids": held_ids,
        "released_units": released_units,
        "held_units": held_units,
        "rate_percent": round(100 * len(released_ids) / total, 1) if total else 0.0,
    }


if __name__ == "__main__":
    examples = [
        {"id": "C-01", "finished_on": "2026-03-01", "verified": True, "sensor_score": 92, "lot_units": 100},
        {"id": "C-02", "finished_on": "2026-03-03", "verified": True, "sensor_score": 84, "lot_units": 200},
        {"id": "C-03", "finished_on": "2026-03-04", "verified": True, "sensor_score": None, "lot_units": 2500},
        {"id": "C-04", "finished_on": "2026-03-08", "verified": True, "sensor_score": 71, "lot_units": 500},
        {"id": "C-05", "finished_on": "2026-03-11", "verified": True, "sensor_score": 81, "lot_units": 150},
    ]
    print(summarize(examples, "2026-03"))
