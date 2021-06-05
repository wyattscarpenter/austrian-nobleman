# Austrian Nobleman

(This project is currently incomplete and unusable.)

> _So you'll be an Austrian nobleman_  
> _Commissioning a symphony in C_  
> _Which defies all earthly descriptions_  
> _You'll be commissioning a symphony in C_  
> —CAKE, “Commissioning a Symphony in C”

Austrian Nobleman allows you to write C in a lisp, ie sexpr, syntax. On the compromises this necessarily entails, AN makes design trade-offs that are significantly different than other work in this space.

One of the benefits of AN is the reduced number of forms in the language. Please see the implementation file for a complete description (and implementation) of the valid forms.

## Example

TODO: put the longest, most involved example here.

For further examples, please see the test folder.

## Related Work

There are a variety of other projects which try to do something like this, generally with slightly different approaches or syntax.

L++ https://bitbucket.org/ktg/l/src/master/ "L++ is a programming language that transcompiles to C++. It uses Lisp-like syntax." It is written in Racket. I didn't quite like the chosen syntax, nor do I like C++, nor do I understand Racket.

Dale https://github.com/tomhrr/dale "Dale is a system (no GC) programming language that uses S-expressions for syntax and supports syntactic macros. The basic language is similar to C, with [...] additional features". Again, I didn't really like the particular choice of syntax.

C-Mera, once known as cgen, https://github.com/kiselgra/c-mera "The C-Mera system is a set of very simple compilers that transform a notation based on S-Expressions (sexp) for C-like languages to the native syntax of that language, e.g. from sexp-C to C, and from sexp-CUDA to CUDA. The semantics of the sexp-based notation is identical to that of the native language, i.e. no inherent abstraction or layering is introduced." Again, I didn't quite care for their syntax.

## A Long And Rambling History Of A Project That Never Really Went Anywhere

_“It is a truth universally acknowledged, that a single man in possession of a computer science degree, must be in want of a lisp.”_

For motivations that are best left undescribed lest the length of this document tend to infinity, in the late Spring of 2021 I became interested in lisps again and wanted to implement my own. I had heard that C was effectively an assembly language for some other languages, and that the second most promising way of slap-dashing a compiler together, LLVM IR, was actually still quite infuriating. So, since I had already decided to sacrifice the perfect for the good in this project, I decided to make a lisp that compiled to C.

I was already familiar with L++ https://bitbucket.org/ktg/l/src/master/ and figured an appropriate name for an analogous language targeting pure C would be L. Thus, the name of this project was L for about five minutes, before I realized there was already a programming language called L http://l-lang.org/

And the rest, as they say, is history
