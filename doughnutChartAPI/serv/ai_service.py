from google import genai
import config


async def ai_summary(result):
    try:
        client = genai.Client(api_key=config.GEMINI_API_KEY)

        response = client.models.generate_content(
            model=config.MODEL,
            contents=
                "Analyze this sales dataset "
                "total:{} "
                "highest_value:{} "
                "lowest_value:{} "
                "average_value:{} "
                "Provide a short business summary".format(
                    result["total"],
                    result["highest_category"],
                    result["lowest_category"],
                    result["average_value"]
                )
        )

        return response.text

    except Exception as e:
        print(e)
        return  "{}\n AI summary unavailable. Analytics completed successfully".format(e)