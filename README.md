# ASTParse (Py2Art)
Code for ITMO hackathon (Nov 2023)

# Тема
Утилита, позволяющая получить представление функций/классов программы в виде Control Flow Graph (CFG) и псевдокода, предназначенная в первую очередь для облегчения написания статей (например, на Habr или GitHub). 

# Использование
Установить библиотеки

```
pip install -r requirements.txt 
```

# Участники
| Name              | Role                                            |
| ----------------- | ----------------------------------------------- |
| Мулюкова Амина    | тимлид, трансляция Python в псевдокод           |
| Поляков Андей     | архитектура, токенизация Python, построение CFG |
| Жарков Федор      | UI, построение CFG                              |
| Казаков Алексей   | архитектура, трансляция Python в псевдокод      |
| Васильев Анатолий | UI                                              |

# Интерфейс py2art
`save_image(path: str, config: str, format: str) -> None` - рендерит изображение формата `format` на основе dot-конфига `config` в файл `{path}.{format}`

`def build_cfg_config(code: str, pseudocode: bool = True) -> str` - строит CFG на основе исходного кода `code` в формате dot

`translate(code: str) -> str` - преобразует исходный код Python в псевдокод

`code_to_image_and_pseudocode(filepath: str, pseudocode: bool = False, format: str = 'png') -> List(Tuple(str, str, str))` - на основе файла с исходным кодом создает псевдокод и CFG

`change_keys_colors(new_node_colors : dict) -> None` - изменяет цвета элементов CFG
     
`get_keys_colors() -> dict` - возвращает словарь с цветами элементов CFG

`get_supported_formats() -> list(str)` - возвращает список поддерживаемых для экспорта форматов изображений