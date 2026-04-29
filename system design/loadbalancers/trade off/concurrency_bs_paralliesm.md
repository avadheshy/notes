Concurrency and parallelism are two of the most misunderstood concepts in system design.

While they might sound similar, they refer to fundamentally different approaches to handling tasks.

Simply put, one is about managing multiple tasks simultaneously, while the other is about executing multiple tasks at the same time.

# 1. What is Concurrency?
Concurrency means an application is making progress on more than one task at the same time.

In a computer, the tasks are executed using Central Processing Unit (CPU).

While a single CPU can work on only one task at a time, it achieves concurrency by rapidly switching between tasks.

This seamless switching—enabled by modern CPU designs—creates the illusion of multitasking and gives the appearance of tasks running in parallel.

However, it’s important to note this is not parallel. This is concurrent.

Concurrency is primarily achieved using threads, which are the smallest units of execution within a process. The CPU switches between threads to handle multiple tasks concurrently, ensuring the system remains responsive.

The primary objective of concurrency is to maximize CPU utilization by minimizing idle time.

For example:

When one thread or process is waiting for I/O operations, database transactions, or external program launches, the CPU can allocate resources to another thread.
This ensures the CPU remains productive, even when individual tasks are stalled.

# How Does Concurrency Works?
Concurrency in a CPU is achieved through context switching.

Here’s how it works:

**Context Saving**: When the CPU switches from one task to another, it saves the current task's state (e.g., program counter, registers) in memory.

**Context Loading**: The CPU then loads the context of the next task and continues executing it.

**Rapid Switching**: The CPU repeats this process, switching between tasks so quickly that it seems like they are running simultaneously.

The Cost of Context Switching
While context switching enables concurrency, it also introduces overhead:

Every switch requires saving and restoring task states, which consumes both time and resources.
Excessive context switching can degrade performance by increasing CPU overhead.

# 2. What is Parallelism?
Parallelism means multiple tasks are executed simultaneously.

To achieve parallelism, an application divides its tasks into smaller, independent subtasks. These subtasks are distributed across multiple CPUs, CPU cores, GPU cores, or similar processing units, allowing them to be processed in parallel.

To achieve true parallelism, your application must:

Utilize more than one thread.
Ensure each thread is assigned to a separate CPU core or processing unit.
## How does Parallelism Works?
Modern CPUs consist of multiple cores. Each core can independently execute a task. Parallelism divides a problem into smaller parts and assigns each part to a separate core for simultaneous processing.

**Task Division**: The problem is broken into smaller independent sub-tasks.

**Task Assignment**: Sub-tasks are distributed across multiple CPU cores.

**Execution**: Each core processes its assigned task simultaneously.

**Result Aggregation**: Results from all cores are combined to form the final output.
# 3. Concurrency and Parallelism Combinations
## 3.1 Concurrent, Not Parallel
An application can be concurrent without being parallel. In this case:

The application makes progress on multiple tasks at the same time seemingly (concurrently).
However, it achieves this by switching between tasks rapidly, rather than running them simultaneously.
Example: A single-core CPU alternating between tasks, giving the illusion of multitasking.

## 3.2 Parallel, Not Concurrent
An application can be parallel without being concurrent. Here:

A single task is divided into subtasks, and these subtasks are executed simultaneously on separate cores.
There is no overlap between tasks; one task (and its subtasks) completes before the next task starts.
Example: Video rendering, where a single video is divided into frames, and each frame is processed in parallel.
## 3.3 Neither Concurrent Nor Parallel
Some applications are neither concurrent nor parallel. This means:

Tasks are executed sequentially, one at a time, without any overlap or parallel execution.

Example: A single-core CPU where only one task is processed, and it completes fully before the next task begins.
## 3.4 Concurrent and Parallel
An application can be both concurrent and parallel, combining the strengths of both execution models.

In this approach:

Multiple tasks make progress at the same time, and each task is also divided into subtasks that are executed in parallel.

Example: A Multi-core CPU where some subtasks run concurrently on the same core, while others run in parallel on separate cores.
