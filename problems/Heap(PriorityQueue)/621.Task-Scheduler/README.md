# Problem

You are given an array of CPU `tasks`, each represented by letters A to Z, and a cooling time, `n`. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least `n` intervals due to cooling time.

Return the minimum number of intervals required to complete all tasks.


### Solution
So everytime we complete a task we have to wait `n` cycles before we can use it again. If we have a task `A` and it starts at `0` and `n=2`, we can complete task `A` again when we are at `3`: `A _ _ A`, we have 2 cycles between to complete another task or idle if we can't do anything else.

When choosing a task to complete we should always choose the task that has the higest count. Consider the tasks: `[A,A,A,B,C,D] n=1`, if we choose the least frequent we would get `B C D A idle A idle A` we would have to idle cycles. But if we choose most frequent we get: `A B A C A D`, we end up getting no idle cycles, getting the best time possible. By choosing the most frequent, we can keep the most number of different tasks at once which allows us to alternate between them as opposed to having only 1 task left you are forced to idle a number of cycles equivalent to `n`.

Using example 1, we choose most frequent task as `A`, sine our `n=2` we have to cycles before we can use `A` again. So we should also choose other available tasks during this time.
`A _ _ `

We only have one other available task: `B` so we can complete this task:
`A B _`
Now we are out of tasks as we use `A` and `B` so we have to wait before we can use again. Since that we have to wait again when picking tasks to complete we should `n + 1` per iteration to follow the cooling cycle rule. This is because if our `n=2` that means after choosing one task we have 2 more slots to choose 2 other tasks (if there are 2 other tasks). Also when we chose `A` as first one at `0` we can only use it again at `3` which is `n + 1` away from `0`, so we should use this "interval" before we start picking the same tasks again.
```
n = 2
n + 1 = 3

A B idle
1 2 3
```

Now to implement, we first need count the frequencies of our tasks to initialize our heap using tuples as values: `(task_count, task)`. We'll use a max heap as we want to find the most frequent. 

We will initialize `cycles` to keep track of total cycles
Our main loop will continue until we run out of tasks, each iteration we:
- initialize `count` to store number of cycles used in this iteration
- `task_counts` will be an array to store the tasks we pop
- then we loop `n + 1` times or until our heap is empty meaning no tasks to complete this iteration
  - pop from heap to get most frequent task and add to `tasks_count` while decreasing frequency by 1 as we completed one of its tasks
  - increment `count`
- outside this loop we would add back all the tasks that still have frequency greater than `0`
- update `cycles` by `n + 1` if heap is no empty or by `count` if it was empty
  - if heap was empty that means all the tasks were completed during this iteration so we can just return `count` of number of tasks completed
  - otherwise we would return size of whole "interval" `n + 1`