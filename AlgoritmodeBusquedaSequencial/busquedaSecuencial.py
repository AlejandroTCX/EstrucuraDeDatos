def linear_search(arr, find)
(0..arr.length - 1).each { |i| return i if arr[i] ==
find }
-1
End