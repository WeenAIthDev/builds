import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd 
import uuid
import serv.data_processing as proc
import config
import os
import cloudinary
from cloudinary.uploader import upload
#import serv.ai_service as ai
#app = FastAPI() #creates backend app



'''@app.post("/analyze-sales")
async def analyze_sales(data:Data):
    dt = processing_sales(data)
    data_analysis = {
        "Sum of Values": dt[2],
        "Highest Category": dt[0],
        "Lowest Category": dt[1]
    }
    return data_analysis
'''
cloudinary.config(
    cloud_name=config.CLOUDINARY_CLOUD_NAME,
    api_key=config.CLOUDINARY_API_KEY,
    api_secret=config.CLOUDINARY_API_SECRET
)
    
def processing_sales(dt):
    value = dt['values']
    max_values = max(value)
    min_values = min(value)
    sum_values = sum(value)
    avg_value = sum(value)/len(value)
    keys = dt['label']
    index = 0
    for v in value:
        index = index + 1
        if max_values == v:
            max_index_values = keys[index-1]
        
        if min_values == v:
            min_index_values = keys[index-1]

    return max_index_values, min_index_values, sum_values, avg_value


async def visualise_sales(dv:proc.DataVisual):
    try:
      color_map = dv.color
      fig_size = dv.figsize
      fig,ax = plt.subplots(figsize=fig_size)
      ax.pie(dv.values, labels=dv.label, colors=pd.Series(dv.label).map(color_map).fillna(config.DEFAULT_COLOR))
      circle_draw = patches.Circle((0,0), radius=config.RADIUS, color=config.DEFAULT_COLOR)
      ax.add_patch(circle_draw)
      plt.legend(title=dv.title)
      ud = str(uuid.uuid4())
      os.makedirs(config.OUTPUT_FOLDER, exist_ok=True)
      filename = '{}/{}_{}_{}.png'.format(config.OUTPUT_FOLDER, config.CHART_PREFIX, dv.title, ud)
      fig.savefig(filename)
      result = upload(filename)
      dt = {
        'label':dv.label,
        'values':dv.values
     }
    #print(dt) test
      data_analysis = processing_sales(dt)
      message = {
     "status": "success",
     "chart_url": result['secure_url'],
     "total":data_analysis[2],
     "highest_category":data_analysis[0],
     "lowest_category":data_analysis[1],
     "average_value": data_analysis[3]


    }
      return message

    except Exception as e:
     print(e)
     return "{}\n Analytics failed".format(e)

    











#@app.get("/health") #creates health endpoint and checks if the endpoint exists in backend system if it is then root() gets executed  
#@app.get("/add/{operator}/{operator2}")
'''
Client
↓
POST /analyze-sales
↓
Validation
↓
Analytics Service
↓
Visualization Service
↓
Response
'''
'''def processing_stuff(message):
    msg = str(message.message)
    up = msg.upper()    
    words = msg.split(" ")
    wcount = len(words)
    return msg,up,wcount #tuple
class Item(BaseModel):
   name: str
   price: float
   description: str | None = None

class Message(BaseModel):
    message: str

@app.post("/process-text")
async def message_process(message:Message):
    ps = processing_stuff(message)
    processed_msg = {
        "original":ps[0],
        "uppercase":ps[1],
        "word_count":ps[2]

    }
    return processed_msg

@app.post("/items/")
async def items_add(item: Item):
    return item


async def add(operator:int,operator2:int):
    total = operator + operator2
    return total
async def root():
    return {'message':'Backend Alive!'} #the format of request to be sent back
'''
'''
import matplotlib.pyplot as plt
import matplotlib.patches as patches 
fig, ax = plt.subplots(figsize=())
x = df[]
y = df[]
color_map = {}
ax.pie(y, labels=x, color=df[''].map(color_map).fillna('white'))
circle_patches = ax.circle((0,0), radius=0.5, color='white')
ax.add_patch(circle_patches)
plt.legend(title="")
plt.show()
'''