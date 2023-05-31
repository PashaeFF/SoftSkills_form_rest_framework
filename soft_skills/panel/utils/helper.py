def check_values(form_name,values):
    form_keys = ['title','answer_1','answer_2','answer_3',
                 'answer_1_point','answer_2_point','answer_3_point']
    # point_keys = ['answer_1_point','answer_2_point','answer_3_point']
    if len(form_name) < 1:
        return 'The form title cannot be empty'
    if type(values) != dict:
        return 'Something went wrong'
    if len(values) < 10:
        return 'Fill in all fields'
    for value in values.values():
        if len(value) < 5:
            return 'Fill in all fields'
        for k,v in value.items():
            for k_item,v_item in v.items():
                if k_item not in form_keys:
                    return 'Something went wrong'
                if type(v_item) != int and len(v_item) < 1:
                    return 'Fill in all fields'
                