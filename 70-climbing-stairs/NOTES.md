* 用2个variable来记录 到n-1 和 n-2分别有多少种方法
​
*  n = 1 时，ways = 1: 跨1步
*  n = 2 时，ways = 2: 跨1+1，or 跨2
*  n = 3 时，ways 取决于 n-1和 n-2， 由加和得来
*  n = 4时， ways 由 n-1 和 n-2 加和得来
​
​
* 对2 - n进行for loop：
* 每一个n均由 （n-2） + （n-1）得来
​
​