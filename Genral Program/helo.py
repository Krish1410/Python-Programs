#text prectis

print("hello word")

#veriable prectis

print("Enter yhe first number")
a=input()
print("enter second number")
b=input()
print("sum of entered number is",int(a)+int(b))

#dicsnory prectis

dic={"k":"12","a":"1","b":"2","c":"3"}
print(type(dic))
krish=dic
dic["j"]="17"
del krish["j"]
krish.update({"j":"17"})
print("pleas enter your name fo genret code")
print(dic[input()])

#string prectis

st= "heloo i am a krish"
print(st)
print("wrile a any sententend ")
st=input()
print(type(st))
print(len(st))
print(st[0:5])
print(st[::2])
print(st[-1:-2:-1])
print(st.upper())
print(st.lower())
print(st.lstrip())
print("write a word that last in sentens")
print(st.endswith(input()))
print(st)

#list prectis

li=[]
print(type(li))
print("write kyour 7 best friend name")
print("write a  first name")
li.insert(0,input())
print("write a second name")
li.insert(1,input())
print("write a third name")
li.insert(2,input())
print("write a  forth name")
li.insert(3,input())
print("write a  fifth name")
li.insert(4,input())
print("write a six name")
li.insert(7,input())
print("write a last name")
li.append(input())
print(li)
if li=='krish':
    print("krish is greate")
print(input("write your feedback:"))
print("thankx for feedback......")