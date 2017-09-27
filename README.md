# subencode

Not the most efficient way to solve this problem, but gets the job done.

Goes about solving the NNM exploit's massive amount of bad characters (https://www.exploit-db.com/exploits/5342/)
Instead of using an algorithm to find the correct values to subtract to reach shellcode, it instead brute forces the values, starting with a random seed.
