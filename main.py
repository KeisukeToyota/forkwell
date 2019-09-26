import os
from multiprocessing import Pool, cpu_count

def code_factory(lang, ext, code):
    if not os.path.isdir(lang):
        os.mkdir(lang)
    for i in range(100):
        with open(f"{lang}/source-{i}.{ext}", 'w+') as f:
            f.write(code)
    print(f"{lang.capitalize()} done!")

def python():
    lang = 'python'
    ext = 'py'
    code = """
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
    """
    code_factory(lang, ext, code * 100000)

def ruby():
    lang = 'ruby'
    ext = 'rb'
    code = """
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2) 
    """
    code_factory(lang, ext, code * 100000)

def rust():
    lang = 'rust'
    ext = 'rs'
    code = """
fn main() {{
{}
}}

    """.format('  println!("Hello world");\n' * 100000)
    code_factory(lang, ext, code)

def go():
    lang = 'go'
    ext = 'go'
    code = """
package main

import "fmt"

func main() {{
{}
}}
    """.format('\tfmt.Println("Hello world")\n' * 100000)
    code_factory(lang, ext, code)

def c():
    lang = 'c'
    ext = 'c'
    code = """
#include <stdio.h>

int main() {{
{}
}}
    """.format('\tprintf("Hello world");\n' * 100000)
    code_factory(lang, ext, code)

def cpp():
    lang = 'c++'
    ext = 'cpp'
    code = """
#include <iostream>

int main() {{
{}
}}
    """.format('\tstd::cout << "Hello world" << std::endl;\n' * 100000)
    code_factory(lang, ext, code)

def php():
    lang = 'php'
    ext = 'php'
    code = """
<?php

{}
    """.format('echo "Hello world";\n' * 100000)
    code_factory(lang, ext, code)

def commit():
    if not os.path.isdir('.git'):
        os.system('git init')
    os.system('git add .')
    os.system('git commit -m "commit"')

def callback(f):
    f()

if __name__ == '__main__':
    funcs = [python, ruby, rust, go, c, cpp, php]

    with(Pool(cpu_count())) as p:
        p.map(callback, funcs)

    #commit()
