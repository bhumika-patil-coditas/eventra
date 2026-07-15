from typing import Any

from sqlalchemy import Column, Select

FILTER_REGISTRY: dict[str, Any] = {
    "ge":         lambda stm, col, v: stm.filter(col >= v),
    "gt":         lambda stm, col, v: stm.filter(col > v),
    "le":         lambda stm, col, v: stm.filter(col <= v),
    "lt":         lambda stm, col, v: stm.filter(col < v),
    "eq":         lambda stm, col, v: stm.filter(col == v),
    "ne":         lambda stm, col, v: stm.filter(col != v),
    "in":         lambda stm, col, v: stm.filter(col.in_(v)),
    "notin":      lambda stm, col, v: stm.filter(col.not_in(v)),
    "between":    lambda stm, col, v: stm.filter(col.between(*v)),
    "like":       lambda stm, col, v: stm.filter(col.like(f"%{v}%")),
    "notlike":    lambda stm, col, v: stm.filter(col.notlike(f"%{v}%")),
    "ilike":      lambda stm, col, v: stm.filter(col.ilike(f"%{v}%")),
    "notilike":   lambda stm, col, v: stm.filter(col.notilike(f"%{v}%")),
    "startswith": lambda stm, col, v: stm.filter(col.startswith(v)),
    "endswith":   lambda stm, col, v: stm.filter(col.endswith(v)),
    "contains":   lambda stm, col, v: stm.filter(col.contains(v)),
}

SORTED_OPS = sorted(FILTER_REGISTRY, key=len, reverse=True)


def apply_filters(model: type, statement: Select, **kwargs: Any) -> Select:
    for key, value in kwargs.items():

        field_name = key
        matched_op = "eq"
        for op in SORTED_OPS:
            if key.endswith(f"_{op}"):
                field_name = key[: -(len(op) + 1)]
                matched_op = op
                break
        column: Column | None = getattr(model, field_name, None)
        if column is None:
            raise ValueError(f"Model '{model.__name__}' has no field '{field_name}'")
        statement = FILTER_REGISTRY[matched_op](statement, column, value)
    return statement
