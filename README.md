# ASTParse
Code for ITMO hackathon (Nov 2023)

# Тема

Написание утилиты, позволяющей визуализировать и отображать структуру <mark>программы/класса/AST</mark> на языке _Python_ для языка _Python_ :joy:

Основное назначение для _публицации статей_ на хабре/гитхабе, чтобы не рисовать это вручную. (ну и для обучающих целей)
Также для _дебага_ программы

# Использование
Установить библиотеки

```
pip install -r requirements.txt 
```

# Участники

|Role|Name|
|--|--|
|Псевдокод парсер| Амина|
|Псевдокод грамматика| Леша|
|Токенизация, сборка| Андрей|
|UI| Толян|
|Разнорабочий| Федя|

# Интерфейс

`translate(code: str) -> str (code)`

`tokenize(fn: str) -> List[dict]`

`build_cfg_config(code: str) -> str` -> генерит конфиг

`create_image_from_config(config: str, name : str)` 

`wrapper_image(code: str, name: str) -> path` -> генерит картинку из кода

`code_to_image_and_pseudocode(filepath: str) -> List[tuple[name: str, pseudocode: str, Image, config: str]]:` -> генерит все из пути к файлу кода

