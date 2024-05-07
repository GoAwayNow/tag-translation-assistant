```
         ,  . .,  °                    ,.,   '               ,  . .,  °                    ,.,   '                   ,. -,    
   ;'´    ,   ., _';\'                ;´   '· .,        ;'´    ,   ., _';\'                ;´   '· .,            ,.·'´,    ,'\   
   \:´¨¯:;'   `;::'\:'\             .´  .-,    ';\      \:´¨¯:;'   `;::'\:'\             .´  .-,    ';\      ,·'´ .·´'´-·'´::::\' 
     \::::;   ,'::_'\;'            /   /:\:';   ;:'\'      \::::;   ,'::_'\;'            /   /:\:';   ;:'\'   ;    ';:::\::\::;:'  
         ,'  ,'::;'  ‘            ,'  ,'::::'\';  ;::';          ,'  ,'::;'  ‘            ,'  ,'::::'\';  ;::';   \·.    `·;:'-·'´     
         ;  ;:::;  °        ,.-·'  '·~^*'´¨,  ';::;          ;  ;:::;  °        ,.-·'  '·~^*'´¨,  ';::;    \:`·.   '`·,  '     
         ;  ;::;'  ‘         ':,  ,·:²*´¨¯'`;  ;::';          ;  ;::;'  ‘         ':,  ,·:²*´¨¯'`;  ;::';      `·:'`·,   \'      
         ;  ;::;'‚           ,'  / \::::::::';  ;::';          ;  ;::;'‚           ,'  / \::::::::';  ;::';       ,.'-:;'  ,·\     
         ',.'\::;'‚          ,' ,'::::\·²*'´¨¯':,'\:;           ',.'\::;'‚          ,' ,'::::\·²*'´¨¯':,'\:;   ,·'´     ,.·´:::'\    
          \::\:;'‚          \`¨\:::/          \::\'            \::\:;'‚          \`¨\:::/          \::\'    \`*'´\::::::::;·'‘   
           \;:'      ‘       '\::\;'            '\;'  '           \;:'      ‘       '\::\;'            '\;'  '   \::::\:;:·´        
             °                `¨'                                °                `¨'                 Tag Translation Assistant
```

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/J3J12YAQZ)

## Requirements
* Python 3.9+
* A basic understanding of Poetry

## Installation
1. Clone this repository
2. Navigate to the resulting folder in your favorite terminal
3. Poetry install: `poetry install` or `python -m poetry install` or `py -3.9 -m poetry install` or equivalent

## Usage
Basic requirements for running this module are either an input file with one tag per line or a space-delimeted list of tags passed via the terminal (tags with spaces can be passed using quotes).

This is the basic structure of a run command, including the full 'poetry run' portion:

`python -m poetry run python -m tag_translation_assistant -i tagfile.txt -o resultfile.csv`

Output will be a .csv file with the original tag in the first collumn and various translations in subsequent collumns.

### DeepL
Upon first run, config.toml will be generated with a single entry:
```
[deepl]
apikey = ""
```
In order to use DeepL, you must visit the DeepL website, register an account and generate an API key, and then copy the api key into the configuration file. Next time you run, DeepL will be used.

It's important to note two things about DeepL, however. First, an account can only be used for either online translations or API translations, meaning if you already have an account and decide to create an API key on it, you will no longer be able to access the online translator. Second, DeepL is designed to work with sentences and paragraphs, not single words or short tags, so the results will often seem lower-quality in comparison to other translations. For these reasons, I don't consider it important to go through the work of setting up DeepL as an end user.

## Help Output
```
Automatically machine-translate multiple tags

positional arguments:
  tags                  A space-delemited list of tags

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        A text file containing tags to be translated
  -o OUTFILE, --outfile OUTFILE
                        Path to a CSV file where results are saved
  -a, --artist          Perform an artist alias lookup instead of a normal tag lookup. Only uses Danbooru as a source.
  ```