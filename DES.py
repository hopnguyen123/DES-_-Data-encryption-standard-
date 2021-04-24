#--------------------- S_BOX , P_BOX --------------------------
import numpy as np

def decimalToBinary(n):
    x = bin(n)[2:]
    k = str(x)
    n = len(k)
    while n<4:
        k = "0"+k
        n+=1
    return k

l_S1_box = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
           0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
           4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
           15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]

l_S2_box =[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
           3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
           0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
           13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]

l_S3_box=[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
          13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
          13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
          1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

l_S4_box = [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
            13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
            10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
            3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]

l_S5_box = [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
            14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
            4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
            11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]

l_S6_box =[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
           10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
           9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
           4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

l_S7_box =[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
           13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
           1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
           6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]

l_S8_box = [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
            1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
            7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
            2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]

arr_S1_box = np.array(l_S1_box).reshape(4,16)
arr_S2_box = np.array(l_S2_box).reshape(4,16)
arr_S3_box = np.array(l_S3_box).reshape(4,16)
arr_S4_box = np.array(l_S4_box).reshape(4,16)
arr_S5_box = np.array(l_S5_box).reshape(4,16)
arr_S6_box = np.array(l_S6_box).reshape(4,16)
arr_S7_box = np.array(l_S7_box).reshape(4,16)
arr_S8_box = np.array(l_S8_box).reshape(4,16)

Index_P_box = [15,6,19,20,28,11,27,16,
               0,14,22,25,4,17,30,9,
               1,7,23,13,31,26,2,8,
               18,12,29,5,21,10,3,24]


def S_box(list_48bit):
    index_sub_input=range(0,48,6)
    chuoicon = []
    chuoioutput=""
    for index in index_sub_input:
        l_sub_input = list_48bit[index:index+6]
        chuoicon.append(l_sub_input)
    dem =1
    for i in chuoicon:
        # print(i)
        row = [i[0], i[5]]
        column = [i[1], i[2], i[3], i[4]]
        # print(row)
        # print(column)
        row_dec=row[0]*2+row[1] #Chuyển list -> dec (hệ 10)
        column_dec=column[0]*(2**3) + column[1]*(2**2) +column[2]*2 +column[3]
        # print("row_str: ",row_dec)
        # print("column_str: ",column_dec)
        if dem==1:
            # print(arr_S1_box[row_dec, column_dec])
            x = arr_S1_box[row_dec, column_dec]
            x_=decimalToBinary(x)
            chuoioutput+=x_
        elif dem==2:
            # print(arr_S2_box[row_dec, column_dec])
            x = arr_S2_box[row_dec, column_dec]
            x_ = decimalToBinary(x)
            chuoioutput += x_
        elif dem==3:
            # print(arr_S3_box[row_dec, column_dec])
            x = arr_S3_box[row_dec, column_dec]
            x_ = decimalToBinary(x)
            chuoioutput += x_
        elif dem==4:
            # print(arr_S4_box[row_dec, column_dec])
            x = arr_S4_box[row_dec, column_dec]
            x_ = decimalToBinary(x)
            chuoioutput += x_
        elif dem==5:
            # print(arr_S5_box[row_dec, column_dec])
            x = arr_S5_box[row_dec, column_dec]
            x_ = decimalToBinary(x)
            chuoioutput += x_
        elif dem==6:
            # print(arr_S6_box[row_dec, column_dec])
            x = arr_S6_box[row_dec, column_dec]
            x_ = decimalToBinary(x)
            chuoioutput += x_
        elif dem==7:
            # print(arr_S7_box[row_dec, column_dec])
            x = arr_S7_box[row_dec, column_dec]
            x_ = decimalToBinary(x)
            chuoioutput += x_
        elif dem==8:
            # print(arr_S8_box[row_dec, column_dec])
            x = arr_S8_box[row_dec, column_dec]
            x_ = decimalToBinary(x)
            chuoioutput += x_
        dem+=1

    # print(chuoioutput)
    return chuoioutput






#------------------------------------------------------
#1. -------------------------------------------
#Hàm ShiftLeft 1 bit
def ShiftLeft_1(LIST):
    len_ = len(LIST)
    l_=LIST[0]
    for i in range(len_-1):
        LIST[i]=LIST[i+1]
    LIST[len_-1]=l_
#Hàm ShiftLeft 2 bit
def ShiftLeft_2(LIST):
    len_ = len(LIST)
    l0=LIST[0]
    l1=LIST[1]
    for i in range(len_-2):
        LIST[i]=LIST[i+2]
    LIST[len_-1]=l1
    LIST[len_-2]=l0
#Số bit ShiftLeft từng Round
LIST_SHIFTLEFT=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

#2.-----------------------------------------------------
#Chỉ số hoán vị lần 2 của KEY
index_Permuted2=[13,16,10,23,0,4,2,27,
                      14,5,20,9,22,18,11,3,
                      25,7,15,6,26,19,12,1,
                      40,51,30,36,46,54,29,39,
                      50,44,32,47,43,48,38,55,
                      33,52,45,41,49,35,28,31]


#SUBKEY HOÀN THÀNH
LIST_SUBKEY=[]


#Nhập Key đầu vào 64bit, hệ HEX(16)
print("Nhap KEY: ",end=' ')
key = input()
key_binary=""

#Chuyển Key HEX -> BINARY
for i in key:
	if i == 'A' or i =='a':
		key_binary+="1010"
	elif i == 'B' or i =='b':
		key_binary+="1011"
	elif i == 'C' or i =='c':
		key_binary+="1100"
	elif i == 'D' or i =='d':
		key_binary+="1101"
	elif i == 'E' or i =='e':
		key_binary+="1110"
	elif i == 'F' or i =='f':
		key_binary+="1111"
	else:
		key_binary += bin(ord(i))[4:]

#Chuyển từ String -> List
Key_binary= list(key_binary)

#Hoán Vị Key (Lần 1)
key_Permuted1=[]
Index_permuted1=[56,48,40,32,24,16,8,
				    0,57,49,41,33,25,17,
				    9,1,58,50,42,34,26,
				    18,10,2,59,51,43,35,
				    62,54,46,38,30,22,14,
				    6,61,53,45,37,29,21,
				    13,5,60,52,44,36,28,
				    20,12,4,27,19,11,3]
for i in Index_permuted1:
	key_Permuted1.append(Key_binary[i])


#ROUND 1/16
key_left=key_Permuted1[:28]
key_right=key_Permuted1[28:]

ROUND=1
ShiftLeft_1(key_left)
ShiftLeft_1(key_right)

list_p2=[]
for i in key_left:
	list_p2.append(i)
for i in key_right:
	list_p2.append(i)

key_permuted2=[]
for i in index_Permuted2:
    key_permuted2.append(list_p2[i])

LIST_SUBKEY.append(key_permuted2)


#	ROUND 2/16 -> 16/16
ROUND = ROUND +1

while ROUND <= 16:
	if ROUND == 2 or ROUND == 9 or ROUND == 16:
		ShiftLeft_1(key_left)
		ShiftLeft_1(key_right)
	else:
		ShiftLeft_2(key_left)
		ShiftLeft_2(key_right)

	list_p2 = []
	for i in key_left:
		list_p2.append(i)
	for i in key_right:
		list_p2.append(i)

	key_permuted2 = []
	for i in index_Permuted2:
		key_permuted2.append(list_p2[i])

	LIST_SUBKEY.append(key_permuted2)

	ROUND = ROUND + 1


#	XUÂT
SUBKEY=[]
for i_ in LIST_SUBKEY:
	i_ = ''.join(i_)
	sub_int = []
	for i in i_:
		i = int(i)
		sub_int.append(i)
	SUBKEY.append(sub_int)

# Phần này là SUBKEY 16 ROUND


# ------------------------------------------------------------------




index_Initial_permutation=[57,49,41,33,25,17,9,1,
              				59,51,43,35,27,19,11,3,
              				61,53,45,37,29,21,13,5,
              				63,55,47,39,31,23,15,7,
              				56,48,40,32,24,16,8,0,
              				58,50,42,34,26,18,10,2,
              				60,52,44,36,28,20,12,4,
              				62,54,46,38,30,22,14,6]

index_final_permutation=[39,7,47,15,55,23,63,31,
						 38,6,46,14,54,22,62,30,
						 37,5,45,13,53,21,61,29,
						 36,4,44,12,52,20,60,28,
						 35,3,43,11,51,19,59,27,
						 34,2,42,10,50,18,58,26,
						 33,1,41,9,49,17,57,25,
						 32,0,40,8,48,16,56,24]

index_Expansion=[31,0,1,2,3,4,
				3,4,5,6,7,8,
				7,8,9,10,11,12,
				11,12,13,14,15,16,
				15,16,17,18,19,20,
				19,20,21,22,23,24,
				23,24,25,26,27,28,
				27,28,29,30,31,0]

#def S_box(list_48bit):



#PlainText (ASCII) -> Binary
print("Nhap Plaintext: ",end =' ')
plaintext = input()
Plaintext_hex=""
Plaintext_bin=""
for i in plaintext:
	Plaintext_hex+=hex(ord(i))[2:]
print(Plaintext_hex)

for i in Plaintext_hex:
	if i == 'A' or i =='a':
		Plaintext_bin+="1010"
	elif i == 'B' or i =='b':
		Plaintext_bin+="1011"
	elif i == 'C' or i =='c':
		Plaintext_bin+="1100"
	elif i == 'D' or i =='d':
		Plaintext_bin+="1101"
	elif i == 'E' or i =='e':
		Plaintext_bin+="1110"
	elif i == 'F' or i =='f':
		Plaintext_bin+="1111"
	else:
		Plaintext_bin += bin(ord(i))[4:]

print(Plaintext_bin)
plaintext_bin = list(Plaintext_bin)
# print(plaintext_bin)


#Intial_Permuation
Intial_Permutation=[]
for i in index_Initial_permutation:
    Intial_Permutation.append(plaintext_bin[i])



#------------------------------------------------------

#ROUND 1/16

#Left Right
l_0 = Intial_Permutation[:32]
# print("l_0: ",l_0)
r_0 = Intial_Permutation[32:]
l_1 = r_0
l1_int=[]
for i in l_1:	#Có l_1
	i_ = int(i)
	l1_int.append(i_)
#Expand R0 32bit->48bit
r0_expansion=[]
for i in index_Expansion:
	r0_expansion.append(r_0[i])
# print(r0_expansion)
a = ''.join(r0_expansion)
# print(a)

r0_int=[]	#từ 48bit r0_str -> r0_int : để xor ở bước tiếp theo
for i in a:
	i = int(i)
	r0_int.append(i)	#Có r0_int

l0_int=[]	#từ 48bit r0_str -> r0_int : để xor ở bước tiếp theo
a = ''.join(l_0)
for i in a:
	i = int(i)
	l0_int.append(i)	#Có l0_int

#S_box ------------------------------------------------------
#xor k1 and r0_expansion
# k1 =['0', '0', '0', '0', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '1', '1', '0', '1', '0', '0', '1', '0', '1']
# k1 = ''.join(k1)
# print(k1)
# k1_int=[]
# for i in k1:
# 	i = int(i)
# 	k1_int.append(i)
# for i in k1_int:
	# print(i)
	# print(type(i))
k1_int=[]
for i in SUBKEY[0]:
	k1_int.append(i)

input_S_box=[]
for i in range(len(r0_int)):
	x = r0_int[i]^k1_int[i]
	input_S_box.append(x)
# print(input_S_box)


S_box_str =S_box(input_S_box)
Output_S_box=list(S_box_str)
# print(x_list)

#Permutation
output_P_box =[]
for index in Index_P_box:
    output_P_box.append(Output_S_box[index])

# print(output_P_box)

#Xor sau P_box
input_xor=[]
for i in output_P_box:
    i_ = int(i)
    input_xor.append(i_)

# print("input_xor: ",input_xor)

# l_0_str = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '0']
# l_0_int =[]
# for i in l_0_str:
#     i_ = int(i)
#     l_0_int.append(i_)
# print("l_0_int: ",l_0_int)

r_1 =[]
for i in range(len(l0_int)):
    x = l0_int[i]^input_xor[i]
    r_1.append(x)
# print("output: ",r_1)	#Có r_1

print("===============")
print("l_1: ",l1_int)
print("r_1: ",r_1)


# ROUND 2/16 -> 16/16 -------------------------------------------------
l_in=[]
for i in l1_int:
	l_in.append(i)
r_in =[]
for i in r_1:
	r_in.append(i)

ROUND_ = 2

while ROUND_ <=16:
	l_out = []
	r_out = []
	for i in r_in:
		l_out.append(i)		#Có l_out

					#Mở rộng r_in
	r_in_expansion = []
	for i in index_Expansion:
		r_in_expansion.append(r_in[i])

	k_int = []
	for i in SUBKEY[ROUND_-1]:
		k_int.append(i)

	input_S_box = []
	for i in range(len(k_int)):
		x = r_in_expansion[i] ^ k_int[i]
		input_S_box.append(x)
	# print(input_S_box)

	S_box_str = S_box(input_S_box)
	Output_S_box = list(S_box_str)
	# print(x_list)

	# Permutation
	output_P_box = []
	for index in Index_P_box:
		output_P_box.append(Output_S_box[index])

	# print(output_P_box)

	# Xor sau P_box
	input_xor = []
	for i in output_P_box:
		i_ = int(i)
		input_xor.append(i_)

	# print("input_xor: ",input_xor)

	# l_0_str = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '0']
	# l_0_int =[]
	# for i in l_0_str:
	#     i_ = int(i)
	#     l_0_int.append(i_)
	# print("l_0_int: ",l_0_int)

	# print("l_in: ",l_in)
	# print(len(l_in))
	# print("input_xor: ",input_xor)
	# print(len(input_xor))
	for i in range(len(l_in)):
		x = l_in[i] ^ input_xor[i]
		r_out.append(x)				#Có r_out

	# print("l_out: ",l_out)
	# print("l_in: ",l_in)
	l_in = []
	for i in l_out:
		l_in.append(i)
	r_in = []
	for i in r_out:
		r_in.append(i)

	ROUND_ +=1

# ----------------------------------

input_final_Permuation=[]
for i in r_out:
	input_final_Permuation.append(i)
for i in l_out:
	input_final_Permuation.append(i)

CIPHERTEXT=[]
for i in index_final_permutation:
	CIPHERTEXT.append(input_final_Permuation[i])

k=[]
for i in CIPHERTEXT:
	x = str(i)
	k.append(x)
k = ''.join(k)
print("================================")
print("CIPHER TEXT: ",k)




