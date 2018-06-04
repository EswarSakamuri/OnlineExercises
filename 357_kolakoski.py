"""
Problem:
A Kolakoski sequence (A000002) is an infinite sequence of symbols {1, 2} that is its own run-length encoding.
It alternates between "runs" of symbols. The sequence begins:
12211212212211211221211212211...
The first three symbols of the sequence are 122, which are the output of the first two iterations.
After this, on the i-th iteration read the value x[i] of the output (one-indexed). If i is odd, output x[i] copies of the number 1.
If i is even, output x[i] copies of the number 2.
There is an unproven conjecture that the density of 1s in the sequence is 1/2 (50%).
In today's challenge we'll be searching for numerical evidence of this by tallying the ratio of 1s and 2s for some initial N symbols of the sequence.
"""

def kolakoski(num):
    res=[1,2,2]
    for i in range(2, num+1):
        for j in range(res[i]):
            if i%2 == 0:
                res.append(1)
            else:
                res.append(2)
    return (res[:num].count(1), res[:num].count(2))

if __name__ == "__main__":
    result={}
    samp_input = [10, 100, 1000]
    for sam in samp_input:
        result[sam] = kolakoski(sam)
    print(result)