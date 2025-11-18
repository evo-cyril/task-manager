from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models import session , create_app , view_app  , doc , pat , apo 

app=FastAPI(title="appoinmet")
# view doctor list

# @app.get("/list/")
# def list_doc():
#     view=session.query(doc)
#     count=view.count()
#     if count < 1:
#         return JSONResponse({
#             "status":False,
#             "message":"no one available at the moment!"

#         })
    
#     view=view.all()
#     data=[]
#     for i in view:
#         data.append({
#         "id" : i.id,
#         "name":i.name,
#         "department":i.department
#         })
    
#     return JSONResponse({
#         "status":True,
#         "message":"doctors list",
#         "data":data
#     })

#create an appointment

# @app.post("/create/")
# def make(ap:create_app):
#     doctor=session.query(doc.id).filter(doc.is_avail==True).first()
#     if not doctor:
#         return JSONResponse({
#             "status":False,
#             "message":"no doctor available"
#         }
#         )
#     add_app=apo(doctor_id=doctor.id,patient_name=ap.patient_name)
#     session.add(add_app)
#     session.commit()
#     session.refresh(add_app)
#     review={
#             "id":doctor.id,
            

#     }
#     return JSONResponse({
#         "status":True,
#         "message":"process successfully",
#         "data":review
# })

#fetch appointment

@app.get("/appointments/")
def show_app():
    show=session.query(apo)
    count=show.count()


    if count<1:
        return JSONResponse({
            "status":False,
            "message":"no appointments"
        })
    show=show.all()
    data=[]
    for a in show:
        data.append({
            "id":a.ap_id,
            "name":a.patient_name

        })
    return JSONResponse({
        "status":True,
        "message":"sucessfully fetched",
        "data":data
    })    


