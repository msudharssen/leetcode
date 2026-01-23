class Solution:
    def __init__(self):
        pass

    def mergeKLists(self, lists):
        if len(lists)<=1:
            return lists
       
        mid = (len(lists))//2
        leftArr = lists[:mid]
        rightArr = lists[mid:]
        left = self.mergeKLists(leftArr)
        right = self.mergeKLists(rightArr)
        return self.merge(left, right)
            

    def merge(self, left, right):
        output = [0]*(len(left)+len(right))
        print(output)

        writePointer = 0
        leftPointer = 0
        rightPointer = 0

        while leftPointer < len(left) and rightPointer < len(right):
            if left[leftPointer]<=right[rightPointer]:
                output[writePointer]=left[leftPointer]
                leftPointer+=1
            else:
                output[writePointer]=right[rightPointer]
                rightPointer+=1
            writePointer+=1
        
        while leftPointer < len(left):
            output[writePointer]=left[leftPointer]
            leftPointer+=1
            writePointer+=1
        while rightPointer < len(right):
                output[writePointer]=right[rightPointer]
                rightPointer+=1
                writePointer+=1
        return output
    

sample = Solution()
print(sample.mergeKLists([5,7,1,6,4,10]))  #[1,1,2,3,4,4,5,