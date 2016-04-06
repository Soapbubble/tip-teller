[tip]
# Binding a Reference to an Rvalue
Rvalues and lvalues are a fundamental concept of C++ programming. In essence, an rvalue is an expression that cannot appear on the left-hand side of an assignment expression. By contrast, an lvalue refers to an object (in its wider sense), or a chunk of memory, to which you can write a value. References can be bound to both rvalues and lvalues. However, due to the language's restrictions regarding rvalues, you have to be aware of the restrictions on binding references to rvalues, too.

Binding a reference to an rvalue is allowed as long as the reference is bound to a const type. The rationale behind this rule is straightforward: you can't change an rvalue, and only a reference to const ensures that the program doesn't modify an rvalue through its reference. In the following example, the function f() takes a reference to const int:

```C
void f(const int & i);
int main()
{
  f(2); /* OK */
}
```

The program passes the rvalue 2 as an argument to f(). At runtime, C++ creates a temporary object of type int with the value 2 and binds it to the reference i. The temporary and its reference exist from the moment f() is invoked until it returns; they are destroyed immediately afterwards. Note that had we declared the reference i without the const qualifier, the function f() could have modified its argument, thereby causing undefined behavior. For this reason, you may only bind references to const objects.

The same rule applies to user-defined objects. You may bind a reference to a temporary object only if it's const:

```C
struct A{};
void f(const A& a);
int main()
{
  f(A()); /* OK, binding a temporary A to a const reference*/
}
```

