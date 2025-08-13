complex_dict = {
    "string_key": "value",
    42: [1, 2, 3, {"nested_dict": {"a": 1, "b": (2, 3)}}],
    (1, 2): {"tuple_key_dict": {frozenset({1, 2, 3}): "set_as_key"}},
    frozenset({4, 5}): [{"list_of_dicts": [{"x": 10}, {"y": 20}]}],
    "mixed_list": [1, "two", (3, 4), {"five": 5}],
    "nested_mixed": {
        "inner_dict": {
            "inner_list": [1, 2, 3, {"deep_dict": "end"}],
            "inner_tuple": (1, {"t": "tuple_in_dict"})
        }
    },
    True: None,
    None: "null_key",
}

print(complex_dict[(1,2)]["tuple_key_dict"][frozenset({1, 2, 3})])
print(complex_dict["nested_mixed"]["inner_dict"]["inner_list"][3]["deep_dict"])