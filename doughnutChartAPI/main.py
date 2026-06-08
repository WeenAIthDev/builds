from fastapi import FastAPI #get the tools
import serv.data_processing as process
import serv.visualization as visualise
import serv.ai_service as ai_serv
import config

app = FastAPI() #creates backend app
@app.get("/health")
async def root():
    msg = '{} Alive!'.format(config.APP_NAME)
    return {'message': msg}

@app.post("/visualise-data")
async def visual(dv:process.DataVisual):
   try: 
      result = await visualise.visualise_sales(dv)
      summary = await ai_serv.ai_summary(result)
      return {
        "result": result,
        "summary": summary
    }
    
   except Exception as e:
     print(e)
     return "{}\n Failed to process info".format(e)    