# Go (Golang) — Quick Reference

---

## 1. Introduction to Go

Go is a statically typed, compiled language developed by Google. It's designed for simplicity, performance, and built-in concurrency support.

**Key features:** Fast compilation, garbage collection, strong typing, goroutines for concurrency, and a rich standard library.

---

## 2. Hello World

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

- Every Go file belongs to a `package`
- `main` package → entry point
- `import` brings in standard/external packages

---

## 3. Fundamentals of Go

### Identifiers
Names given to variables, functions, types, etc.
- Must start with a letter or `_`
- Case-sensitive (`age` ≠ `Age`)
- Exported (public) if it starts with an uppercase letter

### Keywords
Reserved words — cannot be used as identifiers.

```
break    case     chan      const    continue
default  defer    else      fallthrough  for
func     go       goto      if       import
interface  map    package   range    return
select   struct   switch    type     var
```

### Data Types

| Category  | Types |
|-----------|-------|
| Integer   | `int`, `int8`, `int16`, `int32`, `int64`, `uint`, `uint8`… |
| Float     | `float32`, `float64` |
| Complex   | `complex64`, `complex128` |
| Boolean   | `bool` |
| String    | `string` |
| Other     | `byte` (alias `uint8`), `rune` (alias `int32`) |

### Variables

```go
// Using var
var name string = "Go"
var age int     // zero value: 0

// Short declaration (inside functions only)
city := "Delhi"
```

### Constants

```go
const Pi = 3.14
const (
    A = 1
    B = 2
)
```

### Rune

A `rune` represents a Unicode code point (`int32`).

```go
var r rune = 'A'   // single quotes
fmt.Println(r)     // 65
```

### Operators

| Type        | Operators |
|-------------|-----------|
| Arithmetic  | `+` `-` `*` `/` `%` |
| Relational  | `==` `!=` `<` `>` `<=` `>=` |
| Logical     | `&&` `\|\|` `!` |
| Bitwise     | `&` `\|` `^` `<<` `>>` |
| Assignment  | `=` `+=` `-=` `*=` `/=` |

### Scope of Variables

- **Package-level:** declared outside functions, accessible throughout the package
- **Function-level:** declared inside a function
- **Block-level:** declared inside `{}`, visible only within that block

### Type Casting

```go
var i int = 42
var f float64 = float64(i)
var u uint = uint(f)
```

### `var` vs `:=`

| Feature | `var` | `:=` |
|---------|-------|------|
| Scope | Package + function | Function only |
| Type | Explicit or inferred | Inferred |
| Zero value | Yes | No (must assign) |

---

## 4. Control Statements

### Decision Making

```go
// if-else
if x > 10 {
    fmt.Println("big")
} else if x == 10 {
    fmt.Println("equal")
} else {
    fmt.Println("small")
}

// if with init statement
if val := compute(); val > 0 {
    fmt.Println(val)
}
```

### Loops

Go has only one loop keyword: `for`

```go
// Classic
for i := 0; i < 5; i++ { }

// While-style
for i < 10 { i++ }

// Infinite
for { }

// Range
for index, value := range slice { }
```

### Loop Control Statements

| Statement  | Description |
|------------|-------------|
| `break`    | Exit the loop |
| `continue` | Skip to next iteration |
| `goto`     | Jump to a label |

### Switch Statement

```go
switch day {
case "Mon":
    fmt.Println("Monday")
case "Tue", "Wed":
    fmt.Println("Midweek")
default:
    fmt.Println("Other")
}

// Expressionless switch (acts like if-else)
switch {
case x < 0:
    fmt.Println("negative")
}
```

### Select + Deadlock & Default

`select` works like `switch` but for channels.

```go
select {
case msg := <-ch1:
    fmt.Println(msg)
case msg := <-ch2:
    fmt.Println(msg)
default:
    fmt.Println("no message") // prevents deadlock
}
```

> Without a `default` case, `select` blocks until a channel is ready — this can cause a **deadlock**.

---

## 5. Functions & Methods

### Basic Function

```go
func add(a int, b int) int {
    return a + b
}
```

### Variadic Function

```go
func sum(nums ...int) int {
    total := 0
    for _, n := range nums { total += n }
    return total
}
```

### Anonymous Function

```go
result := func(x, y int) int {
    return x + y
}(3, 4)
```

### `main` and `init`

- `main()` — program entry point
- `init()` — runs before `main()`, used for setup; multiple `init()` allowed per package

### Multiple Return Values

```go
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}
```

### Named Return Values

```go
func minMax(a, b int) (min, max int) {
    if a < b { min, max = a, b } else { min, max = b, a }
    return // naked return
}
```

### Blank Identifier

```go
value, _ := divide(10, 2) // discard error
```

### Defer

Deferred calls execute after the surrounding function returns (LIFO order).

```go
func main() {
    defer fmt.Println("world")
    fmt.Println("hello")
}
// Output: hello → world
```

### Methods

```go
type Circle struct { Radius float64 }

func (c Circle) Area() float64 {
    return 3.14 * c.Radius * c.Radius
}
```

### Methods With Same Name (Different Receivers)

Two different types can have methods with the same name.

```go
func (r Rect) Area() float64   { return r.W * r.H }
func (c Circle) Area() float64 { return 3.14 * c.R * c.R }
```

---

## 6. Structures

### Define & Use

```go
type Person struct {
    Name string
    Age  int
}
p := Person{Name: "Alice", Age: 25}
```

### Structure Equality

Two structs are equal if all their fields are equal (and fields are comparable).

```go
p1 := Person{"Alice", 25}
p2 := Person{"Alice", 25}
fmt.Println(p1 == p2) // true
```

### Nested Structure

```go
type Address struct { City string }
type Employee struct {
    Name    string
    Address Address
}
```

### Anonymous Structure & Fields

```go
// Anonymous struct
p := struct{ Name string }{Name: "Bob"}

// Anonymous field (embedded)
type Animal struct { string }
a := Animal{"Dog"}
```

### Promoted Fields & Methods

When a struct embeds another struct, its fields and methods are **promoted** — accessible directly.

```go
type Base struct { ID int }
func (b Base) Show() { fmt.Println(b.ID) }

type Child struct { Base }
c := Child{Base{1}}
c.Show()    // promoted method
fmt.Println(c.ID) // promoted field
```

### Function as a Field

```go
type Transformer struct {
    Transform func(int) int
}
t := Transformer{Transform: func(x int) int { return x * 2 }}
fmt.Println(t.Transform(5)) // 10
```

---

## 7. Arrays & Slices

### Arrays

Fixed-size, same type.

```go
var arr [3]int = [3]int{1, 2, 3}
arr2 := [...]int{4, 5, 6} // compiler counts
```

**Copying:** Arrays are value types — assignment copies the whole array.

```go
arr2 := arr1 // full copy
```

**Passing to function:** Also a copy; use pointer to mutate original.

```go
func modify(a *[3]int) { a[0] = 99 }
```

### Slices

Dynamic, reference to an underlying array.

```go
s := []int{1, 2, 3}
s = append(s, 4)

// from array
arr := [5]int{1,2,3,4,5}
sl := arr[1:4] // {2,3,4}
```

**Composite Literal:**
```go
s := []string{"a", "b", "c"}
```

**Copy:**
```go
dst := make([]int, len(src))
copy(dst, src)
```

**Compare:** Slices cannot be compared with `==` (except to `nil`); use `reflect.DeepEqual` or loop.

**Sort:**
```go
import "sort"
sort.Ints(s)
sort.Strings(s)
```

**Trim / Split:** (string-based slices → see Strings section)

---

## 8. Strings

```go
s := "Hello, Go"
```

| Operation | Example |
|-----------|---------|
| Compare | `s1 == s2`, `strings.Compare(s1, s2)` |
| Concatenate | `s1 + s2`, `strings.Join([]string{s1,s2}, "")`, `fmt.Sprintf` |
| Trim | `strings.TrimSpace(s)`, `strings.Trim(s, "!")` |
| Split | `strings.Split(s, ",")` |
| Contains | `strings.Contains(s, "Go")` |
| Repeat | `strings.Repeat("ab", 3)` → `"ababab"` |
| Index | `strings.Index(s, "Go")` |
| Count | `strings.Count(s, "l")` |

---

## 9. Pointers

A pointer stores the memory address of a value.

```go
x := 42
p := &x         // p holds address of x
fmt.Println(*p) // dereference → 42
*p = 100        // change x via pointer
```

### Double Pointer

```go
var p *int
var pp **int = &p
```

### Pointer to Function

```go
func greet() { fmt.Println("Hi") }
f := greet
f() // calls greet
```

### Returning Pointer from Function

```go
func newInt(v int) *int { return &v }
```

### Pointer to Array

```go
func double(arr *[3]int) {
    for i := range arr { arr[i] *= 2 }
}
```

### Pointer to Struct

```go
p := &Person{Name: "Alice"}
p.Name = "Bob" // auto-dereferenced
```

### Comparing Pointers

```go
fmt.Println(p1 == p2) // true only if same address
```

### Length & Capacity of Pointer (to array)

```go
arr := [5]int{1,2,3,4,5}
p := &arr
fmt.Println(len(p)) // 5
fmt.Println(cap(p)) // 5
```

---

## 10. Interfaces

Defines a set of method signatures. Implemented implicitly.

```go
type Shape interface {
    Area() float64
}

type Circle struct { Radius float64 }
func (c Circle) Area() float64 { return 3.14 * c.Radius * c.Radius }

var s Shape = Circle{5}
fmt.Println(s.Area())
```

### Multiple Interfaces

```go
type Stringer interface { String() string }
type Sizer   interface { Size() int }

type Doc struct{}
func (d Doc) String() string { return "doc" }
func (d Doc) Size() int      { return 10 }
```

### Embedding Interfaces

```go
type ReadWriter interface {
    Reader
    Writer
}
```

### Polymorphism

```go
func printArea(s Shape) {
    fmt.Println(s.Area())
}
printArea(Circle{3})
printArea(Rect{4, 5})
```

---

## 11. Concurrency

### Goroutines

A goroutine is a lightweight thread managed by the Go runtime.

```go
go func() {
    fmt.Println("runs concurrently")
}()
```

### Channels

Used to communicate between goroutines.

```go
ch := make(chan int)

go func() { ch <- 42 }()
val := <-ch
fmt.Println(val)
```

**Buffered channel:**
```go
ch := make(chan int, 2)
ch <- 1
ch <- 2
```

### Unidirectional Channel

```go
func send(ch chan<- int)    { ch <- 1 }   // send-only
func receive(ch <-chan int) { <-ch }       // receive-only
```

### Select Statement

```go
select {
case v := <-ch1:
    fmt.Println("ch1:", v)
case v := <-ch2:
    fmt.Println("ch2:", v)
}
```

### Multiple Goroutines

```go
var wg sync.WaitGroup
for i := 0; i < 5; i++ {
    wg.Add(1)
    go func(n int) {
        defer wg.Done()
        fmt.Println(n)
    }(i)
}
wg.Wait()
```

### Goroutine vs Thread

| Feature | Goroutine | OS Thread |
|---------|-----------|-----------|
| Stack size | ~2 KB (grows) | ~1–8 MB (fixed) |
| Managed by | Go runtime | OS |
| Cost | Very cheap | Expensive |
| Communication | Channels | Shared memory / mutex |
| Switching | Cooperative (M:N) | Preemptive (1:1) |

---

> **Tip:** Use `go vet` and `go fmt` regularly to catch errors and keep code clean.