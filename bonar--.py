# -*- coding: utf-8 -*-
# Esolang compiler based on Boner++
# Bonar--

# read the input file (extension is '.bonar')

import sys

filename = sys.argv[1]

f = open(filename + '.bonar', 'r')

code = f.read()

# dictionary of words to be swapped

swap = {
            'gamming' : 'for',
            'sonic' : 'while',
            'shitpost' : 'in',
            'hmm' : 'if',
            'wtf' : 'else',
            'wtmm' : 'elif',
            'doitwork' : 'try',
            'nah' : 'except',
            'kaolo' : 'break',
            'clobbong' : 'continue',
            'gibin' : 'input',
            'gebneralk' : 'class',
            'chumbender' : 'def',
            'jeff' : 'return',
            'away' : '-',
            'yang' : '+', 
            'perc' : '%',
            'deliberately_equals' : '==',
            'bonar' : '=',
            'unfunwaa' : '<',
            'funwaa' : '>',
            'yote' : '<=',
            'yeet' : '>=',
            'xon' : 'and',
            'detecotb' : 'or',
            'itdobe' : 'is',
            'zenzi' : 'not',
            'hpock' : 'import',
            'tysob' : 'from',
            'blorgia' : 'as',
            'pungle' : 'with',
            'anime' : 'True',
            'no_anime' : 'False',
            'soulLESS' : 'None',
            'ban' : 'del',
            'howdy' : 'print',
            'zoom' : 'yield',
            'troll' : 'lambda',
            'ADL' : 'raise',
            'oil' : 'pass',
            'zoomer' : 'nonlocal', 
            'boomer' : 'global',
            'doge' : 'finally',
            'sus' : 'await',
            'amongus' : 'assert',
            'chungus' : 'async',
            'blacksheets' : 'dict',
            'thumbnail' : 'str',
            'xomc' : 'int',
            'dicde' : 'double',
            'boatin' : 'float',
            'touhou' : 'chr',
            'osu' : 'map',
            'reimu' : 'set',
            'based' : 'max',
            'cringe' : 'min',
            'BrUH' : 'range',
            'mips' : 'round',
            'vig' : 'sum',
            'pringle' : 'super',
            'dino' : 'tuple',
            'rshig' : 'zip',
            'racoon' : 'type',
            'dong' : 'len',
            'balls' : 'list',
            'jeb' : 'open',
            'pipeline' : 'join',
            'epyc' : 'file',
            'skeet' : 'split',
            'goof' : 'append',
            'cock' : 'run',
            'chumburger' : '[]',
            'eburger' : '\'\'',
            'sprite' : 'event',
            '!!' : ':',
            'tree' : '3',
            '})]' : '(',
            '[({' : ')',
            '}])' : '[',
            '([{' : ']',
            ')]}' : '{',
            '{[(' : '}'
}

new = code

for name in swap.values():
    calcname = " " + name + " " 
    if calcname in code:
        raise ValueError('What is this? '+ name)

for item in swap: new = new.replace(item, swap[item])

# now we just have regular python code

print("Bonar-- 1.0 shits fixed")
# confirm message

exec('# -*- coding: utf-8 -*-\n' + new)




            
            
  
