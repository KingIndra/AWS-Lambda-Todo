
def get_update_params(body):

    update_expression = []
    attribute_values = dict()
    attribute_names = dict()

    for key, val in body.items():
        update_expression.append(f" #{key.lower()} = :{key.lower()}")
        attribute_values[f":{key.lower()}"] = val
        attribute_names[f"#{key.lower()}"] = key

    return "set " + ", ".join(update_expression), attribute_values, attribute_names