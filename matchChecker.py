import urllib3
import json

def check_paraphrase(sentence1, sentence2, access_key):
    open_api_url = "http://aiopen.etri.re.kr:8000/ParaphraseQA"

    request_json = {
        "argument": {
            "sentence1": sentence1,
            "sentence2": sentence2
        }
    }

   
    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        open_api_url,
        headers={"Content-Type": "application/json; charset=UTF-8", "Authorization": access_key},
        body=json.dumps(request_json)
    )

    #print("[responseCode] " + str(response.status))
    #print("[responBody]")
    #print(str(response.data, "utf-8"))

    
    result_json = json.loads(response.data.decode('utf-8'))
    
    print(sentence1, sentence2, result_json)#에러 확인하기 위해 잠시 적어둠
    return result_json["return_object"]["result"] != "not paraphrase"


access_key = "c5dd01ba-7adb-4ae6-ae1e-3f494a9c29c6"  
sentence1 = "두통"
sentence2 = "두통"

result = check_paraphrase(sentence1, sentence2, access_key)
print(result)




from sentence_transformers import SentenceTransformer, util

def calculate_similarity(sentence1, sentence2):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    
    embedding1 = model.encode(sentence1, convert_to_tensor=True)
    embedding2 = model.encode(sentence2, convert_to_tensor=True)

    
    similarity = util.pytorch_cos_sim(embedding1, embedding2)[0].item()

    return similarity*100
    #print(f"두 문장의 의미 유사성: {similarity * 100:.2f}%")


sentence1 = "두통"
sentence2 = "이명"


print(calculate_similarity(sentence1, sentence2))
