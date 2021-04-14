import os
import string
import random # define the random module  
from common.AppConstants import success_code, internal_server_error_code, failure_key,bad_request_error_code
def unique_token_generator():
    try:
        S = 10  # number of characters in the string.
        # call random.choices() string module to find the string in Uppercase + numeric data.
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
        #The randomly generated string
        with open(os.path.join(os.getcwd(), "file.txt"), 'r') as f:
            score = [line.rstrip('\n') for line in f]
        score.append(ran)
        with open("file.txt", 'w') as f:
            for each in score:
                f.write(str(each) + '\n')
        return {"status":"success","message":"unique token generated is "+str(ran)}
    except Exception as e:
        return {"status":"success","message":"unique token generator raised exception "+str(e)}
def assign_unique_token(input_data):
    """
    :param input_data: unique id
    :return:
    """
    try:
        unique_assigned_token = input_data["unique_token"]
        count = 0
        with open("file.txt", "r") as f:
            lines = f.readlines()
        with open("file.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != unique_assigned_token:
                    count = count+1
                    f.write(line)
        if count == 0:
            response_obj = {"status":"Failed","message":"No free Token"}
            return response_obj,bad_request_error_code
        else:
            response_obj = {"status": "Success", "message": "Token is assigned"}
            return response_obj,200
    except Exception as e:
        raise {"Exception raised while assigning unique token", str(e)}
def re_assigned_token(input_data):
    """
    :param input_data:
    :return:
    """
    try:
        unique_re_assigned_token = input_data["unique_token"]
        with open(os.path.join(os.getcwd(), "file.txt"), 'r') as f:
            score = [line.rstrip('\n') for line in f]
        score.append(unique_re_assigned_token)
        with open("file.txt", 'w') as f:
            for each in score:
                f.write(str(each) + '\n')
        return {"status":"success","message":"unique token reassigned is "+str(unique_re_assigned_token)}
    except Exception as e:
        return {"status":"success","message":"unique token reassigned raised exception "+str(e)}
def delete_token(input_data):
    """
    :param input_data:
    :return:
    """
    try:
        unique_token = input_data["unique_token"]
        with open(os.path.join(os.getcwd(), "file.txt"), 'r') as f:
            score = [line.rstrip('\n') for line in f]
        score.remove(unique_token)
        with open("file.txt", 'w') as f:
            for each in score:
                f.write(str(each) + '\n')
        return {"status": "success", "message": "unique token deleted is " + str(unique_token)}
    except Exception as e:
        return {"status": "success", "message": "unique token deletion raised exception " + str(e)}