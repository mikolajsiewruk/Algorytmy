from random import randint
import time as tm
import matplotlib.pyplot as plt

class Solution:
    def __init__(self):
        self.bubble_arrays=[]
        self.insert_arrays=[]
        self.selection_arrays=[]
        self.bubble_time=[]
        self.insert_time=[]
        self.selection_time=[]
        self.sizes=[50,100,200,500,1000,2000]
        self.array_maker()
        self.get_times()
    def array_maker(self):
        l=[50,100,200,500,1000,2000]
        self.bubble_arrays = []
        self.insert_arrays = []
        self.selection_arrays = []
        for i in range(0,len(l)):
            a=[randint(0,5000) for _ in range(0,l[i])]
            self.bubble_arrays.append(a)
            self.insert_arrays.append(a)
            self.selection_arrays.append(a)
    def bubble_sort(self,arr):
        start=tm.perf_counter_ns()
        changes=1
        i=0
        while changes!= 0:
            changes = 0
            for j in range (0,len(arr)-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    changes+=1
        end=tm.perf_counter_ns()
        return end-start
    #print(bubble_sort(tab))
    def insertion_sort(self,arr):
        start=tm.perf_counter_ns()
        for j in range(1,len(arr)):
            key=arr[j]
            i=j-1
            while i>=0 and key< arr[i]:
                arr[i+1]=arr[i]
                i-=1
            arr[i+1]=key
        end=tm.perf_counter_ns()
        return end-start
    def selection_sort(self,arr):
        start=tm.perf_counter_ns()
        for j in range (0,len(arr)):
            top = 0
            for i in range (0,len(arr)-j):
                if arr[i]>top:
                    top=arr[i]
            arr[arr.index(top)],arr[-1-j]=arr[-1-j],arr[arr.index(top)]
        end=tm.perf_counter_ns()
        return end-start
    def get_times(self):
        for k in range(0,len(self.bubble_arrays)):
            self.bubble_time.append(self.bubble_sort(self.bubble_arrays[k]))
            self.selection_time.append(self.selection_sort(self.selection_arrays[k]))
            self.insert_time.append(self.insertion_sort(self.insert_arrays[k]))
        self.bubble_time=self.bubble_time[0:6]
        self.insert_time=self.insert_time[0:6]
        self.selection_time=self.selection_time[0:6]
    def plot_build(self):
        plt.plot(self.sizes,self.bubble_time,label="Bubble sort")
        plt.plot(self.sizes,self.insert_time,label="Insertion sort")
        plt.plot(self.sizes,self.selection_time,label="Selection sort")
        plt.xlabel('Array Size')
        plt.ylabel('Runtime (ns)')
        plt.title('Runtime Comparison of Sorting Algorithms')
        plt.legend()
        plt.grid(True)
        plt.show()


#print(selection_sort(tab))
tab=[9,2,0,2,1,60,59,100]
tab2=[9,2,0,2,1,60,59,100]
tab3=[9,2,0,2,1,60,59,100]
#for arr in ars:
    #print(selection_sort(arr))
#print(tm.perf_counter_ns())
