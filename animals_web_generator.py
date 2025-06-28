from data.data_service import fetch_animal_by_name
from animals_file_management import read_html_template, write_html_content


FIELDS_TO_PRINT = {
    "characteristics_diet": lambda x: x['diet']  if isinstance(x, dict) and x.get('diet') else None,
    "locations": lambda x: x[0] if isinstance(x, list) and x else None,
    "characteristics_type": lambda x: x['type'] if isinstance(x, dict) and x.get('type') else None,
}


def prompt_animal_name():
    return input("Enter animal's name: ")


def search_animal_by_name(name):
    return fetch_animal_by_name(name)


def serialize_animal(animal):
    html = [
        '<li class="cards__item">'
        f'<div class="card__title">{animal["name"]}</div>'
        '<p class="card__text">'
    ]

    for field, handler in FIELDS_TO_PRINT.items():
        if '_' in field:
            field = field.split('_')
            base_key = field[0]
            actual_key = field[1]
        else:
            base_key = field
            actual_key = field

        value = animal.get(base_key)
        if value is not None:
            processed = handler(value)
            if processed:
                html.append(f"<strong>{actual_key.title()}:</strong> {processed} <br/>")

    html += ['</p>', '</li>\n']
    return ''.join(html)


def serialize_animal_not_found(name):
    return (
        f'<h2 style="text-align: center;">Animal {name} not found.</h2>'
        f'<h3 style="text-align: center;">Search another animal!</h2>'
    )


def serialze_animal_technical_error(error, status):
    return (
        f'<h2 style="text-align: center; font-size: 30px">Error_{status}</h2>'
        f'<h3 style="text-align: center;">{error}</h2>'
    )


def generate_html_for_animals(animals, status, name):
    if status == 200 and animals:
        return ''.join(serialize_animal(animal) for animal in animals)
    elif status == 200 and not animals:
        return serialize_animal_not_found(name)
    else:
        return serialze_animal_technical_error(animals, status)


def main():
    name = prompt_animal_name()
    animals, status, searched_name = search_animal_by_name(name)
    html_body = generate_html_for_animals(animals, status, searched_name)

    html_template = read_html_template()
    html_template = html_template.replace('__REPLACE_ANIMALS_INFO__', html_body)
    write_html_content(html_template)
    print('Html created successfully.')


if __name__ == '__main__':
    main()



