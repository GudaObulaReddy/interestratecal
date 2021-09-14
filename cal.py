from flask import Flask, request, jsonify, render_template

import simpleInterest

cal=Flask(__name__)
@cal.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@cal.route('/math', methods=['POST'])
def math_operation():
    if (request.method == 'POST'):
        typeof = request.form['typeof']
        amount = int(request.form['Amount'])
        months = int(request.form['months'])
        interesttype = request.form['interesttype']
        result = " successful "

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
            print(typeof)
            interest = float((12 * interest))
            years = months // 12
            interesttotal, Amounttotal = simpleInterest.compound_interest(amount, interest, years)
            k = months % 12
            if k > 0:
                interest = float(((1 / 12) * interest))
                interesttotal1, Amounttotal = simpleInterest.simple_interest(Amounttotal, k, interest)
                interesttotal= interesttotal+interesttotal1
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
