from flask import Flask, request, jsonify, render_template

import simpleInterest

cal=Flask(__name__)
@cal.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@cal.route('/math', methods=['POST'])
def math_operation():
    if (request.method == 'POST'):
        noofyears=1
        typeof = request.form['typeof']
        if typeof.upper() == 'C':
            noofyears=int(request.form['noofyears'])
        amount = int(request.form['Amount'])
        originalAmount=amount
        yea=int(request.form['yea'])
        month=int(request.form['month'])
        days=int(request.form['days'])
        #months = int(request.form['months'])
        months = (yea*360)+(month*30)+days
        interesttype = request.form['interesttype']
        result = " successful "
        print(noofyears)
        print(type(noofyears))
        if interesttype.upper() == 'P':
            inter = float(request.form['inter'])
            interest = float((1 / 12) * inter)
        elif interesttype.upper() == 'R':
            interest = float(request.form['inter'])
        else:
            result = "enter correct format of interest type"
        if typeof.upper() == 'S':
            interesttotal, Amounttotal = simpleInterest.simple_interest(amount, months, interest)
        elif typeof.upper() == 'C':
            try:
                years=months//(360)
                l=years//noofyears
                if l>=1:
                    for i in range(l):
                        interesttotal,Amounttotal=simpleInterest.simple_interest(amount,(noofyears*12*30),interest)
                        amount=Amounttotal
                m=years % noofyears
                g=months % (12*30)
                y=(m*12*30)+g
                if y>0:
                    interesttotal,Amounttotal=simpleInterest.simple_interest(amount,y,interest)
                    interesttotal=Amounttotal-originalAmount
                else:
                    interesttotal = Amounttotal - originalAmount
            except Exception as e:
                print(e)
        else:
            result = "Select correct simple or compount "
        return render_template("results.html", result=result,interesttotal=interesttotal,Amounttotal=Amounttotal)

@cal.route('/re', methods=['POST'])
def index1():
    return render_template('index.html')
@cal.route('/via_postman', methods=['POST'])
def math_operation_via_postman():
    if (request.method=='POST'):
        typeof=request.json['typeof']
        amount=int(request.json['Amount'])
        months=int(request.json['months'])
        interesttype=request.json['interesttype']
        result=" successful "
        if interesttype.upper()=='P':
            inter=int(request.json['inter'])
            interest=float((1/12)*inter)
        elif interesttype.upper()=='R':
            interest=float(request.json['interest'])
        else:
            result="enter correct format of interest type"
        if typeof.upper()=='S':
            interesttotal,Amounttotal=simpleInterest.simple_interest(amount,months,interest)
        elif typeof.upper()=='C':
            interest=float((12*interest))
            years=months//12
            interestcomp,Amount1=simpleInterest.compound_interest(amount,months,years)
            k=months%12
            if k>0:
                interest=float(((1/12)*interest))
                interesttotal,Amounttotal=simpleInterest.simple_interest(Amount1,k,interest)
        else:
            result="Select correct simple or compount "

        return jsonify(interesttotal,Amounttotal,result)

if __name__=='__main__':
    print('The app is working')
    cal.run()
