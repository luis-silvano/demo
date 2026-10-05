"""Conferência fictícia de materiais retirados para solicitações."""

from collections import defaultdict


def summarize(requests: list[dict], withdrawals: list[dict]) -> dict:
    """Confirma se cada solicitação recebeu o item e a quantidade esperados."""
    issued_by_request = defaultdict(int)
    for withdrawal in withdrawals:
        key = withdrawal["request_id"]
        issued_by_request[key] += withdrawal["quantity"]

    ready_ids = []
    blocked_ids = []
    shortage_value = 0
    released_value = 0
    for request in requests:
        issued = issued_by_request[request["id"]]
        missing = max(request["expected_quantity"] - issued, 0)
        if missing:
            blocked_ids.append(request["id"])
            shortage_value += missing * request["unit_price"]
        else:
            ready_ids.append(request["id"])
            released_value += request["expected_quantity"] * request["unit_price"]

    total = len(requests)
    return {
        "requests": total,
        "fulfilled": len(ready_ids),
        "ready_ids": ready_ids,
        "blocked_ids": blocked_ids,
        "released_value": released_value,
        "shortage_value": shortage_value,
        "rate_percent": round(100 * len(ready_ids) / total, 1) if total else 0.0,
    }


if __name__ == "__main__":
    requests = [
        {"id": "R-01", "item_code": "X-1", "expected_quantity": 2, "unit_price": 100},
        {"id": "R-02", "item_code": "X-2", "expected_quantity": 2, "unit_price": 200},
        {"id": "R-03", "item_code": "X-3", "expected_quantity": 1, "unit_price": 800},
        {"id": "R-04", "item_code": "X-4", "expected_quantity": 1, "unit_price": 500},
        {"id": "R-05", "item_code": "X-5", "expected_quantity": 1, "unit_price": 1000},
    ]
    withdrawals = [
        {"request_id": "R-01", "item_code": "X-1", "quantity": 2},
        {"request_id": "R-02", "item_code": "X-2", "quantity": 1},
        {"request_id": "R-03", "item_code": "X-9", "quantity": 1},
        {"request_id": "R-05", "item_code": "X-5", "quantity": 1},
    ]
    print(summarize(requests, withdrawals))
