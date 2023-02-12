def overload_detection(load_capacity_max, current_weight):
    overload = round((current_weight / load_capacity_max * 100), 1) - 100
    if overload > 0:
        return overload
    return 0
