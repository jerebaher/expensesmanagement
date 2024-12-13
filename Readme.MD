# Expenses Manager

This project is a personal expense manager devveloped by @maunicols and @jerebaher with python and Django

## Virtual enviroment:"venv"- setup

This section is using the official [Documentation]("https://docs.python.org/es/3/tutorial/venv.html")
as reference

1. Once we have Python and **venv** installed we'll specify the python package with the _-m_ flag to use an already installed module

```python
python -m venv <directory_name>
```

2. After creation we activate the enviroment inside our terminal.

On linux

```linux
<directory-name>/bin/activate.<shell-extension>
```

On Windows

```windows
<directory-name>\Scripts\activate.<user_shell>
```

3. To install packages inside the venv we use the commands

`python -m pip install <package-name> `

for specific versioning:

`python -m pip install <package-name>==<version>`

to upgrade our packages:

` python -m pip install --upgrade <package-name>`

4. Creating a requirements.txt

The requirements.txt file is the convention for python packages such as this one.
We can list our packages inside the venv by executing the command `python -m pip list`

```
(directory-name) $ python -m pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

to transfer the list as an requirements file with autoformatting we use

`python -m pip freeze >requirements.txt`

to obtain the following file:

```
(directory-name) $ cat requirements.txt

novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```
5. To install our venv after activation we use the command 

`pip install -r requirements.txt`

6. Keep updating the file
when addong new packages. 
If done manually specify version 
