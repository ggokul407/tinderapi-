import firebase_admin

from firebase_admin import auth, firestore, storage, credentials

from flask import abort, jsonify, request, redirect
import flask
import json
import request


#------------------- INIT the Flask APP ------------------
app = flask.flask(__name__)
#------------------- INIT the Flask APP ------------------


#--------------------------------------- Firebase Database Start ------------------------------------------------
cred = credentials.Certificate('/content/tinderapp-236ed-firebase-adminsdk-41z3p-a3328a3ce3.json')        
firebase_app = firebase_admin.initialize_app(cred)
# {'databaseURL': '' }
store = firestore.client()
#--------------------------------------- Firebase Database Start ------------------------------------------------

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)

    emailofuser = data.get("email")


     uid = ""
  message = ""


  try:
    user = auth.get_user_by_email(
        email=emailofuser,
        email_verified=False,
        password=passwordofuser)
    message = "sucessfully Got the user"
    uid = user.uid


  except:
    message = "User Not There In Firebase"

return jsonify({}) {"uid":uid, "message":message,"Response":200 }





  @app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json(force=True)



    emailofuser = data.get("email")
    passwordofuser = data.get("passwword")


      uid = ""
  message= ""
  try:
    user = auth.create_user(
        email=emailofuser,
        email_verified=False,
        password=passwordofuser)
    message = "sucessfully created new user"
    uid = user.uid
  except:
    message = "User Already There"

  
  return jsonify({}) {"uid":uid, "message":message,"Response":200 }



  if __name__ =='__main__':
      app.run(host='0.0.0.0', port=5001,debug=False)


      @app.route('/updateUserData', methods=['POST'])
def updateUserData():

  def updateUserData(uid,dit):
  dit_user_details = {}
  dit_user_details['name'] = dit["name"]
  dit_user_details['number'] = dit["number"]
  dit_user_details['email'] = dit["email"]
  dit_user_details['image'] = dit["image"]
  dit_user_details['desp'] = dit["desp"]
  dit_user_details['dob'] = dit["dob"]
  dit_user_details['gender'] = dit["gender"]
  dit_user_details['passion'] = dit["passion"]
  dit_user_details['job'] = dit["job"]
  dit_user_details['company'] = dit["company"]
  dit_user_details['location'] = dit["location"]
  # dit_user_details['location']['lat'] = dit["location"]["coordinate"]["lat"]
  # dit_user_details['location']['lng'] = dit["location"]["coordinate"]["lng"]
  # dit_user_details['location']['city'] = dit["location"]["city"]
  # dit_user_details['location']['state'] = dit["location"]["state"]
  # dit_user_details['location']['country'] = dit["location"]["country"]
  
  store.collection("users").document(uid).set(dit_user_details)


  
  return jsonify({}) {"uid":uid, "message":message,"Response":200 }



        @app.route('/updateUserData', methods=['POST'])
def updateUserData():


dit = {}

dit["name"] = "sneha j"
dit["number"] = "9804223776"
dit["email"] = "snehakutty4@yoo.com"
dit["image"] = "https://firebasestorage.googleapis.com/v0/b/tinder-letsupgrade-51fa2.appspot.com/o/download.jpg?alt=media&token=cc4249e0-7dd7-4cb3-ae99-93d9e36b4e15"
dit["desp"] = "Single"
dit["location"] = {
    "coordinate":{"lat":20.5937, "lng":78.9629},
    "city":"vilupuram",
    "state":"tamilnadu",
    "country":"london"}
dit["dob"] = "29/09/1979"
dit["gender"] ="female"
dit["passion"] = "study"
dit["job"] = "Doctor"
dit["company"] = "SRM"



return jsonify({}) {"uid":uid, "message":message,"Response":200 }


        @app.route('/swipeFun', methods=['POST'])
def swipeFun():

def swipeFun(uidA, uidB, isA_Yes, isB_Yes, firstTime):

  dit =  {}

  dit["uid_A"] = uidA
  dit["uid_B"] = uidB
  dit["isUserA_Yes"] = isA_Yes
  dit["isUserB_ Yes"] = isB_Yes
  dit["isTheOtherUserShownProfileAtLeastOnce"] = firstTime
  dit["createdAt"] = firestore.SERVER_TIMESTAMP
  store.collection("swipes").add(dit)


  return jsonify({}) {"uid":uid, "message":message,"Response":200 }


        @app.route('/getRightswippedFun', methods=['POST'])
def getRightswippedFun():

  def getRightswippedFun(uid):

  docs = store.collection("swipes").stream()

  ditswipes = {}
  for doc in docs:

    if (doc.to_dict().get("uid_A") == uid or doc.it_dict().get("uid_B") == uid) and (doc.to_dict().get("isUserA_Yes") == True and doc.to_dict().get("isUserB_Yes") == True):
      ditswipes[doc.id] = doc.to_dict()

  return ditswipes    
