from flask import Flask, request, jsonify
import datetime,json, math

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    if(request.method=='GET'):
        return "Your at home page", 200
        # return jsonify({"Hello":"World"})
    

@app.route("/test/<date>", methods = ['GET'])
def get_user(date):

    hostel = request.args.get("hostel")

    return jsonify({
        "date":date,
        "hostel":hostel,
    })
    

def getDate(rx):
    rx = list(map(int,rx.split('-')))
    return rx

def getHostel(tx):

    if(tx.upper() in ["BH1","BH2","BH3","BH4","BH5","BH6","BH8","BH9","BH10","BH12"]):
        return "BH"
    elif (tx.upper() in ["LH1","LH2","LH3","LH4","BH11"]):
        return "LH"
    
def getMenu(hostel,datelist):
    date1 = datetime.date(2023, 12, 25)
    date2 = datetime.date(datelist[2],datelist[1],datelist[0])

    t_days = abs((date2 - date1).days) + 1
    # print("Number of days: ",t_days," ",hostel)

    with open(f"./Assets/{hostel}.json", 'r') as f:
        d = json.load(f)

    days = t_days % 28
    week = days / 7
    day = days % 7
    mess_week = f"WEEK{(math.ceil(week))}"

    dic = {
      0: "SUNDAY",
      1: "MONDAY",
      2: "TUESDAY",
      3: "WEDNESDAY",
      4: "THURSDAY",
      5: "FRIDAY",
      6: "SATURDAY"
  }
    mess_day = dic[day]
    data = d[mess_week][mess_day]
    data["WEEK"] = mess_week
    data["DAY"] = mess_day

    return data


@app.route("/getPageInfo/<date>",methods = ['GET'])
def getPageInfo(date):
    menu = {}
    menu["DATE"] = date
    date = getDate(date)

    hostel = request.args.get("hostel")
    hostel = getHostel(hostel)

    menu.update(getMenu(hostel,date))






    return jsonify(menu),200