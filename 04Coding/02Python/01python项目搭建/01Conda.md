---
title: conda
date: 2023-06-08 23:01
article: false
star: false
check: 0
---

以下是一些常用的 Conda 操作：

1. 创建一个新的环境：

   ```
   conda create --name myenv
   ```

   这将创建一个名为 `myenv` 的新环境。

2. 激活一个环境：

   ```
   conda activate myenv
   ```

   这将激活名为 `myenv` 的环境。在激活环境后，你可以在其中安装软件包并运行 Python 程序。

3. 安装一个软件包：

   ```
   conda install numpy
   ```

   这将在当前环境中安装名为 `numpy` 的软件包。你可以将软件包名称替换为任何你想要安装的软件包。

4. 查看已安装的软件包：

   ```
   conda list
   ```

   这将列出当前环境中已安装的所有软件包。

5. 导出当前环境的软件包列表：

   ```
   conda env export > environment.yml
   ```

   这将导出当前环境的软件包列表到名为 `environment.yml` 的文件中。

6. 创建一个新的环境并从环境文件中导入软件包列表：

   ```
   conda env create --file environment.yml
   ```

   这将创建一个新的环境，并从名为 `environment.yml` 的文件中导入软件包列表。

   7. 更新一个软件包：

   ```
   conda update numpy
   ```

   这将在当前环境中更新名为 `numpy` 的软件包。

7. 搜索可用的软件包：

   ```
   conda search numpy
   ```

   这将搜索名为 `numpy` 的软件包，并列出所有可用的版本。

8. 移除一个软件包：

   ```
   conda remove numpy
   ```

   这将从当前环境中移除名为 `numpy` 的软件包。

9. 禁用环境：

   ```
   conda deactivate
   ```

   这将禁用当前环境并返回到默认环境。

10. 列出所有可用的环境：

	```
    conda env list
    ```

	这将列出所有可用的环境，并标记当前激活的环境。

11. 删除一个环境：

	```
    conda env remove --name myenv
    ```

	这将删除名为 `myenv` 的环境。

12. 创建一个新的 Python 环境：

	```
    conda create --name myenv python=3.8
    ```

	这将创建一个名为 `myenv` 的新环境，并指定 Python 版本为 3.8。

13. 将一个环境中的软件包复制到另一个环境中：

	```
    conda create --name newenv --clone oldenv
    ```

	这将创建一个名为 `newenv` 的新环境，并将名为 `oldenv` 的环境中的所有软件包复制到其中。

14. 列出当前环境中的软件包依赖关系：

	```
    conda list --explicit
    ```

	这将列出当前环境中的所有软件包，并显示它们之间的依赖关系。

15. 列出当前环境中的软件包文件：

	```
    conda list --files
    ```

	这将列出当前环境中的所有软件包，并显示它们安装的文件路径。

16. 列出当前环境中的软件包更新：

	```
    conda list --outdated
    ```

	这将列出当前环境中的所有已安装软件包，并显示它们是否有更新可用。

17. 更新所有已安装的软件包：

	```
    conda update --all
    ```

	这将更新当前环境中的所有已安装软件包。
