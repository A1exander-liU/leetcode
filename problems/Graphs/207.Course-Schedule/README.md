# Problem

There are a total of `numCourses` courses you have to take, labeled from `0 to numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
Return `true` if you can finish all courses. Otherwise, return `false`.

### Solution

We can use topological sort to determine if we can finish. The `prerequisites` represent the edges between the courses. If we have `[0, 1]`,
then the connection would look like this: `1 -> 0`. We basically have a directed graph as the ordering `[0, 1]` are important as it only
goes on way so `[1,0]` would be: `0 -> 1`.

If we can't finish, that means 2 courses requires each other to take. If course `1` needs course `3` and course `3` needs course `1`, it would be impossible to finish. Essentially if there is a cycle we can't finish.

```bash
0 -* 1 -* 2 -* 3
     *_________|

```

Since topological sorting only works for directed acyclic (no cycles) graphs, if we don't use up all the courses we then know we can't finish.

To determine in degrees, use `prerequisites`, since `[a, b]`, `b` points to `a`, we would increment the in degree of `a` by `1`. Store these in dictionary.

Use dictionary represent graph (`{ vertex: [neighbors] }`). `b` points to `a` so do: `graph[b].append(a)`

Make to iterate over `numCourses` to set each course `0 to numCourses - 1` with initial in degree of `0` and neighbors of `[]` as the `prerequisites` only store the edges.

Then apply the topological sorting:

- use queue to store initial candidates (all vertices with in degree 0)
- keep going until no more candidates
  - remove next candidate from candidates
  - decrement in degree of its neighbors by `1`
  - add the neighbor to queue if the in degree becomes `0`
  - after going through all neighbors delete candidate from graph
- at end if graph is empty, we can finish since we used up all vertices
