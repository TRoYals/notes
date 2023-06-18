---
title: Poetry
date: 2023-06-09 09:51
article: false
---

[官方文档](https://python-poetry.org/docs)

[Python 環境管理，讓 poetry 幫你建立虛擬環境 - Max行銷誌](https://www.maxlist.xyz/2022/05/08/python-poetry/)

# Poetry基本操作
## Poetry 安裝

Poetry 安裝需要在 Python 版本 2.7 or 3.5+ 以上

### 1. Poetry 在 Mac 或 Linux 安裝的朋友：

- 可以用 [Homebrew](https://brew.sh/index_zh-tw "homebrew") 安裝

|   |   |
|---|---|
|1|$ brew install poetry|

- 或用 curl 下載，兩者擇一使用

|   |   |
|---|---|
|1|$ curl -sSL <https://install.python-poetry.org> \| python3 -|

### 2. Poetry 在 Windows 安裝的朋友：

|   |   |
|---|---|
|1|$ (Invoke-WebRequest -Uri <https://install.python-poetry.org> -UseBasicParsing).Content \| py -|

### 3. 查看 Poetry 安裝版本

安裝好 Poetry 後，輸入以下指令，如果看到類似 `Poetry 1.1.4` 代表安裝成功囉！

|   |   |
|---|---|
|1<br><br>2|$ poetry --version<br><br>>> Poetry 1.3.1|

### 4. 如何更新 Poetry 版本

|   |   |
|---|---|
|1|$ poetry self update|

### 5. 如何移除 Poetry 套件

|   |   |
|---|---|
|1|$ python get-poetry.py --uninstall|

## Poetry 基本操作

### 1. 初始設定

建立一個新的專案資料夾：

|   |   |
|---|---|
|1|$ poetry new poetry-demo|

已經有專案資料夾：

|   |   |
|---|---|
|1<br><br>2|$ cd existing-project<br><br>$ poetry init|

建立完之後，資料夾結構如下，而其中`pyproject.toml` 最為重要，

|   |   |
|---|---|
|1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>6<br><br>7<br><br>8|/poetry-tutorial-project<br><br>├── README.md<br><br>├── poetry_tutorial_project<br><br>│   └── __init__.py<br><br>├── pyproject.toml<br><br>└── tests<br><br>    ├── __init__.py<br><br>    └── test_poetry_tutorial_project.py|

### 2. 安裝套件

如果要使用 Poetry 安裝套件，只需要輸入`poetry add {name}`，而刪除的話則是 `poetry remove {name}`，像是我們今天想安裝 black 套件的話：

|   |   |
|---|---|
|1|$ poetry add black|

如果在指令後面加上 `poetry add {name} --dev` 則會在開發環境上安裝指定的套件

3. 查看安裝過的套件

|   |   |
|---|---|
|1|poetry show|

如果後面加上 `--no-dev` 的話，則只會顯示正式環境的安裝套件，加上 `--tree` 的話，則會用樹狀來呈現目前已經安裝的套件

|   |   |
|---|---|
|1<br><br>2<br><br>3<br><br>4|# options<br><br>    •   --no-dev: Do not list the dev dependencies.<br><br>    •   --tree: List the dependencies as a tree.<br><br>    •   --latest (-l): Show the latest version.|

### 4. Poetry 匯出成 requirements.txt

|   |   |
|---|---|
|1|$ poetry export -f requirements.txt --without-hashes > requirements.txt|

以下是一些參數可以選擇使用，像是 `--dev` 就會涵蓋匯出開發環境的套件，`--without-hashes` 就可以去除 poetry 匯出有 hash 的 requirements.txt

|   |   |
|---|---|
|1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>6<br><br>7|•   --format (-f): The format to export to (default: requirements.txt). Currently, only requirements.txt is supported.<br><br>    •   --output (-o): The name of the output file. If omitted, print to standard output.<br><br>    •   --dev: Include development dependencies.<br><br>    •   --extras (-E): Extra sets of dependencies to include.<br><br>    •   --without-hashes: Exclude hashes from the exported file.<br><br>    •   --with-credentials: Include credentials for extra indices.|

### 5. 安裝 poetry 現有的套件

如果專案中已經有 pyproject.toml 的話，直接 `poetry install` 就可以囉, poetry install 会安装所有的生产和开发依赖项目, 不会安装可选项目. 如果想要安装可选项目, 需要使用poetry install --extras \<package_name>

### 6. 開啟 poetry 環境

輸入 `poetry shell` 開啟虛擬環境，要關閉的話輸入 `exit` 即可離開

