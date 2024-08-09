# test-llm-service

Разработка предполагается исключительно на `Linux`

<span style="color:red">После генерация необходимо обратить внимание на Dockerfile, 
в нем установлена `python3.9-dev`, которая актуальна только для 
`python 3.9`, если в указанном образе другой питон, то его нужно заменить!</span>


Как развернуть приложение?

1. Install `pyenv`
```bash
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

exec "$SHELL"
```


2. Установка необходимой версии python 3.9.13
```bash
pyenv install 3.9.13
```

3. Создание окружения
Для единообразия и простоты предлагается называть окружение в pyenv,
так же как и сам сервис
```bash
make venv
```

4. Активация созданного окружения make не хочет обновлять консоль, 
поэтому активацию приходится делать отдельной командой
```bash
pyenv activate 
```

5. Проверка версии питона
```bash
make check-python-version
```

6. Установка poetry (установка всех зависимостей будет происходить через poetry, чтобы было меньше проблем с зависимостями)
Так же запрещаем poetry создавать окружение внутри проекта
Иначе `poetry` будет постоянно намереваться создавать окружение внутри проекта
```bash
make install-poetry
```

7. Установка зависимостей из poetry.lock
```bash
make dep-install
```

8. Обновить версии пакетов
Если какие-то пакеты нужно оставить с определенными версиями, то
    (пример)
`poetry add  "uvicorn==0.17.5"`
а затем, массовое обновление версий библиотек
```bash 
make pkg-upd 
```

9. Генерация зависимостей (requirements.txt/requirements-dev.txt)
```bash 
make gen-req
```

10. Генерация настроек проекта
```bash
make gen-settings
```

11. Генерация настроек DVC
Если в проекте не предполагается использовать dvc, то
можно удалить `.dvc/`
Для генерации конфига, необходимо, чтобы в .bashrc были установлены 
переменные окружения
```
export ACCESS_KEY_ID=<key>
export SECRET_ACCESS_ID=<key>
```
[Ключи взять здесь](https://git.gosuslugi.local/digital-assistant/dadc/keypass.git)
```bash
make gen-dvc 
```

12. После всех шагов необходимо добавить в git index
```bash
git add poetry.lock
git add requirements/requirements.txt
git add requirements/requirements-dev.txt 
```

13. Выбрать новосозданный интерпретатор питона из окружения test_llm_service для работы с проектом

14. Создание `pre-commit` хука
Важно чтобы проект уже версионировался git'ом
```bash
echo "make reformat" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```