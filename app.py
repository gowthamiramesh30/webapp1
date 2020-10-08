import flask
import pickle
import pandas as pd

with open(f'model/october.pickle', 'rb') as f:
    model = pickle.load(f)
    
app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET','POST'])
def main():
    if flask.request.method == 'GET':
       return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
       loanamnt= flask.request.form['loanamnt']
       terms= flask.request.form['terms']
       Rateofintrst= flask.request.form['Rateofintrst']
       grade= flask.request.form['grade']
       Experience= flask.request.form['Experience']
       annualinc= flask.request.form['annualinc']
       verificationstatus= flask.request.form['verificationstatus']
       debtincomeratio= flask.request.form['debtincomeratio']
       numbcredit= flask.request.form['numbcredit']
       totalcredits= flask.request.form['totalcredits']
       totalrecint= flask.request.form['totalrecint']
       lastweekpay= flask.request.form['lastweekpay']
       totcurrbal= flask.request.form['totcurrbal']
       MORTGAGE= flask.request.form['MORTGAGE']
       OWN= flask.request.form['OWN']
       RENT= flask.request.form['RENT']
       CarsMajorpurchases= flask.request.form['CarsMajorpurchases']
       Househouseimporovements= flask.request.form['Househouseimporovements']
       WeddingVacation= flask.request.form['WeddingVacation']
       creditcard= flask.request.form['creditcard']
       debtconsolidation= flask.request.form['debtconsolidation']
       medical= flask.request.form['medical']
       smallbusiness= flask.request.form['smallbusiness']
       f= flask.request.form['f']
            
            
       input_variables = 
pd.DataFrame([[loanamnt,terms,Rateofintrst,grade,Experience,annualinc,verificationstatus,debtincomeratio,numbcredit,totalcredits,totalrecint,lastweekpay,totcurrbal,MORTGAGE,OWN,RENT,CarsMajorpurchases,Househouseimporovements,WeddingVacation,creditcard,debtconsolidation,medical,smallbusiness,f]],columns=
['loanamnt','terms','Rateofintrst','grade','Experience','annualinc','verificationstatus','debtincomeratio','numbcredit','totalcredits','totalrecint','lastweekpay','totcurrbal','MORTGAGE','OWN','RENT','CarsMajorpurchases','Househouseimporovements','WeddingVacation','creditcard','debtconsolidation','medical','smallbusiness','f'],dtype=float,index=['input'])

       prediction = model.predict(input_variables)[0]
    
    
       return flask.render_template('main2.html',original_input={'loan_amnt':loanamnt,'terms':terms,'Rate_of_intrst':Rateofintrst,'grade':grade,'Experience':Experience,'annual_inc':annualinc,'verification_status':verificationstatus,'debt_income_ratio':debtincomeratio,'numb_credit':numbcredit,'total_credits':totalcredits,'total_rec_int':totalrecint,'last_week_pay':lastweekpay,'tot_curr_bal':totcurrbal,'MORTGAGE':MORTGAGE,'OWN':OWN,'RENT':RENT,'Cars and Major purchases':CarsMajorpurchases,'House and house imporovements':Househouseimporovements,'Wedding and Vacation':WeddingVacation,'credit_card':creditcard,'debt_consolidation':debtconsolidation,'medical':medical,'small_business':smallbusiness,'f':f},result=prediction,)
    
    
if __name__ == '__main2__':
    app.run()




        