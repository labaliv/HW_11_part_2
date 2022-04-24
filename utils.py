import json


__list_candidates = []


def load_candidates(file):
    """ Функция загрузки из файла.

    Загружает список кандидатов из файла в формате json  и возвращает в формате списка словарей.
    """
    with open(file, 'r', encoding='utf-8') as file:
        global __list_candidates
        __list_candidates = json.load(file)
        return __list_candidates


def format_candidates(list_candidates):
    """ Функция получения списка кандидатов.

        Возвращает список кандидатов в формате: имя, позиция, навыки.
        """
    total = '<pre>'
    for candidate in list_candidates:
        total += (f'Имя кандидата - {candidate["name"]}\n'
                  f'Позиция кандидата {candidate["position"]}\n'
                  f'Навыки через запятую - {candidate["skills"]}\n\n')
    total += '<pre>'
    return total


def get_candidate_for_id(id_candidate):
    """ Функция получения кандидата из списка.

        Возвращает кандидата c заданным списком данных по id.
        """
    for candidate in __list_candidates:
        if id_candidate == candidate["id"]:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills']
            }
    return {'not_found': 'Ушел в отпуск'}


def get_candidate_for_name(candidate_name):
    """ Функция получения кандидата из списка по имени.

        Возвращает кандидата(ов) c заданным именем.
        """
    return [candidate for candidate in __list_candidates if candidate_name.lower() in candidate['name'].lower()]


def get_candidate_with_skill(skill_name):
    """ Функция получения кандидата из списка.

        Возвращает кандидата(ов) c заданным скиллом.
        """
    result = []
    for candidate in __list_candidates:
        skill = candidate["skills"].lower().split(', ')
        if skill_name in skill:
            result.append(candidate)
    return result
