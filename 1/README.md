Impelement the symbolic_tooctal function so that it converts a permission's symbolic notation into its octal notation.

The string consists of 3 blocks of 3 characters each. The returned number will have three digits, one for each block. Each digit is the sum of all permissions present in the block.

| CHARACTER | VALUE |
| --------- | ----- |
| r         | 4     |
| w         | 2     |
| x         | 1     |
| -         | 0     |

For example rwxr-x-w- is decoded as

| BLOCK | VALUE     |
| ----- | --------- |
| rwx   | 4+2+1 = 7 |
| r-x   | 4+0+1 = 5 |
| -w-   | 0+2+0 = 2 |

So the returned number would be 752.
