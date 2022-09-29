# This Python code is to get all the possible triplets from a stream of input data which unique integers
# The maximum distance between each element of the triplets should be less than or equal to given "k"
# For example:
#   input stream: 0, 6, 11, 16, 4, 9            K = 7 (Max distance)
#   triplets :  [4, 6, 11]
#               [9, 4, 6]
#               [9, 4, 11]
#               [9, 6, 11]
#               [9, 11, 16]

class Triplets:
    def __init__(self, k: int):
        self.k = k      # k is the maximum distance for each element of triplets
        self.IncomingStream = []     # IncomingStream is the list of incoming data stream (integer)
        self.ans = []   # ans is list of all triplets

    # Function to get input of data from user and return list of triplets, if any present
    def incoming(self):
        p = input("Enter next integer : ")
        if p.isalpha():
            print("Exist!")
        else:
            p = int(p)
            self.solve(p)
            print("Triplets with maximum distance of ", self.k, " are :", end=" ")
            if len(self.ans):
                for li in self.ans:
                    print(li)
            else:
                print("None")
            self.IncomingStream.append(p)
            self.IncomingStream.sort()
            self.incoming()

    # Function to evaluate incoming integer, if it has a maximum distance of k from other number of the stream
    def solve(self, p: int):
        n = len(self.IncomingStream)    # Checking for minimum 3 integers in input stream
        while n < 2:
            return
        low = p - self.k    # Getting lower limit for the input number which is at max distance k
        high = p + self.k   # Getting higher limit for the input number which is at max distance k
        index_low = self.find_low_index(low, self.IncomingStream)
        index_high = self.find_high_index(high, self.IncomingStream)
        if index_high == -1 or index_low == -1:
            dist = 0
        else:
            dist = index_high - index_low + 1
        if dist > 1:
            temp_stream = self.IncomingStream[index_low: index_high + 1]
            m = len(temp_stream)
            for i in range(m - 1):
                for j in range(i + 1, m):
                    if i != j and abs(temp_stream[i] - temp_stream[j]) <= self.k:
                        curr_ans = [p, temp_stream[i], temp_stream[j]]
                        self.ans.append(curr_ans)

    @staticmethod
    def find_low_index(a: int, arr: list[int]) -> int:
        l: int = len(arr) - 1
        s = 0
        res = 0
        if a > arr[l]:
            return -1
        if a < arr[0]:
            return 0
        while s <= l:
            mid = (s + l) // 2
            if arr[mid] == a:
                return mid
            elif arr[mid] > a:
                res = mid
                l: int = mid - 1
            else:
                s = mid + 1
        return res

    @staticmethod
    def find_high_index(a: int, arr: list[int]) -> int:
        l: int = len(arr) - 1
        s = 0
        res = l
        if a > arr[l]:
            return l
        if a < arr[0]:
            return -1
        while s <= l:
            mid = (s + l) // 2
            if arr[mid] == a:
                return mid
            elif arr[mid] > a:
                l: int = mid - 1
            else:
                s = mid + 1
                res = mid
        return res


if __name__ == "__main__":
    print("Program to get set of triplets, which has maximum distance of k, from an input stream of integers")
    max_distance = input("Enter the maximum distance for triplets: ")
    if max_distance.isdigit():
        print("To exit press any key, other than the number!\n")
        try:
            triplet = Triplets(int(max_distance))
            triplet.incoming()
        except:
            print("Something went wrong!")
    else:
        print("Error: Distance must be in integer")
