
arr = [[1,0,0,2], [0,1,2,0], [0,2,1,0], [2,0,0,1]]
left = 0
right = 0
auxRight = len(arr) -1
for i in range(0, len(arr)):
    left += arr[i][i]
    right += arr[i][auxRight]
    auxRight -= 1

print(abs(left - right))

#==========================================================================#
#Another solution
left = 0
right = 0
auxRight = 0
for i in range(0, len(arr)):
    left += arr[i][i]

for i in range(len(arr)-1, -1, -1):
    right += arr[auxRight][i]
    auxRight += 1

print(abs(left - right))