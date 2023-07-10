class Solution:
    def get_max_value_and_index(self,arr):
        max = arr[0]
        max_ind = 0
        for ind,value in enumerate(arr):
            if value>max:
                max = value
                max_ind = ind
        return max,max_ind
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        if n<=k:
            return [max(arr)]
        else:
            begin = 0
            end = k
            max_element,max_ind = self.get_max_value_and_index(arr[begin:end])
            max_list = [max_element]
            begin+=1
            for end in range(k,n):
                if begin <= max_ind:
                    if arr[end] >= max_element:
                        max_element = arr[end]
                        max_ind = end
                        max_list.append(max_element)
                        begin+=1
                        continue
                    else:
                        max_list.append(max_element)
                        begin+=1
                        continue  
                else:
                    max_element,max_ind = self.get_max_value_and_index(arr[begin:end+1])
                    max_ind = max_ind + begin
                    max_list.append(max_element)
                    begin+=1
                    continue
            return max_list

print(Solution().max_of_subarrays([1227,1555,1102,1286,1468,1698,1979,1411,1489,1758,1490,1775,1410,1132,1089,1296,1950,1112,1122,1529,1672,1836,1277,1553,1976,1670,1085,1652,1751,1397,1751,1001,1435,1693,1072,1916,1716,1328,1511,1125,1838,1296,1939,1544,1056,1826,1902,1758,1588,1021,1586,1108,1777,1628,1979,1947,1549,1280,1245,1128,1062,1426,1719,1677,1091,1047,1785,1231,1406,1684,1954,1769,1709,1956,1421,1945,1465,1016,1860,1497,1335,1190,1677,1049,1005,1886,1388,1675,1143,1377,1130,1487,1555,1482,1253,1000,1754,1289,1488,1215,1008,1310,1940,1799,1997,1707,1454,1304,1237,1485,1499,1792,1613,1612,1682,1983,1351,1129,1137,1033,1600,1864,1683,1857,1968,1710,1968,1708,1641,1732,1437,1684,1499,1701,1869,1583,1256,1692,1640,1087,1012,1810,1820,1835,1663,1615,1897,1677,1774,1134,1553,1533,1878,1286,1624,1734],156,50))
                
#code here