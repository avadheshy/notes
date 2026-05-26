# Go (Golang) — Complete Quick Reference

---

## 1. Introduction to Go

Go is a statically typed, compiled language by Google. Designed for simplicity, performance, and built-in concurrency.

**Key traits:** No classes (structs + methods instead), no exceptions (errors as values), no inheritance (embedding instead), first-class functions, garbage collected, native concurrency via goroutines + channels.

---

## 2. Hello World

```go
package main

import "fmt"

func main() {
    message := greetMe("world")
    fmt.Println(message)
}

func greetMe(name string) string {
    return "Hello, " + name + "!"
}
```

```bash
$ go run hello.go
$ go build        # compiles to binary
```

---

## 3. Packages

```go
// Single import
import "fmt"

// Grouped import
import (
    "fmt"
    "math/rand"
)

// Alias
import r "math/rand"
r.Intn(10)
```

- Every file starts with `package <name>`
- Executables use `package main`
- **Uppercase** identifier = exported (public); **lowercase** = private
- Convention: package name = last segment of import path (`math/rand` → `rand`)

---

## 4. Fundamentals

### Identifiers
- Must start with a letter or `_`; case-sensitive
- Exported (visible outside package) if it starts with uppercase

### Keywords
```
break    case     chan      const    continue
default  defer    else      fallthrough  for
func     go       goto      if       import
interface  map    package   range    return
select   struct   switch    type     var
```

### Data Types

| Category | Types |
|----------|-------|
| Integer  | `int`, `int8`, `int16`, `int32`, `int64`, `uint`, `uint8`… |
| Float    | `float32`, `float64` |
| Complex  | `complex64`, `complex128` |
| Boolean  | `bool` |
| String   | `string` |
| Aliases  | `byte` = `uint8`, `rune` = `int32` |

### Variables

```go
var msg string                   // zero value ""
var msg = "Hello"                // type inferred
var msg string = "Hello"         // explicit type
var x, y int = 1, 2              // multiple

// Declaration block
var (
    x int
    y = 20
    z int = 30
    d, e = 40, "Hello"
)

// Short declaration (functions only)
msg := "Hello"
x, msg := 1, "Hello"
```

### Constants & iota

```go
const Pi = 3.14
const Size int64 = 1024

const (
    Pi = 3.14
    E  = 2.718
)

// iota — auto-incrementing within const block
const (
    _  = iota      // 0 skipped
    A               // 1
    B               // 2
    C = 1 << iota   // 8  (2^3)
    D               // 16 (2^4)
)

// Classic use: days of week
const (
    Sunday = iota   // 0
    Monday          // 1
    Tuesday         // 2
    // ...
)
```

### Rune

```go
var r rune = 'A'    // single quotes; stores Unicode code point
fmt.Println(r)      // 65
```

### Operators

| Type       | Operators |
|------------|-----------|
| Arithmetic | `+` `-` `*` `/` `%` |
| Bitwise    | `&` `\|` `^` `&^` `<<` `>>` |
| Comparison | `==` `!=` `<` `>` `<=` `>=` |
| Logical    | `&&` `\|\|` `!` |
| Pointer    | `&` (address of) `*` (dereference) `<-` (channel) |

### Scope

- **Package-level:** outside functions, whole package
- **Function-level:** inside a function
- **Block-level:** inside `{}`, only within that block

### Type Casting

```go
var i int = 42
var f float64 = float64(i)
var u uint = uint(f)
```

### `var` vs `:=`

| Feature | `var` | `:=` |
|---------|-------|------|
| Where | Package + function | Function only |
| Type | Explicit or inferred | Always inferred |
| Zero value | Yes | No (must assign) |
| New var required | No | At least one new var on left |

---

## 5. Control Statements

### if / else

```go
if x > 10 {
    fmt.Println("big")
} else if x == 10 {
    fmt.Println("equal")
} else {
    fmt.Println("small")
}

// Init statement before condition
if val := compute(); val > 0 {
    fmt.Println(val)
}

// Type assertion inside if
var val interface{} = "foo"
if str, ok := val.(string); ok {
    fmt.Println(str)
}
```

### Loops (only `for`)

```go
for i := 0; i < 5; i++ { }          // classic
for i < 10 { i++ }                  // while-style
for { }                              // infinite

for i, v := range slice { }         // range with index + value
for _, v := range slice { }         // range value only
for i := range slice { }            // range index only

// Labels for nested loops
outer:
    for i := 0; i < 3; i++ {
        for j := 0; j < 3; j++ {
            if j == 1 { continue outer }
            if i == 2 { break outer }
        }
    }
```

### Loop Control

| Statement | Description |
|-----------|-------------|
| `break` | Exit loop (or labeled outer loop) |
| `continue` | Next iteration (or labeled outer loop) |
| `goto label` | Jump to label |

### Switch

```go
switch day {
case "Mon":
    fmt.Println("Monday")
case "Tue", "Wed":         // comma-separated cases
    fmt.Println("Midweek")
default:
    fmt.Println("Other")
}

// Switch with init statement
switch os := runtime.GOOS; os {
case "darwin": fmt.Println("Mac")
}

// Expressionless switch (if-else chain)
switch {
case x < 0:  fmt.Println("negative")
case x == 0: fmt.Println("zero")
}

// fallthrough (explicit)
switch day {
case "sunday":
    fallthrough
case "saturday":
    rest()
}
```

### Select + Deadlock & Default

```go
select {
case msg := <-ch1:
    fmt.Println("ch1:", msg)
case msg := <-ch2:
    fmt.Println("ch2:", msg)
case <-time.After(time.Second):
    fmt.Println("timeout")
default:
    fmt.Println("no message")  // prevents blocking/deadlock
}
```

> Without `default`, `select` blocks until a channel is ready — can cause **deadlock**.

---

## 6. Functions & Methods

### Basic Function

```go
func add(a, b int) int { return a + b }
```

### Function Arguments — Pass by Value vs Reference

```go
// Pass by value — original unchanged
func double(x int) { x *= 2 }

// Pass by pointer — mutates original
func doublePtr(x *int) { *x *= 2 }

n := 5
doublePtr(&n)
fmt.Println(n) // 10
```

### Variadic Function

```go
func sum(nums ...int) int {
    total := 0
    for _, n := range nums { total += n }
    return total
}
sum(1, 2, 3)

nums := []int{10, 20, 30}
sum(nums...)   // spread slice
```

### Anonymous Function & Closures

```go
// Anonymous function (immediately invoked)
result := func(x, y int) int { return x + y }(3, 4)

// Closure — captures outer variable
func counter() func() int {
    count := 0
    return func() int {
        count++
        return count
    }
}
c := counter()
c() // 1
c() // 2
```

### `main` and `init`

- `main()` — program entry point (package main only)
- `init()` — runs before `main()`, auto-called, used for setup; multiple allowed per file/package

### Multiple Return Values

```go
func divide(a, b float64) (float64, error) {
    if b == 0 { return 0, fmt.Errorf("division by zero") }
    return a / b, nil
}
val, err := divide(10, 2)
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
value, _ := divide(10, 2)   // discard second return
```

### Defer

```go
// Runs after surrounding function returns (LIFO order)
func main() {
    defer fmt.Println("3rd")
    defer fmt.Println("2nd")
    fmt.Println("1st")
}
// Output: 1st → 2nd → 3rd

// Defer with closure (captures final value)
func main() {
    d := 0
    defer func() { fmt.Println(d) }()   // prints final d
    d = 42
}
// Output: 42
```

### Methods & Pointer Receivers

```go
type Circle struct { Radius float64 }

// Value receiver — struct is copied, cannot mutate
func (c Circle) Area() float64 { return 3.14 * c.Radius * c.Radius }

// Pointer receiver — can mutate the original struct
func (c *Circle) Scale(factor float64) { c.Radius *= factor }

c := Circle{5}
c.Scale(2)
fmt.Println(c.Area())
```

### Methods With Same Name (Different Types)

```go
func (r Rect) Area() float64   { return r.W * r.H }
func (c Circle) Area() float64 { return 3.14 * c.R * c.R }
```

---

## 7. Structures

```go
type Person struct {
    Name string
    Age  int
}
p := Person{Name: "Alice", Age: 25}
p.Age = 26
```

### Structure Equality

```go
p1 := Person{"Alice", 25}
p2 := Person{"Alice", 25}
fmt.Println(p1 == p2) // true — all fields must be comparable
```

### Nested Structure

```go
type Address struct { City string }
type Employee struct {
    Name    string
    Address Address
}
e := Employee{"Bob", Address{"Delhi"}}
fmt.Println(e.Address.City)
```

### Anonymous Structure & Fields

```go
// Anonymous struct
p := struct{ Name string }{Name: "Bob"}

// Anonymous field (embedded type)
type Animal struct { string }
a := Animal{"Dog"}
fmt.Println(a.string)
```

### Promoted Fields & Methods

Embedding a struct promotes its fields and methods to the outer struct.

```go
type Base struct { ID int }
func (b Base) Describe() { fmt.Println("ID:", b.ID) }

type Child struct { Base; Extra string }
c := Child{Base{1}, "extra"}
c.Describe()       // promoted method
fmt.Println(c.ID)  // promoted field
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

## 8. Arrays & Slices

### Arrays (fixed size)

```go
var arr [3]int               // [0 0 0]
arr := [3]int{1, 2, 3}
arr := [...]int{1, 2, 3}     // compiler counts length

arr[0] = 42
fmt.Println(len(arr))
```

**Copy:** Arrays are value types — assignment = full copy.

```go
arr2 := arr1  // independent copy
```

**Pass to function:** Also copied; use pointer to mutate original.

```go
func modify(a *[3]int) { a[0] = 99 }
modify(&arr)
```

### Slices (dynamic, reference type)

```go
s := []int{1, 2, 3}
s = append(s, 4, 5)

// From array
arr := [5]int{1, 2, 3, 4, 5}
sl := arr[1:4]      // {2,3,4} — shares underlying array
sl2 := arr[:3]      // {1,2,3}
sl3 := arr[3:]      // {4,5}

// make
s := make([]int, 5)        // len=5, cap=5
s := make([]int, 3, 10)    // len=3, cap=10

// Concatenate
c := append(a, b...)
```

**Composite Literal:**
```go
s := []string{"a", "b", "c"}
```

**Passing to function:** Slices are reference types — changes inside a function affect the original.

```go
func addOne(s []int) {
    for i := range s { s[i]++ }
}
nums := []int{1, 2, 3}
addOne(nums)
fmt.Println(nums) // [2 3 4]
```

**Copy (independent):**
```go
dst := make([]int, len(src))
copy(dst, src)
```

**Trim (re-slice):**
```go
s = s[1:]            // remove first element
s = s[:len(s)-1]     // remove last element
s = s[1:len(s)-1]    // remove both ends
```

**Split:**
```go
mid := len(s) / 2
first, second := s[:mid], s[mid:]
```

**Compare / Equality:**
```go
// Cannot use == (except with nil)
import "reflect"
reflect.DeepEqual(s1, s2)   // true if same elements

// Manual
func equal(a, b []int) bool {
    if len(a) != len(b) { return false }
    for i := range a { if a[i] != b[i] { return false } }
    return true
}
```

**Sort:**
```go
import "sort"
sort.Ints(s)
sort.Strings(s)
sort.Slice(s, func(i, j int) bool { return s[i] < s[j] })
```

---

## 9. Maps

```go
// Create
m := make(map[string]int)
m["age"] = 25

// Map literal
m := map[string]int{"alice": 30, "bob": 25}

// Read
val := m["alice"]

// Check existence
val, ok := m["charlie"]   // ok=false if key doesn't exist

// Delete
delete(m, "alice")

// Iterate
for key, value := range m { fmt.Println(key, value) }

// Map of structs
users := map[string]Person{
    "a": {Name: "Alice", Age: 30},
}
```

> Maps are reference types. Zero value is `nil` — must be initialized with `make` or literal before use.

---

## 10. Strings

```go
s := "Hello, Go"
s2 := `Multiline
string`                   // raw string literal (backticks)
```

| Operation | Code |
|-----------|------|
| Compare | `s1 == s2`, `strings.Compare(s1, s2)` |
| Concatenate | `s1 + s2`, `strings.Join([]string{s1,s2}, "")`, `fmt.Sprintf("%s%s", s1, s2)` |
| Trim | `strings.TrimSpace(s)`, `strings.Trim(s, "!")`, `strings.TrimLeft/Right` |
| Split | `strings.Split(s, ",")` → `[]string` |
| Contains | `strings.Contains(s, "Go")` → `bool` |
| Repeat | `strings.Repeat("ab", 3)` → `"ababab"` |
| Index | `strings.Index(s, "Go")` → `-1` if not found |
| Count | `strings.Count(s, "l")` |
| Has prefix/suffix | `strings.HasPrefix(s, "He")`, `strings.HasSuffix(s, "Go")` |
| To upper/lower | `strings.ToUpper(s)`, `strings.ToLower(s)` |

---

## 11. Pointers

```go
x := 42
p := &x           // p is *int, holds address of x
fmt.Println(*p)   // dereference → 42
*p = 100          // modifies x through pointer
```

**`new` keyword:**
```go
p := new(int)    // allocates zeroed int, returns *int
*p = 42
```

### Double Pointer

```go
x := 10
p := &x
pp := &p          // **int
fmt.Println(**pp) // 10
```

### Pointer to Function

```go
func greet() { fmt.Println("Hi") }
f := greet     // function value
f()
```

### Returning Pointer from Function

```go
func newInt(v int) *int { return &v }  // safe in Go — heap allocated
```

### Pointer to Array (as function argument)

```go
func double(arr *[3]int) {
    for i := range arr { arr[i] *= 2 }
}
double(&arr)
```

### Pointer to Struct

```go
p := &Person{Name: "Alice"}
p.Name = "Bob"   // auto-dereferenced (same as (*p).Name)
```

### Comparing Pointers

```go
fmt.Println(p1 == p2)  // true only if they point to same address
```

### Length & Capacity of Pointer to Array

```go
arr := [5]int{1, 2, 3, 4, 5}
p := &arr
fmt.Println(len(p), cap(p)) // 5 5
```

---

## 12. Interfaces

```go
type Shape interface {
    Area() float64
    Perimeter() float64
}

type Rectangle struct{ Length, Width float64 }

func (r Rectangle) Area() float64      { return r.Length * r.Width }
func (r Rectangle) Perimeter() float64 { return 2 * (r.Length + r.Width) }

var s Shape = Rectangle{3, 4}
fmt.Println(s.Area())
```

> Types implement interfaces **implicitly** — no `implements` keyword needed.

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
    Reader    // embeds Reader interface
    Writer    // embeds Writer interface
}
```

### Polymorphism

```go
func printArea(s Shape) { fmt.Println(s.Area()) }

printArea(Rectangle{3, 4})
printArea(Circle{5})
```

### Type Assertion

```go
var i interface{} = "hello"

s, ok := i.(string)    // safe assertion
fmt.Println(s, ok)     // "hello" true

n, ok := i.(int)       // won't panic — ok is false
```

### Type Switch

```go
func describe(i interface{}) {
    switch v := i.(type) {
    case int:
        fmt.Printf("int: %v\n", v*2)
    case string:
        fmt.Printf("string: %q, len=%d\n", v, len(v))
    default:
        fmt.Printf("unknown type: %T\n", v)
    }
}
```

---

## 13. Error Handling

Go has no exceptions — errors are return values.

```go
// error is a built-in interface
type error interface {
    Error() string
}
```

```go
func sqrt(x float64) (float64, error) {
    if x < 0 {
        return 0, errors.New("negative value")
    }
    return math.Sqrt(x), nil
}

val, err := sqrt(-1)
if err != nil {
    fmt.Println("Error:", err)
    return
}
fmt.Println(val)
```

**Custom errors:**
```go
type ValidationError struct {
    Field   string
    Message string
}
func (e *ValidationError) Error() string {
    return fmt.Sprintf("%s: %s", e.Field, e.Message)
}
```

---

## 14. Concurrency

### Goroutines

```go
go func() { fmt.Println("concurrent") }()

// Named function
go doWork("task1")
```

### Channels

```go
ch := make(chan int)         // unbuffered — blocks until both sides ready

go func() { ch <- 42 }()
val := <-ch

// Buffered — doesn't block until buffer full
ch := make(chan int, 3)
ch <- 1; ch <- 2; ch <- 3
// ch <- 4  ← would deadlock here
```

### Closing Channels

```go
close(ch)               // only the sender should close

// Check if closed
val, ok := <-ch         // ok=false means channel is closed

// Range over channel until closed
for v := range ch {
    fmt.Println(v)
}
```

### Channel Axioms (important for interviews!)

| Operation | Result |
|-----------|--------|
| Send on `nil` channel | Blocks forever (deadlock) |
| Receive from `nil` channel | Blocks forever (deadlock) |
| Send on **closed** channel | **Panics** |
| Receive from **closed** channel | Returns zero value immediately |

### Unidirectional Channels

```go
func send(ch chan<- int)    { ch <- 1 }    // send-only
func receive(ch <-chan int) { fmt.Println(<-ch) }  // receive-only
```

### Select Statement

```go
select {
case v := <-ch1:
    fmt.Println("ch1:", v)
case v := <-ch2:
    fmt.Println("ch2:", v)
case <-time.After(time.Second):
    fmt.Println("timeout")
default:
    fmt.Println("non-blocking")
}
```

### Multiple Goroutines with WaitGroup

```go
import "sync"

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
| Stack size | ~2 KB (grows dynamically) | ~1–8 MB (fixed) |
| Managed by | Go runtime | OS |
| Cost | Very cheap (millions possible) | Expensive |
| Communication | Channels | Shared memory / mutex |
| Scheduling | M:N (cooperative + preemptive) | 1:1 (preemptive) |

---

## 15. fmt — Printing & Formatting

```go
fmt.Println("Hello", name)           // adds spaces, newline
fmt.Printf("Name: %s, Age: %d\n", name, age)  // formatted

// Format verbs
// %v  — default format
// %T  — type of value
// %d  — integer
// %f  — float  (%0.2f for 2 decimal places)
// %s  — string
// %q  — quoted string
// %b  — binary
// %x  — hex
// %e  — scientific notation
// %t  — boolean
// %p  — pointer address

s := fmt.Sprintf("Hello, %s!", name)   // returns string
fmt.Fprintln(os.Stderr, "error msg")   // write to writer
```

---

## 16. Reflection

```go
import "reflect"

x := 42
fmt.Println(reflect.TypeOf(x))   // int
fmt.Println(reflect.ValueOf(x))  // 42
```

---

## 17. Snippets

### HTTP Server

```go
package main

import (
    "fmt"
    "net/http"
)

type Hello struct{}

func (h Hello) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    fmt.Fprint(w, "Hello!")
}

func main() {
    http.ListenAndServe(":4000", Hello{})
}
```

### File Embedding

```go
import "embed"

//go:embed hello.txt
var content string   // or embed.FS for multiple files

fmt.Println(content)
```

---

> **Quick tips:** `go fmt` — format code | `go vet` — catch bugs | `go test` — run tests | `go mod init` — start a module