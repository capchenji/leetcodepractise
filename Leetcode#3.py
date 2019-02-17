nums1 = [1,3]
nums2 = [2]

imin = 0

if len(nums2) < len(nums1):
    Anums = nums2
    Bnums = nums1
else:
    Anums = nums1
    Bnums = nums2

m = len(Anums)
n = len(Bnums)
imax = m

while True:
    i = int((imin + imax) / 2) - 1
    j = int((m + n + 1) / 2) - i - 1
    print(j)
    if Bnums[j - 1] > Anums[i]:
        imin = i + 1
    elif Anums[i - 1] > Bnums[j]:
        imax = i - 1
    else:
        break

if (m + n) % 2 == 0:
    print( (max(Anums[i - 1], Bnums[j - 1]) + min(Anums[i], Bnums[j])) / 2 )
else:
    print( max(Anums[i - 1], Bnums[j - 1]))