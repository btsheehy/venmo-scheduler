def yes_or_no(question):
    prompt = f'{question} (y/n): '
    ans = input(prompt).strip().lower()
    if ans not in ['y', 'n', 'yes', 'no']:
        print(f'{ans} is invalid, please try again...')
        return yes_or_no(question)
    if ans in ['y', 'yes']:
        return True
    return False


def print_env(var_name, val):
    try:
        print(var_name + "=" + val)
    except:
        print(var_name + '=NOT_AVAILABLE')
