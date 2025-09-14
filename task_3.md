# Висновки:

```sh
Розмір масиву: 100
Insertion sort: 0.00021220000053290278
Merge sort: 0.0004600999964168295
Timsort (Python sorted): 2.0199993741698563e-05

Розмір масиву: 1000
Insertion sort: 0.02467600000090897
Merge sort: 0.0017291000112891197
Timsort (Python sorted): 0.00011590000940486789

Розмір масиву: 5000
Insertion sort: 1.0252543999959016
Merge sort: 0.026949200007948093
Timsort (Python sorted): 0.001548699990962632
```


- Insertion sort показує гарну швидкість тільки на малих даних (O(n²) у гіршому випадку).

- Merge sort стабільно працює за O(n log n).

- Timsort (Python sorted) значно швидший завдяки оптимізації (гібрид merge + insertion).
