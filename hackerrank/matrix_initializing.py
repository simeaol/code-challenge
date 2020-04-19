from pprint import pprint
arr = [[0]*3]*3 #create innner list
arr[0][0] = 1
pprint(arr)

brr = [ ([0] *3 ) for i in range(3)]
brr[0][0] = brr[1][1] = brr[2][2] = 1
pprint(brr)