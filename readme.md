# Austrian Nobleman

(This project is currently incomplete and unusable.)

> _So you'll be an Austrian nobleman_  
> _Commissioning a symphony in C_  
> _Which defies all earthly descriptions_  
> _You'll be commissioning a symphony in C_  
> —CAKE, “Commissioning a Symphony in C”

Austrian Nobleman allows you to write C in a lisp, ie sexpr, syntax. On the compromises this necessarily entails, AN makes design trade-offs that are significantly different to other work in this space. Namely, it tries to be as faithful to C as possible. However, it should be easy to modify the ast_to_c function in the implementation file to create less-faithful derivatives, if desired. (Coming soon: Austrian Nobleman 2: Revenge of the Austrian Nobleman) This code is public domain and may be adapted freely.

## Example

TODO: put the longest, most involved example here.

For further examples, please see the test folder.

## Dependencies

Python: The implementation of this project is in Python (Python 3 is probably required, I didn't check because who uses Python 2 any more), because ~~why not lol~~ I didn't feel like writing a lot of string manipulation code in C. There are no plans to self-host Austrian Nobleman; even though it would be relatively trivial, the only foreseeable "benefit" would be having to maintain a two simultaneous implementations: the realistic one and the self-hosted one.

A C compiler: I feel a bit bad that I'm just piling more crap on top of the pile of crap that already is contemporary computing, but YOLO.

Unix shell (optional): Austrian Nobleman (.an) files can be invoked the shell as scripts using a shebang (eg `#!/bin/an`) that points to the `an` shell script included in this directory that runs the source script through `austrian-nobleman.py`, pipes that to the c compiler `cc`, and executes the resulting program. Note that this will produce a compiled version of your file in the local directory, named the same as the source file less the file extenion, so make sure you can write to the local directory and that this won't cause name collisions. This shebang business is optional; you can always manually run your source code through `austrian-nobleman.py`, `cc`, and `exec` (or your local equivalents) yourself.


## Related Work

There are a variety of other projects which try to do something like this, generally with slightly different approaches or syntax.

L++ https://bitbucket.org/ktg/l/src/master/ "L++ is a programming language that transcompiles to C++. It uses Lisp-like syntax." It is written in Racket. I didn't quite like the chosen syntax, nor do I like C++, nor do I understand Racket.

Dale https://github.com/tomhrr/dale "Dale is a system (no GC) programming language that uses S-expressions for syntax and supports syntactic macros. The basic language is similar to C, with [...] additional features". Again, I didn't really like the particular choice of syntax.

C-Mera, once known as cgen, https://github.com/kiselgra/c-mera "The C-Mera system is a set of very simple compilers that transform a notation based on S-Expressions (sexp) for C-like languages to the native syntax of that language, e.g. from sexp-C to C, and from sexp-CUDA to CUDA. The semantics of the sexp-based notation is identical to that of the native language, i.e. no inherent abstraction or layering is introduced." Again, I didn't quite care for their syntax.

cmacro https://github.com/eudoxia0/cmacro "Lisp macros for C [...] A macro is a function that operates on your code's abstract syntax tree rather than values. Macros in cmacro have nothing to do with the C preprocessor except they happen at compile time, and have no knowledge of run-time values. In cmacro, a macro maps patterns in the code to templates. A macro may have multiple cases, each matching multiple patterns, but each producing code through the same template. cmacro has a very lenient notion of C syntax, which means you can write macros to implement DSLs with any syntax you like. You could implement Lisp-like prefix notation, or a DSL for routing URLs, or the decorator pattern, for example."

Clasp https://github.com/clasp-developers/clasp "Clasp is a new Common Lisp implementation that seamlessly interoperates with C++ libraries and programs using LLVM for compilation to native code. This allows Clasp to take advantage of a vast array of preexisting libraries and programs, such as out of the scientific computing ecosystem. Embedding them in a Common Lisp environment allows you to make use of rapid prototyping, incremental development, and other capabilities that make it a powerful language."

## A Long And Rambling History Of A Project That Never Really Went Anywhere

_“It is a truth universally acknowledged, that a single man in possession of a computer science degree, must be in want of a lisp.”_

For motivations that are best left undescribed lest the length of this document tend to infinity, in the late Spring of 2021 I became interested in lisps again and wanted to implement my own. I had heard that C was effectively an assembly language for some modern programming languages, and that the second most promising way of slap-dashing a compiler together, LLVM IR, was actually still quite infuriating. So, since I had already decided to sacrifice the perfect for the good in this project, I decided to make a lisp that compiled to C.

I was already familiar with L++ https://bitbucket.org/ktg/l/src/master/ and figured an appropriate name for an analogous language targeting pure C would be L. Thus, the name of this project was L for about five minutes, before I realized there was already a programming language called L http://l-lang.org/

I looked into using, ie, the GCC intermediate AST or something as a touchstone; taking that AST out of the compiler as a sexpr or parsing a sexpr and then feeding the result into the compiler at the step where it would want the parsed AST data. However, even trying to figure out that theoretically-more-direct way was hilariously more complicated than just generating regular C code as my output. For a small taste of this, see http://icps.u-strasbg.fr/~pop/gcc-ast.html https://gcc.gnu.org/onlinedocs/gccint/RTL.html or https://clang.llvm.org/docs/IntroductionToTheClangAST.html or https://llvm.org/docs/LangRef.html

And the rest, as they say, is history.
