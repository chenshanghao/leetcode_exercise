### Follow up

What if the inputs contain unicode characters? How would you adapt your solution to such case?

### **Answer**

Use a hash table instead of a fixed size counter. Imagine allocating a large size array to fit the entire range of unicode characters, which could go up to [more than 1 million](http://stackoverflow.com/a/5928054/490463). A hash table is a more generic solution and could adapt to any range of characters.


