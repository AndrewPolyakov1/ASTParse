# ASTParse
Code for ITMO hackathon (Nov 2023)

# Тема

Написание утилиты, позволяющей визуализировать и отображать структуру <mark>программы/класса/AST</mark> на языке _Python_ для языка _Python_ :joy:

Основное назначение для _публицации статей_ на хабре/гитхабе, чтобы не рисовать это вручную. (ну и для обучающих целей)
Также для _дебага_ программы

# Использование
Установить библиотеки

```
pip install -r reqirements.txt 
```



# Участники

|Role|Name|
|--|--|
|Графика| Амина|
|AST| Андрей|
|Графика| Толян|
|AST| Федя|

# Задачки

<form action="/action_page.php">
  <input type="checkbox" name="vehicle1" value="0">
  <label for="vehicle1"> Возможно подрубить парсер сообщений санитайзера, чтобы отлавливать в какой момент произошла утечка памяти </label><br>
  <input type="checkbox" name="vehicle2" value="1">
  <label for="vehicle2"> В виде графа (дерева), если будет время и желание жить - интерактивное представление </label><br>
  <input type="checkbox" name="vehicle3" value="2" checked>
  <label for="vehicle3"> Парс в Json</label><br><br>
</form>

# Интерфейс

`translate(code: str) -> str (code)`

`tokenize(fn: str) -> List[dict]`

`build_cfg_config(code: str) -> str` -> генерит конфиг

`build_cfg_config_file(code: str, name : str) -> None`

`create_image_from_file(path: str, name : str)` 

`create_image_from_config(config: str, name : str)` 

`wrapper_image(code: str) -> path` -> генерит картинку из кода

