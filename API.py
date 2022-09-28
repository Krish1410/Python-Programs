from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"
@app.route('/armstrong/<int:n>')
def armstrong(n):
    No=n
    Sum=0
    Order=len(str(No))
    Copy_No=No
    while(No>0):
        digit=No%10
        Sum += digit **Order
        No=No//10
    if Sum==Copy_No:
        print(f"{Copy_No} is an armsrong number")
        return jsonyfy(True)
    else:
        print(f"{Copy_No} is Not an armsrong number")
        return jsonyfy(False)



if __name__ == '__main__':
    app.run()