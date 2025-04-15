# Textový analyzátor

*Note: English follows*

Základní textový analyzátor s jednoduchým grafickým výstupem

## Popis

Program testuje přihlášení pomocí uživatelskéo jména a hesla, které jsou uvedené v modulu login_data.py. Po přihlášení umožňuje analyzovat text zadaný v samostatném modulu source_texts.py a zjistit celkový počet slov, počet slov psaných velkými písmeny, počet slov s velkým počátečním písmenem, s malým počátečním písmenem, počet číselných řetězců a jejich součet.
Výsledek zobrazí pomocí jednoduchého grafu.
Zároveň ve všech případech ověřuje zadané vstupy.

## Použité knihovny a verze Pythonu

Tento program vyžaduje **Python 3.9** a novější.

Nejsou vyžadování žádné externí knihovny.

## Používání programu

Program spustíte přímo z příkazového řádku příkazem `python main.py`.
Všechny ostatní vstupy se zadávají v příkazovém řádku a potvrzují se klávesou Enter.
Uživatel se nejprve přihlásí pomocí údajů v modulu login_data.py a následně zadá číslo textu podle modulu source_texts.py.
Výsledky se zobrazí přímo v příkazovém řádku.

## Příklad fungování

Přihlášení uživatele bob a analýza textu 1:

Spuštění:

`python main.py`

Ověření uživatele:

```Please enter your username: bob
Please enter your password: 123```

Výběr textu k analýze:

```Please enter 1, 2 or 3 to select a text: 1```

Ukázka výstupu:

```There are 54 words in the text.
There are 12 titlecase words in the text.
There are 1 uppercase words in the text.
There are 38 lowercase words in the text.
There are 3 numeric strings in the text.
The sum of all the numbers is 8510.
------------------------------------------
LEN|     OCCURENCES     |NR.
------------------------------------------
  1|*                   |1  
  2|***************     |9  
  3|**********          |6  
  4|******************  |11 
  5|********************|12 
  6|*****               |3  
  7|******              |4  
  8|********            |5
  9|*                   |1
 10|*                   |1
 11|*                   |1
```

## Autor
Štěpán Pala


# Text Analyser

Basic text analyser with simple graphical output

## Description

The program tests the login using the username and password specified in the login_data.py module. After logging in, it allows to analyze the text entered in a separate module source_texts.py and find the total number of words, the number of titlecase words, the number of uppercase words, the number of lowercase words, the number of numeric strings and their sum.
The result is displayed using a simple chart.
It also verifies the input in all cases.

## Dependencies

This program requires **Python 3.9** or newer.

No external libraries required.

## Usage

Execute the script directly from your terminal/command line using `python main.py`.
All other inputs are typed in the command line and confirmed with the Enter key.
The user first logs in using the data in the login_data.py module and then enters a text number using the source_texts.py module.
The results are displayed directly in the command line.

## Example

User login for bob and analysis of Text 1:

Initiation:

`python main.py`

User authentication:

```Please enter your username: bob
Please enter your password: 123```

Selecting text for analysis:

```Please enter 1, 2 or 3 to select a text: 1```

Output example:

```There are 54 words in the text.
There are 12 titlecase words in the text.
There are 1 uppercase words in the text.
There are 38 lowercase words in the text.
There are 3 numeric strings in the text.
The sum of all the numbers is 8510.
------------------------------------------
LEN|     OCCURENCES     |NR.
------------------------------------------
  1|*                   |1  
  2|***************     |9  
  3|**********          |6  
  4|******************  |11 
  5|********************|12 
  6|*****               |3  
  7|******              |4  
  8|********            |5
  9|*                   |1
 10|*                   |1
 11|*                   |1
```

## Author
Štěpán Pala
