from PIL import Image, ImageOps
import random
from pydoc import plain


image = Image.open('köpke.png')
gray = ImageOps.grayscale(image)  # resmi siyah beyaz olarak alıyoruz
pix_gray = gray.load()
image.show()
width = gray.size[0]  # resmin enini alıyoruz
height = gray.size[1]

values = []

for y in range(0, height):
    for x in range(0, width):
        values.append(pix_gray[x, y])
# print(len(values))
plaintext = ""
bitesarray = []

for i in values:
    byte = bin(i)[2:]
    length = len(byte)
    if length < 8:
        bitesarray.append([byte + ("0" * (8 - length)), 8 - length])        #her byteın uzunluğunu 0 ekleyerek 83 eşitledik
    else:
        bitesarray.append([byte, 8 - length])

for i in range(0, len(bitesarray)):
    plaintext += bitesarray[i][0]
print(len(plaintext))

i=0
kalan = len(plaintext)%128
plaintext += "0"*(128-kalan)            #128 in katı olması için sonuna 0 ekledik
print((plaintext))





stage_one = plaintext[::-1]            #tersten yazdırıyoruz
# print(stage_one)
blocks = []
i=128
a=0

while(a<len(stage_one)):
    blocks.append(stage_one[0+a:i])     #işlemler için 128lik bloklara böldük
    i += 128
    a+=128
# print(blocks)
# print(len(blocks))


queue = 0
sira = 32
part1 = []
part2 = []
part3 = []
part4 = []

while(queue<len(blocks)):
    part1.append(blocks[queue][0:32])
    part2.append(blocks[queue][32:64])  # 128 biti 4e bölerek 32 lik bloklar elde ettik
    part3.append(blocks[queue][64:96])
    part4.append(blocks[queue][96:128])
    queue+=1

# print(len(part1))
i=0
block32 = []
while(i<171):
    secim = [part1[i], part2[i], part3[i], part4[i]]  # Listeye atıyoruz
    anahtar = random.sample(secim, 4)  # anahtarımızı seçtirmek için random modülü kullanıyoruz
    block32.append(anahtar)
    i+=1

secims = [part1, part2, part3, part4]
# print(len((block32)))


# print(len(secim))
s=0
b=0
b2=0
b3=0
b4=0
keys = []
while(s<171):

    for i in block32[s]:

        if(i==secims[0][b]):
            keys.append(1)
            b += 1
        elif (i == secims[1][b2]):              #random sıralanan bloklarımızın sırasını öğrendik
            keys.append(2)
            b2 += 1
        elif (i == secims[2][b3]):
            keys.append(3)
            b3 += 1
        elif (i == secims[3][b4]):
            keys.append(4)
            b4 += 1
    s += 1

print(len(keys))



stage_two = ""
i=0
while(i<len(block32)):
    for j in block32[i]:
        stage_two += j              # adım ikiyi tek satırda yazdırıyoruz
    i+=1

# print(stage_two)



liste = [1,0]
i=0
xors = []
j=0
while(j<171):
    i=0
    while(i<64):
        xors.append(random.choice(liste))       #xor işlemi yapmak için random şekilde xor oluşutrduk
        i+=1
    j+=1

xor_str = ""
for i in xors:
    xor_str += str(i)
# print(len(xor_str))


xor_str_reverse = xor_str[::-1]
xor = (xor_str_reverse+xor_str)             #xoru birleştirdik
# print(len(xor))

b=0
stage_three = ""
for a in stage_two:
    if(a==xor[b]):
        stage_three += "0"                  #xor işlemi yaptık
    else:
        stage_three += "1"
    b+=1
# print(stage_two)
# print(stage_three)
step1 = []
step2 = []
step3 = []
step4 = []
step5 = []
step6 = []
step7 = []
step8 = []

queue = 0
while(queue<len(blocks)):
    step1.append(blocks[queue][0:16])
    step2.append(blocks[queue][16:32])  #128 i 16lık bloklara ayırdık
    step3.append(blocks[queue][32:48])
    step4.append(blocks[queue][48:64])
    step5.append(blocks[queue][64:80])
    step6.append(blocks[queue][80:96])
    step7.append(blocks[queue][96:112])
    step8.append(blocks[queue][112:128])
    queue+=1

# print(len(step1))

i=0
block16 = []
while(i<171):
    secim2 = [step1[i], step2[i], step3[i], step4[i],step5[i], step6[i], step7[i], step8[i]]  # Listeye atıyoruz
    anahtar2 = random.sample(secim2, 8)  # anahtarımızı seçtirmek için random modülü kullanıyoruz
    block16.append(anahtar2)
    i+=1

# print((block16))

stage_four = ""
i=0
while(i<len(block16)):
    for j in block16[i]:
        stage_four += str(j)
    i+=1
print((block16[::-1]))
s2=0
a=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
secim8 = [step1, step2, step3, step4, step5, step6, step7, step8]
keys2 = []
print(secim8[7][::-1])
while(s2<171):

    for i in block16[s2]:

        if(i==secim8[0][a]):
            keys2.append(1)
            a += 1
        if (i == secim8[1][a2]):
            keys2.append(2)
            a2 +=1
        if (i == secim8[2][a3]):
            keys2.append(3)
            a3+=1
        if (i == secim8[3][a4]):            #random sıralanan bloklarımızın sırasını öğrendik
            keys2.append(4)
            a4+=1
        if (i == secim8[4][a5]):
            keys2.append(5)
            a5 += 1
        if (i == secim8[5][a6]):
            keys2.append(6)
            a6 += 1
        if (i == secim8[6][a7]):
            keys2.append(7)
            a7 += 1
        if (i == secim8[7][a8]):
            keys2.append(8)
            a8 += 1


    s2 += 1
print((keys2))


# print(stage_four)
cmap = {'1': (255,255,255),'0': (0,0,0)}

data = [cmap[letter] for letter in stage_four]          #şifrelenmiş olan fotoğramızı şifreli bir halde açıyoruz
img = Image.new('RGB', (150, 150))
img.putdata(data)
img.save("köpke2.png")
img.show()

