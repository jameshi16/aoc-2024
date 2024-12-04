# AOC Day 1 Solution

Part 1:

Given an input `input.txt` run the following commands:

``` text
sed 's/   / /g' input.txt | cut -d ' ' -f 1 | sort > col1
sed 's/   / /g' input.txt | cut -d ' ' -f 2 | sort > col2
paste col1 col2 | awk '{ print sqrt(($1 - $2)*($1 - $2)); }' | awk '{ sum += $1 } END { print sum }'
```

Part 2:

See excel
