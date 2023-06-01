def check_values(form_name,values):
    form_keys = ['question','answer_1','answer_2','answer_3','answer_4',
                 'answer_1_point','answer_2_point','answer_3_point','answer_4_point']
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
            if len(v) < 9:
                return 'Fill in all fields'
            for k_item,v_item in v.items():
                if k_item not in form_keys:
                    return 'Something went wrong'
                if type(v_item) != int and len(v_item) < 1:
                    return 'Fill in all fields'
                

def check_fill_form_key_and_values(values):
    question_list = ['question_list_1','question_list_2','question_list_3','question_list_4','question_list_5',
                                         'question_list_6','question_list_7','question_list_8','question_list_9','question_list_10']
    question_list_2 = ['question_1','question_2','question_3','question_4','question_5']
    content_question = ['question','answer_1','answer_2','answer_3','answer_4']
    if len(values) < 10:
        return 'Fill in all fields'
    for key, value in values.items():
        if len(value) < 5:
            return 'Fill in all fields'
        if key not in question_list:
            return 'Something went wrong'
        for key_2,value_2 in value.items():
            if key_2 not in question_list_2:
                return 'Something went wrong'
            if len(value_2) != 2:
                return 'Something went wrong'
            if 'question' not in value_2.keys():
                return 'Something went wrong'
            for key_3 in value_2.keys():
                if key_3 not in content_question:
                    return 'Something went wrong'