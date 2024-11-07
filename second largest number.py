#second largest number in an array
 arr=list(map(int,input("Enter an array of numbers: ").split(",")))
 large=arr[0]
 secondlarge=arr[0]
 print("Array : ",arr)
 for i in arr:
   if i>large:
     secondlarge=large
     large=i
   elif i>secondlarge and i!=large:
        secondlarge=i
 print("Second largest number in array : ",secondlarge


