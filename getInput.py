import secret
import requests

def get_input_for_day(day):
    response = requests.get(f'https://adventofcode.com/2021/day/{day}/input', headers={"Cookie":"session="+secret.get_session_id()})
    return response.content.decode("utf-8")

