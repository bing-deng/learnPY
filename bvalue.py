

def solution(A):

    r, diff_array = isBvalued(A)
    length = 0
    if r:
        length = len(A)
    else:
        length = notBvaluedLength(A, diff_array)
    return length



def notBvaluedLength2(A, diff_array):

    # print(diff_array,A)
    orgian_A = A.copy()

    dict_count = {}
    for i in diff_array:
        # i in a ,counts
        c = A.count(i)
        dict_count[i] = c
    list_diff_values =  list(dict_count.values())
    list_diff_values.sort()
    
    temp_list = list_diff_values[::-1]
    return temp_list[0] + temp_list[1]


def notBvaluedLength(A, diff_array):

    orgian_A = A.copy()

    dict_count = {}
    for i in diff_array:
        # i in a ,counts
        c = A.count(i)
        dict_count[i] = c

    list_diff_values =  list(dict_count.values())
    list_diff_values.sort()

    for index,i in enumerate(list_diff_values):
        # print(index)
        if index >= len(list_diff_values) - 2:
            break
        for k,v in dict_count.items():
            if v == i and k in orgian_A:
                # print(k,index)
                while k in orgian_A:
                    orgian_A.remove(k)
                break
        r,_ = isBvalued(orgian_A)
        if(r):
            break
    return len(orgian_A)


def isBvalued(A):
    b = []
    for i in A:
        if i in A and i not in b:
            b.append(i)
    if len(b) <= 2:
        return True, b
    return False, b


A = [4,2,2,4,2]
B = [1,2,3,2]
C = [0,5,4,4,5,12]
D = [4, 4]

for i in [A, B, C ,D]:
    r = solution(i)
    print(r)